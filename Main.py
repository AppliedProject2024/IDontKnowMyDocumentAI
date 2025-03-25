import streamlit as st
from Backend.UserAuth import intialiseSession, sidebarAuth
from Backend.query import get_query

# Initialize session
intialiseSession()
sidebarAuth()

#check if user is logged in
if not st.session_state.logged_in:
    st.switch_page("Pages/Login.py")

#header
st.title("🤖 IDontKnowMyDocument AI")

#user input
user_input = st.chat_input("Enter your question...")

#if user submits a query
if user_input:
    #add user input to message queue
    st.session_state.messages.append({"role": "user", "message": user_input})

    #get AI response and context
    with st.spinner("Thinking..."):
        response, context = get_query(user_input)

    #add AI response to message queue
    st.session_state.messages.append({"role": "assistant", "message": response})

#display messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["message"])
