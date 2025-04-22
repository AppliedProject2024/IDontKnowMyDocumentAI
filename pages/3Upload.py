import streamlit as st
from Backend.FileProcessing import *
from Backend.UserAuth import intialiseSession, sidebarAuth
from Backend.translations import get_text
#initialise session
intialiseSession()
sidebarAuth()

#check if user is logged in
if not st.session_state.logged_in:
    st.switch_page("pages/Login.py")
else:
    #header for Upload Section
    st.header(f"{get_text('upload_header', st.session_state.language)}")
    #subheader for Upload Section
    st.text(f"{get_text('file_naming_tip', st.session_state.language)}")

    #upload multiple files
    uploaded_file = st.file_uploader(
        get_text('upload_instruction', st.session_state.language),
        accept_multiple_files=False #accept multiple files
    )

    #check if any files are uploaded
    if uploaded_file:
        st.subheader(get_text('uploaded_files', st.session_state.language))
        
        st.success(f"{uploaded_file.name} {get_text('upload_success', st.session_state.language)}")
        #placeholder for processing the document
        with st.spinner(f"{get_text('processing_file', st.session_state.language)}{uploaded_file.name}"):
            result = upload_file(uploaded_file)
        #check if file was processed successfully
        if result == 200:
            st.success(f"{uploaded_file.name} {get_text('processing_success', st.session_state.language)}")
        else:
            st.error(f"{get_text('processing_error', st.session_state.language)} {uploaded_file.name}")