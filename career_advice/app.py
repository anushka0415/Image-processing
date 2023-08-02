
import streamlit as st
from old_resume import old_resume,generate_questions,generate_detailed_questions,generate_gpt_response
import openai
def main():

    st.title("AI career advice")

    st.write("\n")

    col1, col2 = st.columns([1, 3])

    with col1:
        st.write("What is your current role?")

    with col2:

        options = ["Select","Student", "Fresher","working professional"]
        selected_option1 = st.selectbox("", options)
    
    st.write("\n")
    country = st.text_input("Country where you would like to achieve your goal:")
    

    st.write("\n")
    col1, col2 = st.columns([1, 3])

    with col1:
        st.write("What is your Goal?")

    with col2:

        options = ["Select","Pursue higher studies","Get a job","Switch my job"]
        selected_option2 = st.selectbox("", options)

   
    st.write("\n")

    col1, col2 = st.columns([1, 3])

    with col1:
        st.write("Do you have a resume to upload?")

    with col2:

        options = ["Select","Yes", "No"]
        selected_option = st.selectbox("", options)
    
    
    user_answers = {}
    submit_button = None
    if selected_option == "Yes":
        text=old_resume()
        #st.text_area("Resume",value=text,height=1000)
        questions=generate_questions(text,selected_option1,selected_option2,country)
        if questions:
            questions_list=[]
            questions_list=questions.split("\n")
            
            with st.form("Please answer the following questions:"):
                for i in range(len(questions_list)):
                    answer=st.text_input(questions_list[i],key=f"answer_{i}")
                    user_answers[questions_list[i]] = answer
                submit_button = st.form_submit_button("Submit Answers")

               
        
        
    if selected_option =="No":
        text=None
        questions = generate_detailed_questions(selected_option1, selected_option2,country)
        if questions:
            questions_list=[]
            questions_list=questions.split("\n")
        
            with st.form("Please answer the following questions:"):
                for i in range(len(questions_list)):
                    answer=st.text_input(questions_list[i],key=f"answer_{i}")
                    user_answers[questions_list[i]] = answer
                submit_button = st.form_submit_button("Submit Answers")
    
    if submit_button:
            # Pass the user answers to your GPT model and get the response
            gpt_response = generate_gpt_response(text,selected_option1,selected_option2,user_answers,country)

            # Display the GPT-generated response back to the user
            st.subheader("Our Advice:")
            st.write(gpt_response)


        # if questions:
        #     # Display the generated questions and get user answers
        #     st.subheader("Kindly answer the following questions:")
        #     user_answers = {}
        #     for idx, question in enumerate(questions, start=1):
        #         user_answer = st.text_input(f"{idx}. {question}")
        #         user_answers[question] = user_answer

            # if st.button("Submit Answers"):
            #     # Add code here to process the user answers and provide recommendations
            #     # For the sake of example, we'll just display the user answers
            #     st.subheader("User Answers:")
            #     for question, answer in user_answers.items():
            #         st.write(f"{question}: {answer}")
                
        
   
        
 
    
  
        
        

if __name__ == "__main__":
    main()


# %%
