# firebase_config.py
import firebase_admin
from firebase_admin import credentials, firestore, db

cred = credentials.Certificate('lib/firebase_key.json')

# Initialize only once
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://expensetracker-8dff4-default-rtdb.asia-southeast1.firebasedatabase.app'
    })

# Firestore references
fs_db = firestore.client()
account_doc = fs_db.collection("transaction")
account_type = fs_db.collection("types")
account_uncategorized = fs_db.collection("uncategorized")

# Function for Realtime DB
def get_db_ref(node_name):
    return db.reference(node_name)