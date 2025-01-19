# Meshtastic-Related
Project files related to my personal Meshtastic tinkering

## What's going on here?
This repo will be used to collect all the project files related to capturing Meshtastic protobufs from a node using MQTT, decoding those protobufs, and storing them in mongodb and Neo4J.

I've been using a SQL server to collect the packets, shred them into a schema, and query them just to get an idea of what I'm able to hear in my area and learn more about Meshtastic.  I have been using the JSON formatted messages sent by the node to my MQTT server but realized the JSON format was missing details so I decided to take a new approach and started decoding the protobufs to see everything.  Instead of storing this in a bespoke SQL schema I decided to switch to MongoDB since the schema is not fixed and it is capable of storing any random JSON with the ability to query it.

The next step I'll take is to store message the relationships in Neo4J so that I can represent them graphically and query on those relationships.

The design is as follows:

Configure an ESP32 based Meshtastic node by enabling MQTT and enabling MQTT uplink on all the channels I want to monitor.  I've installed a local copy of Mosquitto MQTT broker and I've configured the ESP32 to send its MQTT messages there.  I'm using Node-Red to connect to that MQTT broker, decode the ServiceEnvelope protobufs, then, based on the port number of the message, I decode the payload and store the entire decoded message in MongoDB.  The next step will be to create nodes and relationships in Neo4J based on to/from ids and channelIds as well as trace route information.

Why am I doing this?  I'm not sure :)
