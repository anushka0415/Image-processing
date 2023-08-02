import streamlit as st
import openai
import numpy as np
import pandas as pd
import os
import os.path
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import warnings
warnings.filterwarnings("ignore")
from utils import *
from config import CONFIG
from utils import generate_openai_answer
import json

def old_resume():
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])


    if uploaded_file is not None:
    # Process the uploaded PDF file here
        st.write("You uploaded a PDF file!")
        def convert_pdf_to_txt(path):
            """
            Converts a pdf file to text
                inputs:
                    path: path to the pdf file
                    file: name of the pdf file
                returns:
                    text: text extracted from the pdf file
            """
            rsrcmgr = PDFResourceManager()
            retstr = StringIO()
            codec = "utf-8"
            laparams = LAParams()
            device = TextConverter(rsrcmgr, retstr, laparams=laparams)
            fp = path
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            password = ""
            maxpages = 0
            caching = True
            pagenos = set()

            for page in PDFPage.get_pages(
                fp,
                pagenos,
                maxpages=maxpages,
                password=password,
                caching=caching,
                check_extractable=True,
            ):
                interpreter.process_page(page)

            text = retstr.getvalue()

            fp.close()
            device.close()
            retstr.close()
            return text
        pdf_text=convert_pdf_to_txt(uploaded_file)
        return pdf_text

def generate_questions(text,selected_option1,selected_option2,country):
    if text is not None:
        model = CONFIG['open_ai']['openai_model_name']
      #     prompt= f"""Create a resume by using simple resume template and don't provide extra information and using the given information\n\nName:{name}\nContact Number: {contact_number}\nEmail ID: {email_id}\nLinkedIn Profile URL: {linkedin_url}\nGitHub Profile URL: {github_url}\nPersonal Website: {personal_website}\nCountry: {country}\nState: {state}\nCity: {city}\n\nResume:"
      # \n\nquery:"""
        prompt=f"""You are the best AI career coach. A user is providing you with the following data:
            {text}. They are a {selected_option1} looking for {selected_option2} in {country}.You have to generate a set of 5 and only 5 questions based on the data provided that will help them achieve their goal given in {selected_option2}.
            Rules:-
            1. The questions should be relevant to {selected_option1} and {selected_option2}
            2. For higher studies ask about GPAs,scholarships , interests,projects and so on.
            3. For finding jobs ask about internships, projects, level of experience and certifications.
            4. For job switches ask about interest, prior skills and so on based on your understanding. 
            5. Don't ask redundant questions and don't ask for information already given in {text}
            """
        found_query = generate_openai_answer(prompt)
        return found_query

def generate_detailed_questions(selected_option1,selected_option2,country):
     model = CONFIG['open_ai']['openai_model_name']
      #     prompt= f"""Create a resume by using simple resume template and don't provide extra information and using the given information\n\nName:{name}\nContact Number: {contact_number}\nEmail ID: {email_id}\nLinkedIn Profile URL: {linkedin_url}\nGitHub Profile URL: {github_url}\nPersonal Website: {personal_website}\nCountry: {country}\nState: {state}\nCity: {city}\n\nResume:"
      # \n\nquery:"""
     prompt=f"""You are the best AI career coach.A user is providing you with the following data:
            They are a {selected_option1} looking for {selected_option2} in {country}.You have to generate a set of 10 questions based on the data provided that will help them achieve their goal given in {selected_option2}.Ask questions like a real career guidance counsellor would.
            Rules:-
            1. The questions should be relevant to {selected_option1} and {selected_option2}
            2. For higher studies ask about GPAs,scholarships , interests,projects and so on.
            3. For finding jobs ask about internships, projects, level of experience and certifications.
            4. For job switches ask about interest, prior skills and so on based on your understanding. 
            5.Keep the questions brief.
            """
     found_query = generate_openai_answer(prompt)
     return found_query

def generate_gpt_response(text,selected_option1,selected_option2,user_answers,country):
     model = CONFIG['open_ai']['openai_model_name']
      #     prompt= f"""Create a resume by using simple resume template and don't provide extra information and using the given information\n\nName:{name}\nContact Number: {contact_number}\nEmail ID: {email_id}\nLinkedIn Profile URL: {linkedin_url}\nGitHub Profile URL: {github_url}\nPersonal Website: {personal_website}\nCountry: {country}\nState: {state}\nCity: {city}\n\nResume:"
      # \n\nquery:"""
     prompt=f"""You are the best AI career coach.A user is providing you with the following data:{text} and {user_answers}.
            They are a {selected_option1} looking for {selected_option2}.Generate them career advice on the basis of {selected_option1},{selected_option2},{text} and {user_answers}.
            Rules:-
            1. The Advice should be relevant to {selected_option1},{selected_option2} and {user_answers}.Do not give generic advice. Be very specific. Give names, facts, Courses, options and figures.
            2. For higher studies suggest names of Institites, name of courses and their estimate fees keeping in mind the {country} in the format Name of the institute:"ABC",Courses offered:"XYZ". 
            3. For finding jobs suggest roles based on given information, prior experience and median salary for that {country}.
            4. For job switches based on your understanding suggest certifications, roles and other advices.
            5. Keep the points brief and to the point and give advice only according to rule 1.
            6. Do not give warnings,notes or any unimportant stuff
            7.Give brief advices.stick to points.
            8. Do not include questions or queries.
            """
     found_query = generate_openai_answer(prompt)
     return found_query
      
        
          
      
       
       
      
       
      
    
      
      
         
     

       
      

