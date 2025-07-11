from firebase_admin import firestore, initialize_app

# Initialize Firebase Admin SDK
initialize_app()

# Get a reference to the Firestore database
db = firestore.client()

def add_document(collection_name, document_data):
    """Add a document to a Firestore collection."""
    doc_ref = db.collection(collection_name).add(document_data)
    return doc_ref.id

def get_document(collection_name, document_id):
    """Retrieve a document from a Firestore collection."""
    doc_ref = db.collection(collection_name).document(document_id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return None

def update_document(collection_name, document_id, updated_data):
    """Update a document in a Firestore collection."""
    doc_ref = db.collection(collection_name).document(document_id)
    doc_ref.update(updated_data)

def delete_document(collection_name, document_id):
    """Delete a document from a Firestore collection."""
    doc_ref = db.collection(collection_name).document(document_id)
    doc_ref.delete()