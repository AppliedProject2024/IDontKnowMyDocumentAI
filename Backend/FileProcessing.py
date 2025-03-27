import requests
import streamlit as st
from Backend.UserAuth import api_request

# send file to server
def upload_file(file):
    try:
        files = {"file": file}
        # send post request to upload file
        response = api_request("/file/upload", "POST", files=files)
        status_code = response['status_code']
        #check if file was uploaded successfully 
        if status_code == 200:
            return 200
        elif status_code == 409:
            st.warning("File has already been uploaded.")
            return 409
        else:
            st.error("Error uploading file.")
            return status_code
    except requests.exceptions.RequestException as e:
        st.error("Error connecting to server.")

    
#get filenames from server
def get_user_documents():
    try:
        #send get request to get user documents
        response = api_request("/file/extract", "GET")

        #extract filenames
        if response and "data" in response and "filenames" in response["data"]:
            return response["data"]["filenames"]
        
        #return empty list if no filenames
        return []
    
    except requests.exceptions.RequestException as e:
        st.error("Error connecting to server.")
