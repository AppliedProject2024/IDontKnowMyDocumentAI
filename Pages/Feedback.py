import streamlit as st
from Backend.UserAuth import intialiseSession, sidebarAuth 
from Backend.feedback import send_feedback
from Backend.translations import get_text

#initialise session
intialiseSession()
sidebarAuth()

#check if user is logged in
if not st.session_state.logged_in:
    st.switch_page("Pages/Login.py")
else:
    #feedback Page
    st.header(f"{get_text('feedback_header', st.session_state.language)}")
    #radio button for feedback type
    feedback_type = st.radio(
        f"{get_text('feedback_type_label', st.session_state.language)}", [
        f"{get_text('feedback_translation',st.session_state.language)}", 
        f"{get_text('feedback_qa',st.session_state.language)}",
        f"{get_text('feedback_summarisation',st.session_state.language)}",
        f"{get_text('feedback_mcq',st.session_state.language)}"
    ])
    #text area for feedback
    feedback_text = st.text_area(f"{get_text('feedback_text_label',st.session_state.language)}")
    if st.button(f"{get_text('submit_button',st.session_state.language)}"):
        # Placeholder for storing feedback
        st.success(f"{get_text('feedback_thank_you',st.session_state.language)}")
        #send feedback
        result = send_feedback(feedback_type,feedback_text)