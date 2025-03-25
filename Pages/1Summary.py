import streamlit as st
from Backend.UserAuth import intialiseSession, sidebarAuth, test
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
    word_num = st.selectbox("Select number of words", [100, 200, 300, 400, 500])
    complexity = st.selectbox("Select complexity", ["low", "medium", "high"])

    if st.button("Get Summary"):
        if query and word_num and complexity:
            with st.spinner("Thinking..."):
                response, context = get_summary(query, word_num, complexity)
        else:
            st.warning("Please enter a query, word count and complexity.")
        
        with st.chat_message("assistant"):
            st.markdown(response)

        
        
        