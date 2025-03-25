import streamlit as st
from Backend.feedback import get_feedback

#check if user is logged in
if not st.session_state.logged_in:
    st.switch_page("Pages/Login.py")
else:
    #feedback Page (test)
    st.header("Feedback")
    # Get feedback
    feedback = get_feedback()
    # Display feedback
    for f in feedback:
        st.write("Feedback ID: ", f["id"])
        st.write("User Email: ", f["user_email"])
        st.write(f["feedback_type"])
        st.write(f["feedback"])
        st.write("timestamp: ", f["created_at"])