import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials.
cred = credentials.Certificate('shoestore-d1c3e-8dc92c570146.json')

firebase_admin.initialize_app(cred)
db = firestore.client()

product ={
    "collection": "Men",
    "item": "https://images.pexels.com/photos/786003/pexels-photo-786003.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500", # main product Image link
    "price": 45.57,
    "title": "Mens Sports Shoes",
    "id": "bbl",
    "availableColors": [
      {
        "color": "#000", # hex colors
        "imgs": [
          {
            "img": "https://images.pexels.com/photos/786003/pexels-photo-786003.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500", #img link
          },

          {
            "img": "https://images.pexels.com/photos/786003/pexels-photo-786003.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500", #img link
          },
        ],
      },
    ],
    "availableSizes": [
      {
        "size": 37,
      },

      {
        "size": 40,
      },
    ],
}

db.collection("products").document(product["id"]).set(product)