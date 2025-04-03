import streamlit as st
from Backend.FileProcessing import *
from Backend.UserAuth import intialiseSession, sidebarAuth

#initialise session
intialiseSession()
sidebarAuth()

#check if user is logged in
if not st.session_state.logged_in:
    st.switch_page("Pages/Login.py")
else:
    #display user documents
    st.header("Your Documents")

    #get user documents
    filenames = get_user_documents()

    #if filesnames exist
    if filenames:
        #loop through filenames
        for filename in filenames:
            #create a table to display filenames
            cols= st.columns([3,1])
            #display filename
            cols[0].write(filename)

            #create delete button on each row
            if cols[1].button("Delete", key=f"delete_{filename}"):
                st.warning(f"Delete {filename}")

    else:
        st.info("No documents uploaded yet.")