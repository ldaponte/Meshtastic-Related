import os
import paho.mqtt.client as mqtt
import time
import meshtastic
import meshtastic.tcp_interface
from pubsub import pub
import threading


checkInterfaceTimer = None

def onCheckInterface(interface):
    print("checking interface")
    print("is connected:", interface.isConnected.is_set())
    interface.sendHeartbeat()
    global checkInterfaceTimer
    checkInterfaceTimer = None
    checkInterfaceTimer = threading.Timer(10, onCheckInterface, args=(interface,))
    checkInterfaceTimer.start()

def onReceive(packet, interface): # called when a packet arrives
    mqtt_message = meshtastic.util.message_to_json(packet["raw"], multiline=True)
    print("received message:", len(mqtt_message))
    # mqtt_client.publish(mqtt_topic, mqtt_message)

def onConnection(interface, topic=pub.AUTO_TOPIC): # called when we (re)connect to the radio
    # defaults to broadcast, specify a destination ID if you wish
    # interface.sendText("hello mesh")
    print("connected")
    noop = True

def onConnectionLost(interface):

    print("lost connection")

    while True:
        try:
            interface = meshtastic.tcp_interface.TCPInterface(hostname=meshtastic_host)
            # interface.heartbeatTimer.interval = 10
            # checkInterfaceTimer = threading.Timer(10, onCheckInterface, args=(interface,))
            # checkInterfaceTimer.start()
            break
        except Exception as e:
            print("error:", e)
            print("type:", type(e))
            time.sleep(60)

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
pub.subscribe(onConnectionLost, "meshtastic.connection.lost")
interface = None

while True:
    try:
        interface = meshtastic.tcp_interface.TCPInterface(hostname=meshtastic_host)
        # interface.heartbeatTimer.interval = 10

        break
    except Exception as e:
        print("error:", e)
        print("type:", type(e))

# checkInterfaceTimer = threading.Timer(10, onCheckInterface, args=(interface,))
# checkInterfaceTimer.start()

while True:
    time.sleep(1000)

# interface.close()
# client.disconnect()