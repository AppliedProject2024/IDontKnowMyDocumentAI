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
import time


#load environment variables from .env file
load_dotenv('Keys.env')
#get api key from environment variables
FIREBASE_API_KEY = os.getenv("FIREBASE_API_KEY")

#SMTP credentials
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT"))
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

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
    if "user_email" not in st.session_state:
        st.session_state.user_email = None  # Ensure email variable exists

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

        #send email
        email_status = sendVerificationEmail(email, link)

        return f"User {email} registered successfully! Please check your email for verification."

    except Exception as e:
        return f"Error registering user: {str(e)}"
    
#send verification email
def sendVerificationEmail(email, verification_link):
    try:
        #set up emal message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USER
        msg['To'] = email
        msg['Subject'] = "Email Verification - IDontKnowMyDocument AI"

        #body
        body = f"""
        <html>
        <body>
            <p>Hello,</p>
            <p>Thank you for signing up to IDontKnowMyDocument AI!</p>
            <p>Please find below a link to verify your email address:</p>
            <a href="{verification_link}">Verify Email</a>
            <p>Thank you! We hope you enjoy using our Application!</p>
        </body>
        </html>
        """
        msg.attach(MIMEText(body, 'html'))

        #connect to SMTP server
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()#secure connection
        server.login(EMAIL_USER, EMAIL_PASS)#login to email
        server.sendmail(EMAIL_USER, email, msg.as_string())#send email
        server.quit()#close connection

        return "Verification email sent successfully!"
    except Exception as e:
        return f"Error sending verification email: {str(e)}"

#login user with email and password   
def loginUser(email, password):
    initFirebaseApp()

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
        
        st.session_state.logged_in = True
        st.session_state.user_email = email
        streamlit_js_eval(js_expressions=f"localStorage.setItem('user_email', '{email}');")
        time.sleep(1) #wait 1 second to ensure local storage is set
        st.switch_page("Main.py")
    else:
        return None
    
#sidebar authentication display
def sidebarAuth():
    if st.session_state.logged_in:
        st.sidebar.write(f"Logged in as: {st.session_state.user_email}")

        if st.sidebar.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.user_email = None
            streamlit_js_eval(js_expressions="localStorage.removeItem('user_email')")
            st.switch_page("Pages/Login.py")
    elif not st.session_state.logged_in:
        st.sidebar.error("Please login to access the application")

#retrieve user details from local storage
def retrieveUser():
    #check if retrieval has already been attempted
    if "local_storage_retrieved" not in st.session_state:
        st.session_state.local_storage_retrieved = False

    if not st.session_state.local_storage_retrieved:
        user_email = streamlit_js_eval(js_expressions="localStorage.getItem('user_email')")
        print(f"retrieved email: {user_email}")

        if user_email:
            st.session_state.user_email = user_email
            st.session_state.logged_in = True
            st.session_state.local_storage_retrieved = True  #mark retrieval as done
        else:
            time.sleep(0.5)  #wait for 0.5 seconds to retrieve local storage