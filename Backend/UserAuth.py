import requests
from dotenv import load_dotenv
import os
import streamlit as st
from Backend.translations import get_text

#load environment variables from .env file
load_dotenv('Keys.env')
#backend api url from environment variables
API_URL = os.getenv("API_URL")

#initialise session state
def intialiseSession():
    #initialise session state variables
    if "refresh_token" not in st.session_state:
        st.session_state.refresh_token = None
    if "access_token" not in st.session_state:
        st.session_state.access_token = None
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "user_id" not in st.session_state:
        st.session_state.user_id = None
    if "user_email" not in st.session_state:
        st.session_state.user_email = None
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "context_history" not in st.session_state:
        st.session_state.context_history = []
    if "summary" not in st.session_state:
        st.session_state.summary = None
    if 'mcq_questions' not in st.session_state:
        st.session_state.mcq_questions = []
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'user_answers' not in st.session_state:
        st.session_state.user_answers = {}
    if 'show_result' not in st.session_state:
        st.session_state.show_result = False
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'last_question_answered' not in st.session_state:
        st.session_state.last_question_answered = False
    if 'language' not in st.session_state:
        st.session_state.language = "English"

    #check if user is logged in
    if not st.session_state.logged_in:
        #check if access token is available
        if st.session_state.access_token:
            try: 
                #send get request to check session checks for refresh token
                response = api_request( "/auth/check-session", "GET")
                #if successful sets access token and can log user in
                if response and response.get("status_code") == 200:
                    st.session_state.logged_in = True
                    st.session_state.user_email = response.json().get("email")
                else:
                    #if 401 no access token available must refresh token
                    if st.session_state.refresh_token:
                        refresh = refresh_token()
                        if not refresh:
                            st.session_state.logged_in = False
                            st.session_state.user_email = None
                            st.session_state.access_token = None
                            st.session_state.refresh_token = None
                            return (f"{get_text('session_expired', st.session_state.language)}")
                    #if no refresh token available log out user
                    else:
                        st.session_state.logged_in = False
                        st.session_state.user_email = None
                        st.session_state.access_token = None
                        st.session_state.refresh_token = None
                    return (f"{get_text('session_expired', st.session_state.language)}")
            except requests.exceptions.RequestException as e:
                st.error(f"{get_text('server_error', st.session_state.language)}")
                return None


#register user with email and password
def registerUser(email, password):
    #check if email and password are empty
    if not email or not password:
        return f"{get_text('enter_valid_credentials', st.session_state.language)}"
    
    #create payload for registration
    payload = {"email": email, "password": password}
    
    try:
        #send post request to register user
        response = requests.post(API_URL + "/auth/register", json=payload)
        #get response data
        response_data = response.json()

        #check if registration was successful
        if response.status_code == 200:
            return st.success(f"{get_text('registration_success', st.session_state.language)}")

        else:
            return st.error(f"{get_text('registration_failed', st.session_state.language)}")

    except requests.exceptions.RequestException as e:
        st.error(f"{get_text('server_connection_error', st.session_state.language)}")
        return st.error(f"{get_text('registration_failed', st.session_state.language)}")

#login user with email and password   
def loginUser(email, password):
    #check if email and password are empty
    if not email or not password:
        return None
    #create payload for login
    payload = {"email": email, "password": password}
    
    try:
        #send POST request to login
        response = requests.post(API_URL + "/auth/login", json=payload)
        response_data = response.json()

        #if successful login
        if response.status_code == 200:
            #set session state variables
            st.session_state["logged_in"] = True
            st.session_state["user_email"] = email
            st.session_state["access_token"] = response_data.get("access_token")
            st.session_state["refresh_token"] = response_data.get("refresh_token")
            return response_data
        #if 403 email not verified
        elif response.status_code == 403 and "Email not verified" in response_data.get("error", ""):
            return "unverified"
        else:
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"{get_text('server_connection_error', st.session_state.language)}")
        return None
    
