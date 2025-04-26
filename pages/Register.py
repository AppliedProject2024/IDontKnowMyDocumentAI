import streamlit as st
from Backend.UserAuth import registerUser, sidebarAuth, intialiseSession
from Backend.translations import get_text

#initialise session
intialiseSession()
sidebarAuth()

#register Page
st.title(f"{get_text('app_title', st.session_state.language)}")
st.header(f"{get_text('register_header',st.session_state.language)}")
st.text(f"{get_text('institutional_email_warning', st.session_state.language)}")

#input fields for email and password
email = st.text_input(f"{get_text('email_label',st.session_state.language)}", key="register_email")
password = st.text_input(f"{get_text('password_label',st.session_state.language)}", type="password", key="register_password")

#register button
if st.button(f"{get_text('register_button',st.session_state.language)}", key="register_acc"):
    #call registerUser function
    message = registerUser(email, password)
