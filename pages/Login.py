import streamlit as st
from Backend.UserAuth import loginUser, intialiseSession, sidebarAuth
from Backend.translations import get_text
#initialise session state
intialiseSession()
sidebarAuth()

#check if user is already logged in
if st.session_state.get("logged_in", False):
    st.write(f"{get_text('already_logged_in',st.session_state.language)}")
#title and header
st.title(f"{get_text('app_title', st.session_state.language)}")
st.header(f"{get_text('login_header',st.session_state.language)}")
#login inputs
email = st.text_input(f"{get_text('email_label',st.session_state.language)}", key="login_email")
password = st.text_input(f"{get_text('password_label',st.session_state.language)}", type="password", key="login_password")
email = email.lower()
#login Button
if st.button(f"{get_text('login_button',st.session_state.language)}"):
    #call loginUser function
    data = loginUser(email, password)
    
    #check the response
    if data == "unverified":
        st.error(f"{get_text('email_not_verified',st.session_state.language)}")
    elif data:
        #if success move to main page
        st.success(f"{get_text('login_success',st.session_state.language)}")
        st.switch_page("Main.py")
    else:
        st.error(f"{get_text('login_failed',st.session_state.language)}")

#register Page Button
if st.button(f"{get_text('register_button',st.session_state.language)}", key="register_page"):
    st.switch_page("pages/Register.py")
