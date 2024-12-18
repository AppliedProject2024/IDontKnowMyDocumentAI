import firebase_admin
import requests
from firebase_admin import credentials, auth
from dotenv import load_dotenv
import os

#load environment variables from .env file
load_dotenv('Keys.env')
#get api key from environment variables
FIREBASE_API_KEY = os.getenv("FIREBASE_API_KEY")

#global variable to track initialization of firebase app
firebase_initialized = False

def initFirebaseApp():
    #initialize firebase app if not already initialized
    global firebase_initialized
    if firebase_initialized:
        #create a firebase app if not already created
        cred = credentials.Certificate(r"C:\Users\keith\OneDrive\Desktop\IDKMD\firebase_credentials.json")
        #initialize firebase app
        firebase_admin.initialize_app(cred)
        #set flag to True
        firebase_initialized = True

def registerUser(email, password):
    #initialize firebase app
    initFirebaseApp()
    try:
        #create user with email and password
        user = auth.create_user(email = email, password = password)
        return f"user {user.email} created successfully"
    except Exception as e:
        return f"Error registering user: {e}"
    
def loginUser(email, password):
    #send request to firebase auth REST API
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_API_KEY}"
    #payload for POST request
    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    #send POST request
    response = requests.post(url, json=payload)
    #check if request was successful
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
    