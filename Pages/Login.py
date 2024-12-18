import streamlit as st
from Backend.UserAuth import loginUser

st.sidebar.error("Please login to access the application")
#login Page
st.title("Login")
#input fields for email and password
email = st.text_input("Email", key="login_email")
password = st.text_input("Password", type="password", key="login_password")

#login button
if st.button("Login"):
    #call loginUser function and store the result
    data = loginUser(email, password)
    #check if login was successful
    if data:
        st.success("Login Successful")
        st.session_state.logged_in = True
        st.switch_page("Main.py")
    else:
        st.error("Login Failed")
#register page button
if st.button("Register", key="register_page"):
    st.switch_page("Pages/Register.py")


    
    