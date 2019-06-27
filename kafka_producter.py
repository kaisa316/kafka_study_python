from kafka import KafkaConsumer,KafkaProducer
import time
import random

def producter_go():
    broker_list = ['localhost:9092','localhost:9093','localhost:9094'] #不用全部的broker，有几个就可以
    producer = KafkaProducer(bootstrap_servers=broker_list)
    #ts = random.randint(1,100)
    #msg = bytes([ts])
    for i in range(10):
        result = producer.send('test',b'123')
    producer.flush()

producter_go()
