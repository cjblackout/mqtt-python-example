# MQTT Application with Mosquitto

This is a simple MQTT application that consists of a sender and receiver, communicating through the Mosquitto MQTT broker. The sender periodically generates prime numbers and publishes them to the broker, while the receiver subscribes to the prime number topic and displays the received messages.

## Prerequisites

Before running the application, make sure you have the following prerequisites installed:

- Docker: Ensure that Docker is installed on your machine. You can download and install Docker from the official website: [https://www.docker.com](https://www.docker.com)

## Getting Started

Follow these steps to set up and run the MQTT application:

1. Clone the repository:  
   ```
   git clone <repository_url>
   cd mqtt-application
   ```

2. Configure Mosquitto:
   - Open the `mosquitto.conf` file and modify it according to your needs.
   - Ensure that the bridge configuration is correctly set to connect to the sender and receiver containers.
   - Save the changes to the `mosquitto.conf` file.

3. Build and run the Docker containers:
   ```
   docker-compose up -d
   ```

4. Monitor the logs:
   ```
   docker-compose logs -f
   ```

   The logs will display the messages sent and received by the application.

5. To stop the application, run the following command:
   ```
   docker-compose down
   ```

## Configuration

- **Sender Configuration**: The `sender.py` file contains the sender application logic. You can modify the `calculate_prime_numbers()` function to generate prime numbers according to your requirements. Additionally, you can adjust the time interval between each prime number generation by modifying the `time.sleep()` value.

- **Receiver Configuration**: The `receiver.py` file contains the receiver application logic. You can customize the `on_message()` function to handle the received messages as per your application needs.

- **Mosquitto Configuration**: The `mosquitto.conf` file configures the Mosquitto MQTT broker. You can modify it to adjust various broker settings, including port configuration, network settings, and bridge connections.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This MQTT Application with Mosquitto is open-source software licensed under the [MIT License](LICENSE).

## Acknowledgements

This application was developed using the Eclipse Paho MQTT Python client library and the Eclipse Mosquitto MQTT broker.

---

## Documentation

### Sender.py

The `sender.py` script is responsible for generating prime numbers and publishing them to the MQTT broker. Here's an overview of its functionality:

- `calculate_prime_numbers()`: This function generates prime numbers using a generator approach. It checks for prime numbers by iterating from 2 and incrementing the number until it finds the next prime number.
- `send_message(message)`: This function establishes a connection with the MQTT broker and publishes the provided message to the topic `pythonapp/prime`.

The script runs in an infinite loop, continuously generating prime numbers and publishing them to the MQTT broker with a delay of 5 minutes between each publication.

### Receiver.py

The `receiver.py` script is responsible for subscribing to the MQTT broker and receiving messages published to the topic `pythonapp/prime`. Here's an overview of its functionality:

- `on_connect(client, userdata, flags, rc)`: This function is called when the client connects to the MQTT broker. It prints a confirmation message upon successful connection and subscribes to the topic `pythonapp/prime`.
- `on_message(client, userdata, msg)`: This function is called when a message is received from the subscribed topic. It prints the received message payload.

The script uses the `mqtt.Client` class from the Paho MQTT Python client library to establish a connection with the broker. It then sets the `on_connect` and `on_message` callbacks accordingly. Finally, the `client.loop_forever()` function is called to start the MQTT client's network loop, which handles the communication with the broker.

### Docker Compose

The `docker-compose.yaml` file is used to define and manage the Docker containers required for the MQTT application. It includes the following services:

- `sender`: Builds an image from the `sender` directory and runs the `sender.py` script. It depends on the `mosquitto` service and exposes port `1883`.
- `receiver`: Builds an image from the `receiver` directory and runs the `receiver.py` script. It depends on the `mosquitto` service and exposes port `1883`.
- `mosquitto`: Uses the official Eclipse Mosquitto image, sets up the necessary network and port configurations, and mounts the `mosquitto.conf` file for custom configuration.

The services are connected to a shared `mqtt_network` bridge network, allowing them to communicate with each other through the Mosquitto broker.

### Mosquitto Configuration (mosquitto.conf)

The `mosquitto.conf` file configures the Mosquitto MQTT broker. Here's a breakdown of the configuration settings:

- `persistence`: Enables persistence to store subscriptions and message data.
- `persistence_location`: Specifies the location where persistence data is stored.
- `listener 1883`: Sets up a listener on port 1883 for MQTT connections.
- `allow_anonymous`: Allows anonymous clients to connect to the broker.
- `connection_messages`: Enables logging of client connection and disconnection messages.
- `log_type all`: Configures the log level to include all types of log messages.

The configuration also includes additional settings for network configuration, such as listeners for WebSocket and MQTT over WebSocket connections. Moreover, it defines bridge configurations for connecting to other containers, specifically the `sender` and `receiver` containers, with the topics `pythonapp/prime` configured for both incoming and outgoing messages.

---
