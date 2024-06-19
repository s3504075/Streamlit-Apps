# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 19:33:06 2024

@author: Snoopy
"""
#https://docs.streamlit.io/
import streamlit as st
from openai import OpenAI
import os
import random
import time
 
def providerecipe(recipequestion):
    
       recipes=0
       system_prompt='You are an experienced cook.  Provide me with your best suggestion for the requested recipe based on your experience and knowledge.'

       messages.append({'role':'system','content':system_prompt})
       messages.append({'role':'user', 'content': recipequestion})
       n=2 #number of recipes returned
       botresponse=client.chat.completions.create(model='gpt-3.5-turbo', messages=messages,n=n,temperature=1.6,presence_penalty=1.0)
       progress_text = "Recipe generation in progress. Please wait."
       my_bar = st.progress(0, text=progress_text)
    
       for percent_complete in range(100):
          time.sleep(0.1)
          my_bar.progress(percent_complete + 1, text=progress_text)
       time.sleep(1)
       my_bar.empty()
       
       
       recipes=len(botresponse.choices)
       with st.chat_message("assistant"):
         for i in range(0,recipes):
           st.subheader(f"Recipe {i+1}",divider=True)
           st.write(botresponse.choices[i].message.content)
           
     

def init_existing_messages():
    if "messages" not in st.session_state:
        st.session_state["messages"] = []
    #for message in st.session_state["messages"]:
     #   with st.chat_message(message["role"]):
     #       st.markdown(message["content"])

        
def addrecipe(request):
    
    if request:
       st.session_state["messages"].append({"role": "user", "content": request})
       with st.chat_message("user"):
           st.markdown(request)


if __name__ == '__main__':
    os.environ["OPENAI_API_KEY"]=0
    os.getenv('OPENAI_API_KEY')
    client=OpenAI() #can also pass key to client if enviro vbl not set
    random.seed()
    #sample questions
    #q1="Provide me with a recipe for a lemon risotto.  It should include the ingredients, quantities, and cooking instructions."
    #q2="Provide me with a recipe for red beans and rice.  It should include the ingredients, quantities, and cooking instructions."
    #q3="Proide me with a recipe for pasta with chicken, tomatoes and peas. It should include the ingredients, quantities, and cooking instructions." '''
    messages=list()
    col1,col2=st.columns([0.80,0.20]) #set the page columns
    with col1:
        st.subheader('Welcome to the ChatGPT Recipe Chatbot!', divider='violet') #create the header
        
    with col2:
        st.image("recipesfromchatgpt.png") #import i mage
    init_existing_messages() #initialize responses
    with st.container(border=True):
      reciperequest = st.chat_input("Ask me for a recipe. ")
      if reciperequest:
        addrecipe(reciperequest)
        providerecipe(reciperequest)
    #recipechatbot(questions, responses, messages)
    
