from kafka import KafkaConsumer,KafkaProducer


def consumer_go():
    #consumer = KafkaConsumer('test')
    # topic:test
    consumer = KafkaConsumer('test', group_id='py_group')
    # consumer = KafkaConsumer('test', group_id='py_group_second')
    for msg in consumer:
        print(msg)

def producter_go():
    broker_list = ['localhost:9092','localhost:9093','localhost:9094'] #不用全部的broker 
    producer = KafkaProducer(bootstrap_servers=broker_list)
    for i in range(10):
        result = producer.send('test',b'hello')
        print(i)
    producer.flush()

consumer_go()
