import streamlit as st
from Backend.UserAuth import loginUser, intialiseSession, retrieveUser, sidebarAuth
from streamlit_js_eval import streamlit_js_eval

#initialise session
intialiseSession()
retrieveUser()
sidebarAuth()

if st.session_state.logged_in:
    st.write("You are already logged in, Logging in with a new account will log you out!")

#login Page
st.title("Login")
#input fields for email and password
email = st.text_input("Email", key="login_email")
password = st.text_input("Password", type="password", key="login_password")

#login button
if st.button("Login"):
    #call loginUser function and store the result
    data = loginUser(email, password)
    print(data)
    #check if login was successful
    #if email is not verified
    if data == "unverified":
        st.error("Email not verified. Please check your email for verification link")
    #if login successful
    elif data:
        st.success("Login Successful!")
    #if login failed
    else:
        st.error("Login Failed, Please ensure your email and password are correct")
#register page button
if st.button("Register", key="register_page"):
    st.switch_page("Pages/Register.py")


    
    