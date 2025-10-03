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
account_transaction = fs_db.collection("transaction")
account_type = fs_db.collection("types")
account_un_categorized = fs_db.collection("un_categorized")
uncatego=account_un_categorized.document("uncategorized")
catego=account_un_categorized.document("categorized")
if not uncatego.get().exists:
    uncatego.set({})  # empty document

# Create "categorized" document
catego = account_un_categorized.document("categorized")
if not catego.get().exists:
    catego.set({})

# Function for Realtime DB
def get_db_ref(node_name):
    return db.reference(node_name)