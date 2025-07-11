from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from firebase_admin import auth, credentials, initialize_app

# Initialize Firebase Admin SDK
cred = credentials.Certificate("path/to/your/firebase-adminsdk.json")
initialize_app(cred)

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/login/google")
async def google_login(token: str):
    try:
        # Verify the Google token
        decoded_token = auth.verify_id_token(token)
        uid = decoded_token['uid']
        
        # Here you can implement your logic to create or get the user in your database
        # For example, you might want to check if the user exists in Firestore and create them if not
        
        return {"message": "User logged in successfully", "uid": uid}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    try:
        # Verify the token
        decoded_token = auth.verify_id_token(token)
        return {"uid": decoded_token['uid']}
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")