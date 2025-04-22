import requests
from dotenv import load_dotenv
import os
import streamlit as st
from Backend.translations import get_text

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
        try: 
            #send get request to check session checks for refresh token
            response = session.get(API_URL + "/auth/check-session")
            #if successful sets access token and can log user in
            if response.status_code == 200:
                st.session_state.logged_in = True
                st.session_state.user_email = response.json().get("email")
            else:
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

        st.write(response.status_code)
        st.write(response.text)

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
        response = session.post(API_URL + "/auth/login", json=payload)
        response_data = response.json()

        st.write(response.status_code)
        st.write(response.text)

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
        st.sidebar.write(f"{get_text('logged_in_as', current_language)} {st.session_state.user_email}")
        #if user logs out set session state variables to default
        if st.sidebar.button(f"{get_text('logout_button', current_language)}"):
            try:
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
                api_request("/auth/logout", "POST")
                st.switch_page("pages/Login.py")
            except requests.exceptions.RequestException as e:
                st.sidebar.error(f"{get_text('server_connection_error', current_language)}")
    #if user not logged in display login form
    elif not st.session_state.logged_in:
        st.sidebar.error(f"{get_text('login_required', current_language)}")

#refresh token function
def refresh_token():
    try:
        #send post request to get new access token
        response = session.post(API_URL + "/auth/refresh")
        #check if response is successful
        if response.status_code == 200:
            return True
        #if response is 401 no refresh token available log out user
        else:
            st.session.logged_in = False
            st.session.user_email = None
            return f"{get_text('session_expired', st.session_state.language)}"
    except:
        #if error connecting logout to be safe
        st.error(f"{get_text('server_connection_error', st.session_state.language)}")
        st.session.logged_in = False
        st.session.user_email = None
        return False
    
#wrapper function to check if user session
def api_request(endpoint, method, payload = None, files = None):
    #url for api endpoint
    url = API_URL + endpoint

    try:
        #check method and send request
        if method == "GET":
            response = session.get(url)
        elif method == "POST":
            if files:
                response = session.post(url, files=files)
            else:
                response = session.post(url, json=payload)
        elif method == "PUT":
            response = session.put(url, json=payload)
        elif method == "DELETE":
            response = session.delete(url, json=payload)
        else:
            return None

        #if 401 no access token available must refresh token
        if response.status_code == 401:
            refresh_token()
            #get a new token a send the request again
            if method == "GET":
                response = session.get(url)
            elif method == "POST":
                if files:
                    response = session.post(url, files=files)
                else:
                    response = session.post(url, json=payload)
            elif method == "PUT":
                response = session.put(url, json=payload)
            elif method == "DELETE":
                response = session.delete(url, json=payload)
            else:
                return None
            
            #if 401 no token log out user
            if response.status_code == 401:
                st.warning(f"{get_text('session_expired', st.session_state.language)}")
                st.session_state.logged_in = False
                st.session_state.user_email = None
                return None
        
        #return response data if successful
        return {
            'status_code': response.status_code,
            'data': response.json() if response.content else None
        }
    except:
        st.error(f"{get_text('server_connection_error', st.session_state.language)}")
        return None