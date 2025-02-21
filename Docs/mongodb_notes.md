# mongosh query examples

## links
https://developerslogblog.wordpress.com/2019/10/15/mongodb-how-to-filter-by-multiple-fields/

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

## multiple criteria
db.getCollection('meshtastic-bcp2').find({
    'payload.packet.decoded.portnum': 'NODEINFO_APP',
    'receivedDate': {$gte:"2025-02-17T06:50:00.000Z"}
})

## random queries
db.getCollection('meshtastic-bcp2').find({'payload.packet.decoded.payload.shortName': 'BCP3'})
db.getCollection('meshtastic-bcp2').find({'payload.packet.decoded.portnum': 'NODEINFO_APP', receivedDate: {$gte:"2025-02-21T04:08:27.422Z"}})

db.getCollection('meshtastic-bcp2').find({'payload.packet.from': 579358746},{'payload.packet.decoded.portnum':1,'payload.channelId':1, '_id':0})

db.getCollection('meshtastic-bcp2').find({'payload.packet.decoded.portnum': 'TEXT_MESSAGE_APP'},{'payload.packet.decoded.payload':1,'payload.channelId':1, '_id':0})

db.getCollection('meshtastic-bcp2').find({'payload.packet.decoded.payload.shortName': /BCP/},{'payload.packet.decoded.payload.shortName':1, 'payload.packet.decoded.portnum':1, 'payload.packet.decoded.payload.longName':1, 'payload.packet.from':1})

db.getCollection('meshtastic-bcp2').find({'payload.packet.from': 579358746},{'payload.packet.decoded.payload.shortName':1, 'payload.packet.decoded.portnum':1, 'payload.packet.decoded.payload.longName':1, 'payload.packet.from':1})

