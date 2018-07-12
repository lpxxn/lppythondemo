from kafka import KafkaConsumer
import multiprocessing, time


class Consumer(multiprocessing.Process):
    def __init__(self):
        multiprocessing.Process.__init__(self)
        self.stop_event = multiprocessing.Event()

    def stop(self):
        self.stop_event.set()

    def run(self):
        consumer = KafkaConsumer(bootstrap_servers=['rr-kafka-0001:9092', 'rr-kafka-0002:9092', 'rr-kafka-0003:9092'],
                                 auto_offset_reset='earliest',
                                 consumer_timeout_ms=1000 * 2)
        consumer.subscribe(['useronlinestatus'])
        while not self.stop_event.is_set():
            for message in consumer:
                print(message)
                if self.stop_event.is_set():
                    break

        consumer.close()


def main():
    tasks = [
        Consumer()
    ]

    for t in tasks:
        t.start()

    time.sleep(600)

    for task in tasks:
        task.stop()

    for task in tasks:
        task.join()


if __name__ == "__main__":
    main()
