from pyrebase import *

firebaseConfig = {
    'apiKey': "AIzaSyDQZ04wURdN2E3N_cMRO06M4CQ4DEnPvhk",
    'authDomain': "attendance-f373c.firebaseapp.com",
    'databaseURL': "https://attendance-f373c-default-rtdb.firebaseio.com",
    'projectId': "attendance-f373c",
    'storageBucket': "attendance-f373c.appspot.com",
    'messagingSenderId': "115560806458",
    'appId': "1:115560806458:web:b16b36e6434c3704da5d03",
    'measurementId': "G-1505CH1RN4"
}

db = pyrebase.initialize_app(firebaseConfig)
connection = None


def getDb():
    global connection
    if connection is None:
        connection = db.database()
        return connection
    else:
        return connection
