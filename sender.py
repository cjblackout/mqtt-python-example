import time
import math
import random
import paho.mqtt.client as mqtt

broker_host = "mosquitto"
broker_port = 1884

def calculate_prime_numbers():
    # Function to calculate prime numbers
    primes = []
    num = 2
    while True:
        if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
            primes.append(num)
        num += 1
        yield primes[-1]

def send_message(message):
    client = mqtt.Client()
    client.connect(broker_host, broker_port, bind_port=21884)
    client.publish("pythonapp/prime", message)
    client.disconnect()

if __name__ == '__main__':
    prime_generator = calculate_prime_numbers()
    while True:
        next_prime = next(prime_generator)
        print("Sending prime number:", next_prime)
        send_message(str(next_prime))
        time.sleep(5 * 60)  # Wait for 5 minutes
