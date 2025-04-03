import streamlit as st
from Backend.UserAuth import intialiseSession, sidebarAuth
from Backend.query import get_summary

#initialise session
intialiseSession()
sidebarAuth()

#check if user is logged in
if not st.session_state.logged_in:
    st.switch_page("Pages/Login.py")
else:
    #generating summary (place holder)
    st.title("📚Summary")
    #text input for query
    query = st.text_input("Enter query for summarisation")
    #select box for number of words
    word_num = st.selectbox("Select number of words", [100, 200, 300, 400, 500])
    #select box for complexity
    complexity = st.selectbox("Select complexity", ["low", "medium", "high"])

    #button to get summary
    if st.button("Get Summary"):
        #check if query, word_num and complexity are entered
        if query and word_num and complexity:
            #get summary and context 
            with st.spinner("Thinking..."):
                response, context = get_summary(query, word_num, complexity)

            st.session_state.summary = {"role": "assistant", "message": response}

        else:
            st.warning("Please enter a query, word count and complexity.")
    
    if st.session_state.summary != None:
        #display messages
        message = st.session_state.summary
        with st.chat_message(message["role"]):
            st.markdown(message["message"])
        