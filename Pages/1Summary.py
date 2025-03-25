import streamlit as st
from Backend.UserAuth import intialiseSession, sidebarAuth, test
from Backend.query import get_summary

#initialise session
intialiseSession()
sidebarAuth()

data = ""

#check if user is logged in
if not st.session_state.logged_in:
    st.switch_page("Pages/Login.py")
else:
    #generating summary (place holder)
    st.title("Summary")
    #text input for query
    query = st.text_input("Enter query for summarisation")

    if st.button("Get Summary"):
        if query:
            data = get_summary(query)
        else:
            st.warning("Please enter a question.")

    st.write(data)

        
        
        