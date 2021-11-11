from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='IP:PORT')

for _ in range(100):
    producer.send('foobar', b'some_message_bytes')
    print('data')