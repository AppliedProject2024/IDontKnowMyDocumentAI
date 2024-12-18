import streamlit as st
from Backend.UserAuth import registerUser

#register Page
st.title("Register")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

#register button
if st.button("Register"):
    message = registerUser(email, password)
    st.success(message)
