import requests
import streamlit as st
from Backend.UserAuth import api_request
from Backend.translations import get_text

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
            st.warning(f"{get_text('file_already_uploaded', st.session_state.language)}")
            return 409
        else:
            st.error(f"{get_text('error_uploading_file', st.session_state.language)}")
            return status_code
    except requests.exceptions.RequestException as e:
        st.error(f"{get_text('server_connection_error', st.session_state.language)}")

    
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
        st.error(f"{get_text('server_connection_error', st.session_state.language)}")


def delete_file(filename):
    try:
        #send delete request to delete file
        response = api_request("/file/delete", "DELETE", {"filename": filename})
        
        return response
    except requests.exceptions.RequestException as e:
        st.error(f"{get_text('server_connection_error', st.session_state.language)}")