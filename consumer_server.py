from kafka import KafkaConsumer
import json



def run_consumer():
    consumer = KafkaConsumer(
        'com.udacity.calls',
         bootstrap_servers=['localhost:9092'],
         auto_offset_reset='earliest',
         enable_auto_commit=True,
         group_id='group-2')

    for message in consumer:
        message = message.value
        print('{}'.format(message))


if __name__ == "__main__":
    run_consumer()
