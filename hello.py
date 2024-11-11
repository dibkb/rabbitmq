import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

# channel.basic_publish(exchange='',
#                       routing_key='hello',
#                       body='Hello World!')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Mic testing....🔥')

print(" [x] Sent Message")

connection.close()