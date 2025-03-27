import streamlit as st
from Backend.UserAuth import intialiseSession, sidebarAuth, test
from Backend.query import get_mcq

#initialise session
intialiseSession()
sidebarAuth()

#check if user is logged in
if not st.session_state.logged_in:
    st.switch_page("Pages/Login.py")
else:
    #generating mcq (place holder)
    st.title("📝MCQ")
    query = st.text_input("Enter query for MCQ")
    #select box for number of questions
    question_count = st.selectbox("Select number of questions", [5, 10, 15, 20])
    #select box for complexity
    complexity = st.selectbox("Select complexity", ["low", "medium", "high"])

    if st.button("Create MCQ"):
        if query:
            with st.spinner("Thinking..."):
                response, context = get_mcq(query, question_count, complexity)

                st.write(response)
        else:
            st.warning("Please enter a query.")

