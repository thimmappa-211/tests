try:

   db.products.insertMany( [
      { _id: 10, item: "large box", qty: 20 },
      { _id: 11, item: "small box", qty: 55 },
      { _id: 12, item: "medium box", qty: 30 } ] )

except Exception as e:
    print(e)

'''
#to get latest message 

db.getCollection('deviceTrackerHistory').aggregate([
   {
     $match:{clientId:"12"}
   },
   {
     $project:
      {
         deviceId:1,
         recent: { $arrayElemAt: [ "$history", -1 ] }
      }
   }
])
'''



