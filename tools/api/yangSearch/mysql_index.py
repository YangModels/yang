import MySQLdb
import MySQLdb.cursors
import json
import re
import tools.utility.log as lo

LOGGER = lo.get_logger('sql')
# DBF = '/var/yang/yang.db'

conn = None

# you must create a Cursor object. It will let
#  you execute all the queries you need

cur = None

# Use all the SQL you like
# cur.execute("SELECT * FROM YOUR_TABLE_NAME")

# print all the first cell of all the rows
# for row in cur.fetchall():
#     print(row[0])

# db.close()


def __mysql_regexp(pattern, buf, modifiers=re.I | re.S):
    if pattern is not None and buf is not None:
        exp = re.compile(pattern, modifiers)
        return exp.search(buf) is not None

    return False


def create_connection(dbHost, dbPass, dbName, dbUser):
    connection = MySQLdb.connect(host=dbHost,  # your host, usually localhost
                           user=dbUser,  # your username
                           passwd=dbPass,  # your password
                           db=dbName)  # name of the data base
    cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    return connection, cursor


__schema_types = [
    'typedef',
    'grouping',
    'feature',
    'identity',
    'extension',
    'rpc',
    'container',
    'list',
    'leaf-list',
    'leaf',
    'notification',
    'action'
]

__search_fields = [
    'argument',
    'description',
    'module'
]

__node_data = {
    'name': 'argument',
    'description': 'description',
    'path': 'path',
    'type': 'statement'
}


def do_search(options, dbHost, dbName, dbPass,  dbUser):
    global conn, cur
    opts = json.loads(options)
    if conn is None:
        conn, cur = create_connection(dbHost, dbPass, dbName, dbUser)
    else:
        if not conn.open:
            conn, cur = create_connection(dbHost, dbPass, dbName, dbUser)
    try:
        case_sensitivity = ''
        if 'case-sensitive' in opts and opts['case-sensitive']:
            case_sensitivity = 'BINARY '

        sql = 'SELECT yi.module, yi.revision, yi.organization, yi.path, yi.statement, yi.argument, '
        sql += 'yi.description, yi.properties, MAX(mo.revision) AS latest_revision '
        sql += 'FROM yindex yi, modules mo WHERE ' + case_sensitivity
        search_term = opts['search']
        sts = __search_fields
        if 'search-fields' in opts:
            sts = opts['search-fields']

        wclause = []
        # if 'type' in opts and opts['type'] == 'regex':
        #    for field in sts:
        #        if field in __search_fields:
        #            wclause.append('REGEXP(:descr, yi.{})'.format(field))
        # else:
        for field in sts:
            if field in __search_fields:
                wclause.append('yi.{} LIKE "%{}%"'.format(field, search_term))

        sql += '({})'.format(' OR '.join(wclause))
        if 'schema-types' in opts:
            queries = []
            sql += ' AND ('
            for st in opts['schema-types']:
                if st in __schema_types:
                    queries.append("yi.statement = '{}'".format(st))
            sql += ' OR '.join(queries)
            sql += ')'

        sql += ' AND (mo.module = yi.module) GROUP BY yi.argument, yi.module, yi.revision,'
        sql += ' yi.organization, yi.path, yi.statement, yi.description, yi.properties'
        cur.execute(sql)

        results = []
        filter_list = __node_data.keys()
        if 'filter' in opts and 'node' in opts['filter']:
            filter_list = opts['filter']['node']
        rows = cur.fetchall()
        for row in rows:
            module = {'latest_revision': row['latest_revision'], 'name': row[
                'module'], 'revision': row['revision'], 'organization': row['organization']}
            result = {'module': module}
            result['node'] = {}
            for nf in filter_list:
                if nf in __node_data:
                    result['node'][nf] = row[__node_data[nf]]

            results.append(result)

        return results
    except MySQLdb.Error as e:
        raise Exception("Error searching for {}: {}".format(
            opts['search'], e.args[0]))
