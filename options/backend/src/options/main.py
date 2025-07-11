
import os
import json 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from options.auth import router as auth_router

def cli():
    """Command line interface for the Options backend."""
    key_json = os.environ.get("FIREBASE_KEY_JSON")
    if key_json:
        try:
            key_data = json.loads(key_json)
            print(key_data)
            print("Firebase key loaded successfully.")
        except json.JSONDecodeError:
            print("Invalid JSON format for FIREBASE_KEY_JSON.")
    else:
        print("FIREBASE_KEY_JSON environment variable is not set.")
        
    print("Hello World")



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI backend!"}