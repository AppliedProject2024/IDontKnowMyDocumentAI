import streamlit as st
from Backend.UserAuth import intialiseSession, sidebarAuth
from Backend.query import get_summary
from Backend.translations import get_text

#initialise session
intialiseSession()
sidebarAuth()

#check if user is logged in
if not st.session_state.logged_in:
    st.switch_page("pages/Login.py")
else:
    #generating summary (place holder)
    st.title(f"{get_text('summary_header', st.session_state.language)}")
    #text input for query
    query = st.text_input(f"{get_text('enter_query_summary', st.session_state.language)}")
    #select box for number of words
    word_num = st.selectbox(f"{get_text('select_word_count', st.session_state.language)}", [100, 200, 300, 400, 500])
    #select box for complexity
    complexity = st.selectbox(f"{get_text('select_complexity', st.session_state.language)}",
                                [
                                    f"{get_text('complexity_low', st.session_state.language)}", 
                                    f"{get_text('complexity_medium',st.session_state.language)}", 
                                    f"{get_text('complexity_high', st.session_state.language)}"
                                ])

    #button to get summary
    if st.button(f"{get_text('get_summary_button', st.session_state.language)}"):
        #check if query, word_num and complexity are entered
        if query and word_num and complexity:
            #get summary and context 
            with st.spinner(f"{get_text('thinking', st.session_state.language)}"):
                response, context = get_summary(query, word_num, complexity)

            st.session_state.summary = {"role": "assistant", "message": response}

        else:
            st.warning(f"{get_text('enter_all_fields', st.session_state.language)}")
    
    if st.session_state.summary != None:
        #display messages
        message = st.session_state.summary
        with st.chat_message(message["role"]):
            st.markdown(message["message"])
        