#sidebar authentication display
def sidebarAuth():
    #if user logged in display user email and logout button
    current_language = st.session_state.get("language", "English")
    previous_language = st.session_state.get("language", "English")

    language = st.sidebar.selectbox(
        get_text("language_label", current_language),
        [
            "English",
            "Spanish", 
            "French", 
            "Portuguese",
            "German"
        ],
        index=[
            "English",
            "Spanish", 
            "French", 
            "Portuguese",
            "German"
        ].index(previous_language),
        key="language_selector"
    )

    if language != previous_language:
        st.session_state.language = language
        st.rerun()

    if st.session_state.logged_in:

        #display user email in sidebar
        st.sidebar.text(f"{get_text('logged_in_as', current_language)} {st.session_state.user_email}")
        #if user logs out set session state variables to default
        if st.sidebar.button(f"{get_text('logout_button', current_language)}"):
            try:
                st.session_state.access_token = None
                st.session_state.refresh_token = None
                st.session_state.logged_in = False
                st.session_state.user_email = None
                st.session_state.messages = []
                st.session_state.summary = None
                st.session_state.context_history = []
                st.session_state.mcq_questions = []
                st.session_state.current_question = 0
                st.session_state.user_answers = {}
                st.session_state.show_result = False
                st.session_state.score = 0
                st.session_state.last_question_answered = False
                st.session_state.language = "English"
                #redirect to login page
                st.switch_page("pages/Login.py")
            except requests.exceptions.RequestException as e:
                st.sidebar.error(f"{get_text('server_connection_error', current_language)}")
    #if user not logged in display login form
    elif not st.session_state.logged_in:
        st.sidebar.error(f"{get_text('login_required', current_language)}")

#refresh token function
def refresh_token():
    try:
        headers = {}
        #check if refresh token is available
        if st.session_state.refresh_token:
            headers["Authorization"] = f"Bearer {st.session_state.refresh_token}"
            
            #send post request to refresh token
            response = requests.post(API_URL + "/auth/refresh", headers=headers)
            
            #check if refresh token was successful
            if response.status_code == 200:
                #set access token and refresh token in session state
                response_data = response.json()
                st.session_state.access_token = response_data.get("access_token")
                return True
            else:
                #if refresh token fails set session state variables to default
                st.session_state.logged_in = False
                st.session_state.user_email = None
                st.session_state.access_token = None
                st.session_state.refresh_token = None
                return False
    except:
        st.error(f"{get_text('server_connection_error', st.session_state.language)}")
        st.session_state.logged_in = False
        st.session_state.user_email = None
        st.session_state.access_token = None
        st.session_state.refresh_token = None
        return False
    
#wrapper function to check if user session
def api_request(endpoint, method, payload = None, files = None):
    #url for api endpoint
    url = API_URL + endpoint

    try:
        #set headers for request
        headers = {}
        #check if access token is available
        if st.session_state.access_token:
            headers["Authorization"] = f"Bearer {st.session_state.access_token}"
        
        #check method and send request
        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            if files:
                response = requests.post(url, files=files, headers=headers)
            else:
                response = requests.post(url, json=payload, headers=headers)
        elif method == "PUT":
            response = requests.put(url, json=payload, headers=headers)
        elif method == "DELETE":
            response = requests.delete(url, json=payload, headers=headers)
        else:
            return None

        #if 401 no access token available must refresh token
        if response.status_code == 401:
            refresh_token()
            #set headers for request again
            headers["Authorization"] = f"Bearer {st.session_state.access_token}"
            #get a new token a send the request again
            if method == "GET":
                response = requests.get(url, headers=headers)
            elif method == "POST":
                if files:
                    response = requests.post(url, files=files, headers=headers)
                else:
                    response = requests.post(url, json=payload, headers=headers)
            elif method == "PUT":
                response = requests.put(url, json=payload, headers=headers)
            elif method == "DELETE":
                response = requests.delete(url, json=payload, headers=headers)
            else:
                return None
            
            #if 401 no token log out user
            if response.status_code == 401:
                st.warning(f"{get_text('session_expired', st.session_state.language)}")
                st.session_state.logged_in = False
                st.session_state.user_email = None
                st.session_state.access_token = None
                st.session_state.refresh_token = None
                return None
        
        #return response data if successful
        return {
            'status_code': response.status_code,
            'data': response.json() if response.content else None
        }
    except:
        st.error(f"{get_text('server_connection_error', st.session_state.language)}")
        return None