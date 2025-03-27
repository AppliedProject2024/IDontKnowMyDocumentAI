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
    #header for Upload Section
    st.header("Upload Your Documents")

    #upload multiple files
    uploaded_file = st.file_uploader(
        "Upload one PDF file", 
        type=["pdf"], #only accept pdf files
        accept_multiple_files=False #accept multiple files
    )

    #check if any files are uploaded
    if uploaded_file:
        st.subheader("Uploaded Files")
        
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")
        #placeholder for processing the document
        with st.spinner(f"Processing '{uploaded_file.name}'..."):
            result = upload_file(uploaded_file)
        #check if file was processed successfully
        if result == 200:
            st.success(f"File '{uploaded_file.name}' processed successfully!")
        else:
            st.error(f"Error processing '{uploaded_file.name}'")

    
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
           