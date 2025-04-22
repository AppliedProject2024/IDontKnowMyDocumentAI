import streamlit as st
from Backend.FileProcessing import *
from Backend.UserAuth import intialiseSession, sidebarAuth
from Backend.translations import get_text

#initialise session
intialiseSession()
sidebarAuth()

#check if user is logged in
if not st.session_state.logged_in:
    st.switch_page("Pages/Login.py")
else:
    #display user documents
    st.header(f"{get_text('documents_header', st.session_state.language)}")

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
            if cols[1].button(f"{get_text('delete_button', st.session_state.language)}", key=f"delete_{filename}"):
                with st.spinner(f"Deleting '{filename}'..."):
                    #delete file
                    result = delete_file(filename)
                #check if file was deleted successfully
                if result:
                    st.rerun()                    

    else:
        st.info(f"{get_text('no_documents', st.session_state.language)}")