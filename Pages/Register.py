import streamlit as st
from Backend.UserAuth import registerUser, sidebarAuth

sidebarAuth()

#register Page
st.title("Register")
#input fields for email and password
email = st.text_input("Email", key="register_email")
password = st.text_input("Password", type="password", key="register_password")

#register button
if st.button("Register", key="register_acc"):
    #call registerUser function
    message = registerUser(email, password)
    st.success(message)
