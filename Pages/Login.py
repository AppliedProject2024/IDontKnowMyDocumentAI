import streamlit as st
from Backend.UserAuth import loginUser

st.title("Login")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    data = loginUser(email, password)
    if data:
        st.success("Login Successful")
    else:
        st.error("Login Failed")