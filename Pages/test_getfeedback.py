import streamlit as st
from Backend.feedback import get_feedback

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