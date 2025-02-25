import streamlit as st
from Backend.UserAuth import loginUser, intialiseSession, sidebarAuth

#initialise session state
intialiseSession()
sidebarAuth()

#check if user is already logged in
if st.session_state.get("logged_in", False):
    st.write("You are already logged in. Logging in with a new account will log you out!")

#login inputs
st.title("Login")
email = st.text_input("Email", key="login_email")
password = st.text_input("Password", type="password", key="login_password")

#login Button
if st.button("Login"):
    #call loginUser function
    data = loginUser(email, password)
    
    #check the response
    if data == "unverified":
        st.error("Email not verified. Please check your email for a verification link.")
    elif data:
        #if success move to main page
        st.success("Login Successful!")
        st.switch_page("Main.py")
    else:
        st.error("Login Failed. Please ensure your email and password are correct.")

#register Page Button
if st.button("Register", key="register_page"):
    st.switch_page("Pages/Register.py")
