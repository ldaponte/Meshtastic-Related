// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

// The current database to use.
use("test");

# mongosh query examples

// links
https://developerslogblog.wordpress.com/2019/10/15/mongodb-how-to-filter-by-multiple-fields/

// connecting to mongodb
mongosh mongodb://<database user>:<database password>@<hostname:27017/<database name>

// search for dates
db.getCollection('meshtastic-bcp2').find({receivedDate: {$gte:"2025-02-21T01:22:30.000Z"}})

// find with filter and show only select fields in the output
db.getCollection('meshtastic-bcp2').find({'payload.packet.decoded.portnum': 'TEXT_MESSAGE_APP'},{'payload.packet.decoded.payload':1,'payload.channelId':1, '_id':0})

// simple find with nested object
db.getCollection('meshtastic-bcp2').find({'payload.packet.decoded.portnum': 'TEXT_MESSAGE_APP'});

// distinct
db.getCollection('meshtastic-bcp2').distinct('payload.packet.decoded.portnum')

// find with regular expression
db.getCollection('meshtastic-bcp2').find({'payload.packet.decoded.payload': /Anyone??/});

db.getCollection('meshtastic-bcp2').find({'payload.packet.decoded.wantResponse': true}).limit(3);

db.getCollection('meshtastic-bcp2').find({'payload.packet.decoded.requestId': { $ne: 0 }}).limit(3);

db.getCollection('meshtastic-bcp2').find({'payload.packet.viaMqtt': true}).limit(3);

db.getCollection('meshtastic-bcp2').find({'payload.packet.priority': { $ne: 'UNSET'}}).limit(3);

db.getCollection('meshtastic-bcp2').find({'payload.packet.wantAck': true}).limit(3);


db.getCollection('meshtastic-bcp2').aggregate([
    {
      $lookup: {
        from: "movies",
        localField: "movie_id",
        foreignField: "_id",
        as: "movie_details",
      },
    },
    {
      $limit: 1
    }
  ])


db.getCollection('meshtastic-bcp2').find({'payload.packet.from': 1127935220, 'payload.packet.decoded.portnum': 'NODEINFO_APP'}).limit(1)

db.getCollection('meshtastic-bcp2').find({'payload.packet.from': 1127935220, 'payload.packet.decoded.portnum': 'TEXT_MESSAGE_APP'})

db.getCollection('meshtastic-bcp2').find({'payload.packet.from': 4294967295})

//----
db.getCollection('meshtastic-bcp2').find({'payload.packet.decoded.payload': /Copy W Seattle/});


//----

// delete everything - empty filter
db.getCollection('meshtastic-bcp2').deleteMany({});

// switch to collection
use("test");

// multiple criteria
db.getCollection('meshtastic-bcp2').find({
    'payload.packet.decoded.portnum': 'NODEINFO_APP',
    'receivedDate': {$gte:"2025-02-17T06:50:00.000Z"}
})

// random queries
db.getCollection('meshtastic-bcp2').find({'payload.packet.decoded.payload.shortName': 'BCP3'})

db.getCollection('meshtastic-bcp2').find({'payload.packet.decoded.portnum': 'NODEINFO_APP', receivedDate: {$gte:"2025-02-21T04:08:27.422Z"}})

db.getCollection('meshtastic-bcp2').find({'payload.packet.from': 579358746},{'payload.packet.decoded.portnum':1,'payload.channelId':1, '_id':0})

db.getCollection('meshtastic-bcp2').find({'payload.packet.decoded.portnum': 'TEXT_MESSAGE_APP'},{'payload.packet.decoded.payload':1,'payload.channelId':1, '_id':0})

db.getCollection('meshtastic-bcp2').find({'payload.packet.decoded.payload.shortName': /BCP/},{'payload.packet.decoded.payload.shortName':1, 'payload.packet.decoded.portnum':1, 'payload.packet.decoded.payload.longName':1, 'payload.packet.from':1})

db.getCollection('meshtastic-bcp2').find({'payload.packet.from': 579358746},{'payload.packet.decoded.payload.shortName':1, 'payload.packet.decoded.portnum':1, 'payload.packet.decoded.payload.longName':1, 'payload.packet.from':1})

db.getCollection('meshtastic-bcp2').find({'payload.packet.from': 579358746, 'payload.packet.decoded.portnum': 'NODEINFO_APP'}).limit(1)

db.getCollection('meshtastic-bcp2').find({'payload.packet.decoded.portnum': 'TEXT_MESSAGE_APP', 'payload.packet.to': 579358746})

db.getCollection('meshtastic-bcp2').find({'payload.packet.to': 579358746})

db.getCollection('meshtastic-bcp2').find({'payload.packet.from': 579358746}).forEach(
    function (meshnode) {
        newBook.category = db.categories.findOne( { "_id": newBook.category } );
        newBook.lendings = db.lendings.find( { "book": newBook._id  } ).toArray();
        newBook.authors = db.authors.find( { "_id": { $in: newBook.authors }  } ).toArray();
        db.booksReloaded.insert(newBook);
    }
);
