import streamlit as st
from Backend.UserAuth import intialiseSession, sidebarAuth, test
from Backend.query import get_query

#initialise session
intialiseSession()
sidebarAuth()

data = ""

#check if user is logged in
if  not st.session_state.logged_in:
    st.switch_page("Pages/Login.py")

else:
    #header
    st.title("IDontKnowMyDocument AI")
    st.subheader("Interact with your documents: Translate, Summarize, and Ask Questions")

    #input Box for Questions or Text
    user_input = st.text_area("Enter your text or ask a question:")

    #button to submit question or text
    if st.button("Get Answer"):
            if user_input:
                data = get_query(user_input)
            else:
                st.warning("Please enter a question.")

    #display response
    st.write(data) 

        
        
        