import firebase_admin
import requests
from firebase_admin import credentials, auth
from dotenv import load_dotenv
import os
import streamlit as st
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from streamlit_js_eval import streamlit_js_eval


#load environment variables from .env file
load_dotenv('Keys.env')
#get api key from environment variables
FIREBASE_API_KEY = os.getenv("FIREBASE_API_KEY")
#backend api url from environment variables
API_URL = os.getenv("API_URL")

#initialize session state
def intialiseSession():
    #initialize session state variables
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "user_id" not in st.session_state:
        st.session_state.user_id = None
    if "user_email" not in st.session_state:
        st.session_state.user_email = None

#register user with email and password
def registerUser(email, password):
    #check if email and password are empty
    if not email or not password:
        return "Please enter a valid email and password."
    
    #create payload for registration
    payload = {"email": email, "password": password}
    
    try:
        #send post request to register user
        response = requests.post(API_URL + "/register", json=payload)
        #get response data
        response_data = response.json()

        #check if registration was successful
        if response.status_code == 200:
            return "Registration successful! Please check your email for a verification link."

        else:
            return response_data.get("error", "Registration failed. Please try again.")

    except requests.exceptions.RequestException as e:
        st.error("Error connecting to server.")
        return "Registration failed. Please try again."

#login user with email and password   
def loginUser(email, password):
    #check if email and password are empty
    if not email or not password:
        return None 
    
    #create payload for login
    payload = {"email": email, "password": password}
    
    try:
        #send post request to login user
        response = requests.post(API_URL + "/login", json=payload)
        response_data = response.json()

        #check if login was successful
        if response.status_code == 200:
            #set session state variables
            st.session_state["logged_in"] = True
            st.session_state["idToken"] = response_data["idToken"]
            st.session_state["user_email"] = email
            return response_data  #successful login

        elif response.status_code == 403 and "Email not verified" in response_data.get("error", ""):
            return "unverified"

        else:
            return None

    except requests.exceptions.RequestException as e:
        st.error("Error connecting to server.")
        return None
    
#sidebar authentication display
def sidebarAuth():
    #if user logged in display user email and logout button
    if st.session_state.logged_in:
        st.sidebar.write(f"Logged in as: {st.session_state.user_email}")
        #if user logs out set session state variables to default
        if st.sidebar.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.user_email = None
            #redirect to login page
            st.switch_page("Pages/Login.py")
    elif not st.session_state.logged_in:
        st.sidebar.error("Please login to access the application")