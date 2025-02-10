import firebase_admin
import requests
from firebase_admin import credentials, auth
from dotenv import load_dotenv
import os
import streamlit as st

#load environment variables from .env file
load_dotenv('Keys.env')
#get api key from environment variables
FIREBASE_API_KEY = os.getenv("FIREBASE_API_KEY")

#global variable to track initialization of firebase app
firebase_initialized = False

#initialize firebase app
def initFirebaseApp():
    #initialize firebase app if not already initialized
    if not firebase_admin._apps:
        #create a firebase app if not already created
        cred = credentials.Certificate(r".\firebase_credentials.json")
        #initialize firebase app
        firebase_admin.initialize_app(cred)
        #set flag to True
        firebase_initialized = True

#initialize session state
def intialiseSession():
    #initialize session state variables
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "user_id" not in st.session_state:
        st.session_state.user_id = None

#register user with email and password
def registerUser(email, password):
    #initialize firebase app
    initFirebaseApp()
    try:
        #create user with email and password
        user = auth.create_user(email = email, password = password)
        
        #send verification email
        auth.update_user(user.uid, email_verified=False)
        link = auth.generate_email_verification_link(email)

        #send email verification link(temporary just printing)
        print(f"Verification link: {link}") #temporary just printing

        return f"User {email} registered successfully! Please check your email for verification."

    except Exception as e:
        return f"Error registering user: {str(e)}"

#login user with email and password   
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

        try:
            #get user details to check verification status
            user = auth.get_user_by_email(email)

            #check if email is verified
            if not user.email_verified:
                return "unverified"
        except Exception as e:
            return f"Error getting user details: {str(e)}"
        
        return data #sucessful login return data
    else:
        return None
    