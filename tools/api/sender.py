import threading
import uuid

import pika

import tools.utility.log as log

LOGGER = log.get_logger(__name__)


class Sender:

    def __init__(self):
        LOGGER.debug('Initializing sender')
        self.__response_type = ['Failed', 'In progress', 'Finished successfully', 'does not exist']
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(durable=True, exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)
        self.response = {}
        threading.Timer(120, self.keep_alive).start()

    def keep_alive(self):
        LOGGER.debug('Keeping alive the connection in between api and receiver')
        self.connection.process_data_events()
        threading.Timer(120, self.keep_alive).start()

    def on_response(self, ch, method, props, body):
        self.response[props.correlation_id] = body

    def get(self, correlation_id):
        LOGGER.debug('Trying to get response')
        self.connection.process_data_events()
        if correlation_id not in self.response:
            return self.__response_type[3]
        else:
            return self.response[correlation_id]

    def send(self, n):
        LOGGER.info('Sending data to queue')
        corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='module_queue',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,
                                       correlation_id=corr_id,
                                   ),
                                   body=str(n))
        self.response[corr_id] = self.__response_type[1]
        return corr_id


