import os
import paho.mqtt.client as mqtt
import time
import meshtastic
import meshtastic.tcp_interface
from pubsub import pub

def onReceive(packet, interface): # called when a packet arrives

    mqtt_message = meshtastic.util.message_to_json(packet["raw"], multiline=True)

    mqtt_client.publish(mqtt_topic, mqtt_message)

def onConnection(interface, topic=pub.AUTO_TOPIC): # called when we (re)connect to the radio
    # defaults to broadcast, specify a destination ID if you wish
    # interface.sendText("hello mesh")
    noop = True

meshtastic_host = os.getenv('MESHTASTIC_HOST')
mqtt_host = os.getenv('MQTT_HOST')
mqtt_user = os.getenv('MQTT_USER')
mqtt_password = os.getenv('MQTT_PASSWORD')
mqtt_topic = os.getenv('MQTT_TOPIC')

# Create a client instance
mqtt_client = mqtt.Client()
mqtt_client.username_pw_set(username=mqtt_user, password=mqtt_password)
mqtt_client.connect(mqtt_host,  1883, 60)  # Replace with your broker's address and port

pub.subscribe(onReceive, "meshtastic.receive")
pub.subscribe(onConnection, "meshtastic.connection.established")
interface = meshtastic.tcp_interface.TCPInterface(hostname=meshtastic_host)

while True:
    time.sleep(1000)

# interface.close()
# client.disconnect()