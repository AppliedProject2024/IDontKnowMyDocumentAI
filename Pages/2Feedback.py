import streamlit as st
from Backend.UserAuth import intialiseSession, sidebarAuth, retrieveUser 

#initialise session
intialiseSession()
retrieveUser()
sidebarAuth()

#check if user is logged in
if not st.session_state.logged_in:
    st.switch_page("Pages/Login.py")
else:
    #feedback Page
    st.header("Provide Feedback")
    #radio button for feedback type
    feedback_type = st.radio("What would you like to give feedback on?", ["Translation", "Q&A", "Summarization"])
    #text area for feedback
    feedback_text = st.text_area("Write your feedback here:")
    if st.button("Submit Feedback"):
        # Placeholder for storing feedback
        st.success("Thank you for your feedback!")