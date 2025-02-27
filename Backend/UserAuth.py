import requests
from dotenv import load_dotenv
import os
import streamlit as st

#load environment variables from .env file
load_dotenv('Keys.env')
#backend api url from environment variables
API_URL = os.getenv("API_URL")

session = requests.Session()

#initialise session state
def intialiseSession():
    #initialise session state variables
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "user_id" not in st.session_state:
        st.session_state.user_id = None
    if "user_email" not in st.session_state:
        st.session_state.user_email = None

    #check if user is logged in
    if not st.session_state.logged_in:
        try: 
            #send get request to check session checks for refresh token
            response = session.get(API_URL + "/check-session")
            #if successful sets access token and can log user in
            if response.status_code == 200:
                st.session_state.logged_in = True
                st.session_state.user_email = response.json().get("email")
        except requests.exceptions.RequestException as e:
            st.error("Error connecting to server.")
            return None


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
        #send POST request to login
        response = session.post(API_URL + "/login", json=payload)
        response_data = response.json()

        #if successful login
        if response.status_code == 200:
            #set session state variables
            st.session_state["logged_in"] = True
            st.session_state["user_email"] = email
            return response_data
        #if 403 email not verified
        elif response.status_code == 403 and "Email not verified" in response_data.get("error", ""):
            return "unverified"
        else:
            st.error(response_data.get("error", "Login failed."))
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

#refresh token function
def refresh_token():
    try:
        #send post request to get new access token
        response = session.post(API_URL + "/refresh")
        #check if response is successful
        if response.status_code == 200:
            return True
        #if response is 401 no refresh token available log out user
        else:
            st.session.logged_in = False
            st.session.user_email = None
            return response.json().get("error", "Token refresh failed.")
    except:
        #if error connecting logout to be safe
        st.error(f"Server error.")
        st.session.logged_in = False
        st.session.user_email = None
        return False
    
#wrapper function to check if user session
def api_request(endpoint, method, payload = None):
    #url for api endpoint
    url = API_URL + endpoint

    try:
        #check method and send request
        if method == "GET":
            response = session.get(url)
        elif method == "POST":
            response = session.post(url, json=payload)
        elif method == "PUT":
            response = session.put(url, json=payload)
        elif method == "DELETE":
            response = session.delete(url)
        else:
            return None

        #if 401 no access token available must refresh token
        if response.status_code == 401:
            refresh_token()
            #get a new token a send the request again
            if method == "GET":
                response = session.get(url)
            elif method == "POST":
                 response = session.post(url, json=payload)
            elif method == "PUT":
                response = session.put(url, json=payload)
            elif method == "DELETE":
                response = session.delete(url)
            else:
                return None
        #if 401 no token log out user (backup to refresh method logout)
        if response.status_code == 401:
            st.warning("Your session has expired. Please login again.")
            st.session_state.logged_in = False
            st.session_state.user_email = None
            return None
        
        #return response data if successful
        return response.json()
    except:
        st.error("Error connecting to server.")
        return None

def test():
    try:
        response = api_request("/test", "GET")
        return response
    except requests.exceptions.RequestException as e:
        st.error("Error connecting to server. here")
        return None