import pika
import uuid


class Sender:

    def __init__(self):
        self.__response_type = ['Failed', 'In progress', 'Finished successfully', 'does not exist']
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

        self.channel = self.connection.channel()

        result =  self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)
        self.response = {}

    def on_response(self, ch, method, props, body):
        self.response[props.correlation_id] = body

    def get(self, correlation_id):
        self.connection.process_data_events()
        if correlation_id not in self.response:
            return self.__response_type[3]
        else:
            return self.response[correlation_id]

    def send(self, n):
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


