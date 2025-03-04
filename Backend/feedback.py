import requests
import streamlit as st
from dotenv import load_dotenv
import os
from Backend.UserAuth import api_request

#get api url from environment variables
API_URL_TEMPLATE = os.getenv("API_URL")
#feedback api url
API_URL = API_URL_TEMPLATE + "/feedback"

#send feedback to server
def send_feedback(feedback_type, feedback):
    try:   
        #send post request to submit feedback include type and feedback 
        response = api_request("/feedback/submit", "POST", {"feedback_type": feedback_type, "feedback": feedback})
        return response
    except requests.exceptions.RequestException as e:
        st.error("Error connecting to server.")

#retrieve feedback from server (test)
def get_feedback():
    response = api_request("/feedback/get", "GET")
    return response

