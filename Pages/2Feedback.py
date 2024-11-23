import streamlit as st

#feedback Page
st.header("Provide Feedback")
#radio button for feedback type
feedback_type = st.radio("What would you like to give feedback on?", ["Translation", "Q&A", "Summarization"])
#text area for feedback
feedback_text = st.text_area("Write your feedback here:")
if st.button("Submit Feedback"):
    # Placeholder for storing feedback
    st.success("Thank you for your feedback!")