import os
import paho.mqtt.client as mqtt
import time
import meshtastic
import meshtastic.tcp_interface
from pubsub import pub


def onReceive(packet, interface): # called when a packet arrives
    mqtt_message = meshtastic.util.message_to_json(packet["raw"], multiline=True)
    print("received message:", len(mqtt_message))
    mqtt_client.publish(mqtt_topic, mqtt_message, qos=2)
    print(f"Current mqtt outbound queue size: {len(mqtt_client._out_messages)}")

def onConnection(interface, topic=pub.AUTO_TOPIC): # called when we (re)connect to the radio
    # defaults to broadcast, specify a destination ID if you wish
    # interface.sendText("hello mesh")
    print("connected")

def onConnectionLost(interface):
    print("lost connection")

    while True:
        try:
            interface = meshtastic.tcp_interface.TCPInterface(hostname=meshtastic_host)

            break
        except Exception as e:
            print("error:", e)
            print("type:", type(e))
            time.sleep(60)

def on_connect(client, userdata, connect_flags, reason_code, properties):
    if reason_code == 0:
        print("Connected to MQTT Broker!")
    else:
        print(f"Failed to connect, return code {reason_code}")

def on_disconnect(client, userdata, disconnect_flags, reason_code, properties):
    print("Disconnected from MQTT Broker")
    if reason_code != 0:
        print(f"Unexpected disconnection, return code {reason_code}")
        # Implement reconnection logic here if needed
        # client.reconnect()

retry_timeout = os.getenv('MESHTASTIC_RECONNECT_TIMEOUT')

if retry_timeout is None:
    retry_timeout = 60
else:
    try:
        retry_timeout = int(retry_timeout)
    except:
        retry_timeout = 60

meshtastic_host = os.getenv('MESHTASTIC_HOST')
mqtt_host = os.getenv('MQTT_HOST')
mqtt_user = os.getenv('MQTT_USER')
mqtt_password = os.getenv('MQTT_PASSWORD')
mqtt_topic = os.getenv('MQTT_TOPIC')

# Create a client instance
mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqtt_client.max_queued_messages_set(10000)
mqtt_client.on_connect = on_connect
mqtt_client.on_disconnect = on_disconnect
mqtt_client.username_pw_set(username=mqtt_user, password=mqtt_password)
# todo failure to connect on start
mqtt_client.connect(mqtt_host,  1883, 60)  # Replace with your broker's address and port
mqtt_client.loop_start()

pub.subscribe(onReceive, "meshtastic.receive")
pub.subscribe(onConnection, "meshtastic.connection.established")
pub.subscribe(onConnectionLost, "meshtastic.connection.lost")
interface = None

while True:
    try:
        interface = meshtastic.tcp_interface.TCPInterface(hostname=meshtastic_host)

        break
    except Exception as e:
        print("error:", e)
        print("type:", type(e))
        time.sleep(60)

while True:
    time.sleep(1000)
