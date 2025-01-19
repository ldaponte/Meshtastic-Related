

|Port Number|Protobuf|Message Name|Protobuf File|Definition Purpose|
|-|-|-|-|-|
|0|UNKNOWN_APP|Does not map to a message name|Does not map to a proto file|	Deprecated: Previously used for messages from external devices in an unrecognized format.|
|1|TEXT_MESSAGE_APP|MeshPacket|mesh.proto|Simple UTF-8 text messages for basic communication.|
|2|REMOTE_HARDWARE_APP|HardwareMessage|remote_hardware.proto|Reserved for built-in GPIO/example applications; see remote_hardware.proto for details.|
|3|POSITION_APP|Position|mesh.proto|Transmits GPS position updates; payload is a Position message.|
|4|NODEINFO_APP|User|mesh.proto|Protocol control packets for mesh networking; payload is a Routing message.|
|5|ROUTING_APP|Routing|mesh.proto|Handles protocol control packets for mesh networking.|
|6|ADMIN_APP|AdminMessage|admin.proto|Manages administrative control packets; payload is an AdminMessage.|
|7|TEXT_MESSAGE_COMPRESSED_APP|CompressedTextMessage|mesh.proto|Compressed text messages using Unishox2 compression.|
|8|WAYPOINT_APP|Waypoint|mesh.proto|Communicates waypoint data; payload is a Waypoint message.|
|9|AUDIO_APP|Audio|mesh.proto|Transmits audio payloads encapsulated in codec2 packets (2.4 GHz bandwidths only).|
|10|DETECTION_SENSOR_APP|DetectionSensor|mesh.proto|Similar to text messages but originating from detection sensor modules.|
|32|REPLY_APP|Reply|mesh.proto|Provides a ‘ping’ service that replies to any packet it receives; serves as a small example module.|
|33|IP_TUNNEL_APP|IPPacket|mesh.proto|Facilitates the Python IP tunnel feature; payload is an IP packet.|
|34|PAXCOUNTER_APP|Paxcounter|mesh.proto|Integrates Paxcounter library within the firmware.|
|64|SERIAL_APP|SerialData|mesh.proto|Offers a hardware serial interface for sending and receiving data over the Meshtastic network.|
|65|STORE_FORWARD_APP|StoreForward|storeforward.proto|Work in progress: Implements store and forward functionality.|
|66|RANGE_TEST_APP|RangeTest|mesh.proto|Optional port for messages related to the range test module.|
|67|TELEMETRY_APP|Telemetry|mesh.proto|Provides a format to send and receive telemetry data within the Meshtastic network.|
|68|ZPS_APP|ZPS|mesh.proto|Experimental tools for estimating node position without GPS.|
|69|SIMULATOR_APP|Simulator|mesh.proto|Allows multiple instances of Linux native applications to communicate as if using their LoRa chip.|
|70|TRACEROUTE_APP|Traceroute|mesh.proto|Offers traceroute functionality to display the route a packet takes towards a specific destination within the mesh.|
|71|NEIGHBORINFO_APP|NeighborInfo|mesh.proto|Aggregates edge information by sending out a list of each node’s neighbors.|
|72|ATAK_PLUGIN|AtakPlugin|mesh.proto|Port number for payloads from the official Meshtastic ATAK plugin.|
|73|MAP_REPORT_APP|MapReport|mesh.proto|Provides unencrypted information about a node for consumption by a map via MQTT.|
|74|POWERSTRESS_APP|PowerStress|mesh.proto|Supports power stress-based monitoring for automated power consumption testing.|
|256|PRIVATE_APP|PrivateApp|mesh.proto|Reserved for private applications; use port numbers >= 256 for unregistered private apps.|
|257|ATAK_FORWARDER|AtakForwarder|mesh.proto|ATAK Forwarder Module; see atak-forwarder.|
|511|MAX|MAX|mesh.proto|Currently, port numbers are limited to no higher than this value.|
