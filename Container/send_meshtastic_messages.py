import os
import paho.mqtt.client as mqtt
# import time
# import meshtastic
# import meshtastic.tcp_interface


mqtt_host = os.getenv('MQTT_HOST')
mqtt_user = os.getenv('MQTT_USER')
mqtt_password = os.getenv('MQTT_PASSWORD')
mqtt_topic = os.getenv('MQTT_TOPIC')
mqtt_message = 'hello world'

# mqtt_client = mqtt.Client(client_id="myPy")
mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqtt_client._client_id = "meshtastic_client"
mqtt_client.username_pw_set(username=mqtt_user, password=mqtt_password)
mqtt_client.connect(mqtt_host,  port=1883, keepalive=60)  # Replace with your broker's address and port

mqtt_client.publish(mqtt_topic, mqtt_message)
