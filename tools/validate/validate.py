import ConfigParser
import argparse
import errno
import os
import smtplib
import sys
from email.mime.text import MIMEText

import MySQLdb


def query_yes_no(question, default=None):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


def query_create(question):
    """Ask a path like question via raw_input() and return their answer.

    "question" is a string that is presented to the user.

    The return value is path that should be added to database.
    """

    while True:
        sys.stdout.write(question)
        choice = raw_input().lower()

        if choice.startswith('/'):
            choice = choice[1:]
        if choice.endswith('/'):
            choice = choice[:-1]

        if choice == '/':
            choice_without_last = '/'
        else:
            if len(choice.split('/')) > 1:
                choice_without_last = '/'.join(choice.split('/')[:-1])
            else:
                choice_without_last = choice

        if os.path.isdir('../../' + choice):
            return choice
        else:
            print ('Path ' + choice_without_last + ' does not exist.')
            create = query_yes_no('would you like to create path ' + choice)
            if create:
                try:
                    os.makedirs(choice)
                except OSError as e:
                    # be happy if someone already created the path
                    if e.errno != errno.EEXIST:
                        raise
                return choice


def connect():
    try:
        db = MySQLdb.connect(host=dbHost, db=dbName, user=dbUser, passwd=dbPass)
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        # execute SQL query using execute() method.
        cursor.execute("SELECT * FROM users_temp")
        data = cursor.fetchall()
        db.close()

        return data
    except MySQLdb.MySQLError as err:
        print("Cannot connect to database. MySQL error: " + str(err))


def delete():
    try:
        db = MySQLdb.connect(host=dbHost, db=dbName, user=dbUser, passwd=dbPass)
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        # execute SQL query using execute() method.
        cursor.execute("""DELETE FROM users_temp WHERE Id=%s LIMIT 1""", (row[0], ))
        db.commit()
        db.close()
    except MySQLdb.MySQLError as err:
        print("Cannot connect to database. MySQL error: " + str(err))


def copy():
    try:
        db = MySQLdb.connect(host=dbHost, db=dbName, user=dbUser, passwd=dbPass)
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        # execute SQL query using execute() method.

        cursor.execute("""UPDATE users_temp SET AccessRightsVendor=%s, AccessRightsSdo=%s WHERE Id=%s""",
                       (vendor_path, sdo_path, row[0],))
        cursor.execute("""INSERT INTO users(Username, Password, Email, ModelsProvider, FirstName, LastName,
                          AccessRightsVendor, AccessRightsSdo) SELECT Username, Password, Email, ModelsProvider,
                          FirstName, LastName, AccessRightsVendor, AccessRightsSdo FROM users_temp WHERE Id=%s""",
                       (row[0],))
        db.commit()
        db.close()
    except MySQLdb.MySQLError as err:
        print("Cannot connect to database. MySQL error: " + str(err))


def send_email(to, vendor, sdo):
    msg = MIMEText('Your rights were granted ')
    msg['Subject'] = 'Access rights granted for vendor path ' + vendor + ' and organization for sdo ' + sdo
    msg['From'] = 'info@yangcatalog.org'
    msg['To'] = to

    s = smtplib.SMTP('localhost')
    s.sendmail('info@yangcatalog.org', to, msg.as_string())
    s.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script to validate user and add him to database")
    parser.add_argument('--config-path', type=str, default='../utility/config.ini',
                        help='Set path to config file')
    args = parser.parse_args()
    config_path = os.path.abspath('.') + '/' + args.config_path
    config = ConfigParser.ConfigParser()
    config.read(config_path)
    dbHost = config.get('Validate-Section', 'dbIp')
    dbName = config.get('Validate-Section', 'dbName')
    dbUser = config.get('Validate-Section', 'dbUser')
    dbPass = config.get('Validate-Section', 'dbPassword')
    dbData = connect()
    vendor_path = None
    sdo_path = None
    for row in dbData:
        while True:
            print ('The user ' + row[5] + ' ' + row[6] + ' (' + row[1] + ')' + ' is from organization ' + row[4])
            vendor_access = query_yes_no('Do they need vendor access?')
            if vendor_access:
                vendor_path = query_create('What is their vendor branch ')
            sdo_access = query_yes_no('Do they need sdo (model) access?')
            if sdo_access:
                sdo_path = query_create('What is their model organization ')
            want_to_create = False
            if sdo_path or vendor_path:
                want_to_create = query_yes_no('Do you want to create user ' + row[5] + ' ' + row[6] + ' (' + row[1]
                                              + ')' + ' from organization ' + row[4] + ' with path for vendor '
                                              + repr(vendor_path) + ' and organization for sdo ' + repr(sdo_path))
            if want_to_create:
                if sdo_path is None:
                    sdo_path = ''
                if vendor_path is None:
                    vendor_path = ''
                copy()
                delete()
                send_email(row[3], repr(vendor_path), repr(sdo_path))
                break
            else:
                print('Skipping user ' + row[5] + ' ' + row[6] + ' (' + row[1] + ')' + ' from organization ' + row[4]
                      + ' has no path set.')
                if query_yes_no('Would you like to delete this user from temporary database?'):
                    delete()
                break
