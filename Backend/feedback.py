import requests
import streamlit as st
from dotenv import load_dotenv
from Backend.UserAuth import api_request
from Backend.translations import get_text

#send feedback to server
def send_feedback(feedback_type, feedback):
    try:   
        #send post request to submit feedback include type and feedback 
        response = api_request("/feedback/submit", "POST", {"feedback_type": feedback_type, "feedback": feedback})
        return response
    except requests.exceptions.RequestException as e:
        st.error(f"{get_text('server_connection_error', st.session_state.language)}")

