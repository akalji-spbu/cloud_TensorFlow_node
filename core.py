import pika
import json
import requests
from config import config

print("Connected to "+config.AMQPServer)

AMQPConnection = pika.ConnectionParameters(
        host=config.AMQPServer,
        port=config.AMQPPort,
        credentials=pika.credentials.PlainCredentials(config.AMQPUser, config.AMQPPassword),
        virtual_host=config.AMQPVHost,
    )

def sendMessageToFrontend(Message):
    # Open a connection to RabbitMQ on localhost using all default parameters
    connection = pika.BlockingConnection(parameters=AMQPConnection)

    # Open the channel
    channel = connection.channel()

    # Declare the queue
    channel.queue_declare(queue='solved')

    channel.basic_publish(exchange='',
                          routing_key='solved',
                          body=Message)
    connection.close()

def checkTasks():
    connection = pika.BlockingConnection(parameters=AMQPConnection)
    channel = connection.channel()

    channel.queue_declare(queue='toSolve')

    method_frame, header_frame, body = channel.basic_get('toSolve')
    if method_frame:
        #print(method_frame, header_frame, body)
        channel.basic_ack(method_frame.delivery_tag)
        message = json.loads(body)
        return message
    else:
        return dict()

def downloadImage(id):
    session = requests.Session()
    image = session.get("https://recogniser.akalji.ru/images/"+str(id)).content
    f = open("images/"+id+".jpg", 'wb')
    f.write(image)


def recognise(picture):
    pass

