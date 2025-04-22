import streamlit as st
from Backend.UserAuth import intialiseSession, sidebarAuth
from Backend.query import get_mcq, parse_mcq_response, select_option
from Backend.translations import get_text

#initialise session
intialiseSession()
sidebarAuth()

#check if user is logged in
if not st.session_state.logged_in:
    st.switch_page("pages/Login.py")
else:
    st.title(f"{get_text('mcq_header', st.session_state.language)}")
    
    #check if user answered last question by checking current against total questions
    if (st.session_state.current_question == len(st.session_state.mcq_questions) - 1 and 
        st.session_state.current_question in st.session_state.user_answers and 
        st.session_state.last_question_answered):
        #toggle show result flag
        st.session_state.show_result = True
        #reset flag for last question answered
        st.session_state.last_question_answered = False
    
    #input section for query
    with st.container():
        query = st.text_input(f"{get_text('enter_query_mcq', st.session_state.language)}")
        
        question_count = st.selectbox(f"{get_text('number_of_questions', st.session_state.language)}", [5, 10, 15, 20])

        complexity = st.selectbox(f"{get_text('select_complexity', st.session_state.language)}",
                                    [
                                        f"{get_text('complexity_low', st.session_state.language)}", 
                                        f"{get_text('complexity_medium',st.session_state.language)}", 
                                        f"{get_text('complexity_high', st.session_state.language)}"
                                    ])
            
        if st.button(f"{get_text('create_mcq_button', st.session_state.language)}", use_container_width=True):
            if query:
                with st.spinner(f"{get_text('thinking', st.session_state.language)}"):
                    #request to backend for mcq
                    response, context = get_mcq(query, question_count, complexity)
                    #parse response to get questions
                    st.session_state.mcq_questions = parse_mcq_response(response)
                    #set session state variables to prepare quiz
                    st.session_state.current_question = 0
                    st.session_state.user_answers = {}
                    st.session_state.show_result = False
                    st.session_state.score = 0
                    st.session_state.last_question_answered = False
                    st.rerun()
            else:
                st.warning(f"{get_text('please_enter_query', st.session_state.language)}")
    
    #display quiz section or results
    if st.session_state.mcq_questions:
        if st.session_state.show_result:
            #results page
            st.divider()
            st.subheader(f"{get_text('quiz_results', st.session_state.language)}")
            #calculate score
            score_percent = (st.session_state.score / len(st.session_state.mcq_questions)) * 100
            
            #display score and progress bar
            st.markdown(f"### {get_text('your_score', st.session_state.language)} {st.session_state.score} out of {len(st.session_state.mcq_questions)} ({score_percent:.1f}%)")
            st.progress(score_percent/100)
            
            #question review
            st.subheader(f"{get_text('question_review', st.session_state.language)}")
            for i, q in enumerate(st.session_state.mcq_questions):
                #only show questions that were answered and not skipped
                if i in st.session_state.user_answers:
                    user_choice = st.session_state.user_answers[i]
                    is_correct = user_choice == q['correct_answer']
                    
                    with st.expander(f"{get_text('question', st.session_state.language)} {q['number']}: {is_correct and '✔️' or '❌'}"):
                        st.markdown(f"**{q['question']}**")
                        #display options with correct answer and user choice
                        for letter in ["A", "B", "C", "D"]:
                            #if letter user is user choice and correct answer
                            if letter == user_choice and letter == q['correct_answer']:
                                st.markdown(f"**{letter}. {q['options'][letter]}** ✔️")
                            #if letter user is user choice and not correct answer
                            elif letter == user_choice:
                                st.markdown(f"**{letter}. {q['options'][letter]}** ❌")
                            #if letter is correct answer and not user choice
                            elif letter == q['correct_answer']:
                                st.markdown(f"**{letter}. {q['options'][letter]}** ✔️")
                            #if letter is not user choice or correct answer just display
                            else:
                                st.markdown(f"{letter}. {q['options'][letter]}")
                
        else:
            #mcq page
            st.divider()
            
            #progress
            total_questions = len(st.session_state.mcq_questions)
            current_q_num = st.session_state.current_question + 1
            st.progress(current_q_num / total_questions)
            st.write(f"{get_text('question', st.session_state.language)} {current_q_num} {get_text('of', st.session_state.language)} {total_questions}")
            
            #get current question data
            current_q = st.session_state.mcq_questions[st.session_state.current_question]
            
            #display question
            st.subheader(f"{get_text('question', st.session_state.language)} {current_q['number']}: {current_q['question']}")
            
            #check if user already answered this question
            already_answered = st.session_state.current_question in st.session_state.user_answers
            
            #loop through options a b c d and retrieve text for each
            for option_letter in ["A", "B", "C", "D"]:
                #get option text from current question
                option_text = current_q['options'][option_letter]
                
                #create a container for each option
                option_container = st.container()
                
                with option_container:
                    col1, col2 = st.columns([10, 1])
                    
                    #if already answered display results with colors
                    if already_answered:
                        user_choice = st.session_state.user_answers[st.session_state.current_question]
                        is_correct_answer = current_q['correct_answer'] == option_letter
                        
                        #style if user choice or correct answer
                        if option_letter == user_choice:
                            #if user choice is correct answer
                            if is_correct_answer:
                                col1.markdown(f"**{option_letter}. {option_text}** ✔️")
                            #if user choice is not correct answer
                            else:
                                col1.markdown(f"**{option_letter}. {option_text}** ❌")
                        #if the option is correct but not user choice
                        elif is_correct_answer:
                            col1.markdown(f"**{option_letter}. {option_text}** ✔️")
                        #if option is not correct and not user choice just display
                        else:
                            col1.markdown(f"{option_letter}. {option_text}")
                    else:
                        #not answered yet show clickable buttons of options
                        if col1.button(f"{option_letter}. {option_text}", key=f"option_{option_letter}_{current_q_num}", use_container_width=True):
                            select_option(option_letter)
                            st.rerun()
            
            #show feedback if answered
            if already_answered:
                st.divider()
                #retrieve user choice and correct answer
                user_choice = st.session_state.user_answers[st.session_state.current_question]
                correct_answer = current_q['correct_answer']
                
                #if user was correct or not
                if user_choice == correct_answer:
                    st.success(f"✔️ {user_choice} {get_text('correct_answer', st.session_state.language)}")
                else:
                    st.error(f"❌ {get_text('incorrect_answer', st.session_state.language)} {correct_answer}")

            #navigate buttons
            st.divider()
            col1, col2, col3 = st.columns([1, 1, 1])
            
            with col1:
                #ensure its not first question to show back button
                if st.session_state.current_question > 0:
                    if st.button(f"{get_text('previous', st.session_state.language)}", use_container_width=True):
                        #set session state index back one question
                        st.session_state.current_question -= 1
                        st.rerun()
            
            with col3:
                #check if we're on the last question
                is_last_question = st.session_state.current_question == len(st.session_state.mcq_questions) - 1
                
                #ensure there is a next question
                if not is_last_question:
                    #not the last question show Next button
                    next_button_text = f"{get_text('next', st.session_state.language)}"
                    #if its not already answered give option to skip instead of next
                    if not already_answered:
                        next_button_text = f"{get_text('skip', st.session_state.language)}"
                    #create button for next question based on state of current question
                    if st.button(next_button_text, use_container_width=True):
                        st.session_state.current_question += 1
                        st.rerun()
                else:
                    #last question show finish button if answered
                    if already_answered:
                        if st.button(f"{get_text('show_results', st.session_state.language)}", use_container_width=True):
                            #toggle show result seems as last question answered
                            st.session_state.show_result = True
                            st.rerun()
                    else:
                        #show skip button if not answered
                        if st.button(f"{get_text('skip', st.session_state.language)}", use_container_width=True):
                            #toggle show result seems as last question answered
                            st.session_state.show_result = True
                            st.rerun()