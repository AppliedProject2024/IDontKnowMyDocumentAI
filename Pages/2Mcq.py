import streamlit as st
from Backend.UserAuth import intialiseSession, sidebarAuth, test
from Backend.query import get_mcq

#initialise session
intialiseSession()
sidebarAuth()

data = ""

#check if user is logged in
if not st.session_state.logged_in:
    st.switch_page("Pages/Login.py")
else:
    #generating mcq (place holder)
    st.title("MCQ")
    query = st.text_input("Enter query for MCQ")

    if st.button("Create MCQ"):
        if query:
            data = get_mcq(query)
        else:
            st.warning("Please enter a query.")

    st.write(data)