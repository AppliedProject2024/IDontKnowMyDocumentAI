import streamlit as st

#header for Upload Section
st.header("Upload Your Documents")

#upload multiple files
uploaded_files = st.file_uploader(
    "Upload one or more PDF files", 
    type=["pdf"], #only accept pdf files
    accept_multiple_files=True #accept multiple files
)

#check if any files are uploaded
if uploaded_files:
    st.subheader("Uploaded Files")
    
    #loop through each uploaded file
    for uploaded_file in uploaded_files:
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")
        #placeholder for processing the document
        st.write(f"Processing '{uploaded_file.name}'...")
