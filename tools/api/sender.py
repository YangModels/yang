import datetime
import uuid

import pika

import tools.utility.log as log

LOGGER = log.get_logger(__name__, '/home/miroslav/log/api/yang.log')


class Sender:
    def __init__(self):
        LOGGER.debug('Initializing sender')
        self.__response_type = ['Failed', 'In progress',
                                'Finished successfully', 'does not exist']
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters('127.0.0.1'))

        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='module_queue')

        self.__response_file = 'correlation_ids'

    def get_response(self, correlation_id):
        """Get response according to job_id. It can be either 
        'Failed', 'In progress', 'Finished successfully' or 'does not exist'
                Arguments:
                    :param correlation_id: (str) job_id searched between
                     responses
                    :return one of the following - 'Failed', 'In progress',
                        'Finished successfully' or 'does not exist'
        """
        LOGGER.debug('Trying to get response')

        f = open('./correlation_ids', 'r')
        lines = f.readlines()
        f.close()
        for line in lines:
            if correlation_id == line.split('- ')[1].strip():
                return line.split('- ')[-1]

        return self.__response_type[3]

    def send(self, arguments):
        """Send data to receiver queue to process
                Arguments:
                    :param arguments: (str) arguments to process in receiver
                    :return job_id
        """
        LOGGER.info('Sending data to queue with arguments: {}'
                    .format(arguments))
        corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='module_queue',
                                   properties=pika.BasicProperties(
                                       correlation_id=corr_id,
                                   ),
                                   body=str(arguments))
        with open(self.__response_file, 'a') as f:
            line = '{} -- {} - {}\n'.format(datetime.datetime.now().ctime(),
                                            corr_id, self.__response_type[1])
            f.write(line)

        return corr_id
