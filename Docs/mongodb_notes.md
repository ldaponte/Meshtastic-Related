# mongosh queries

## connecting to mongodb
mongosh mongodb://<database user>:<database password>@<hostname:27017/<database name>

## search for dates
db.getCollection('meshtastic-bcp2').find({receivedDate: {$gte:"2025-01-23T01:20:27.412Z"}})

## find with filter and show only select fields in the output
db.getCollection('meshtastic-bcp2').find({'payload.packet.decoded.portnum': 'TEXT_MESSAGE_APP'},{'payload.packet.decoded.payload':1,'payload.channelId':1, '_id':0})

## simple find with nested object
db.getCollection('meshtastic-bcp2').find({'payload.packet.decoded.portnum': 'TEXT_MESSAGE_APP'});

## distinct
db.getCollection('meshtastic-bcp2').distinct('payload.packet.decoded.portnum')

## find with regular expression
db.getCollection('meshtastic-bcp2').find({'payload.packet.decoded.payload': /there/});

## delete everything - empty filter
db.getCollection('meshtastic-bcp2').deleteMany({});

## switch to collection
use meshtastic-bcp2

## show all collections
show collections

