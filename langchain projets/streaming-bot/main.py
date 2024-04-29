# Import necessary libraries
# pip install langchain streamlit langchain-openai python-dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

# setup the environment variables
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")

st.set_page_config(page_title="Streaming Bot", page_icon="🤖")

st.title("Streaming Bot")

# Chatbot memory management
if "chat_history" not in st.session_state:
  st.session_state.chat_history = []
  
#  get AI response
def get_ai_response(query, chat_history):
  template = """
    You are a helpful friendly assisant. Answer the following quesrions considering the following:
    
    Chat history: {chat_history}
    
    User Question: {user_question}
  """
  prompt = ChatPromptTemplate.from_template(template);
  llm = ChatOpenAI()
  output_parser = StrOutputParser()
  chain = prompt | llm | output_parser
  return chain.stream({
    "chat_history":chat_history,
    "user_question": query
  })

# show conversation
for message in st.session_state.chat_history:
  if isinstance(message, HumanMessage):
    with st.chat_message("Human"):
      st.markdown(message.content)
  else:
    with st.chat_message("AI"):
      st.markdown(message.content)

user_query = st.chat_input("Enter your message...")
if user_query is not None and user_query != "":
  st.session_state.chat_history.append(HumanMessage(user_query))
  
  with st.chat_message("Human"):
    st.markdown(user_query)
    
  with st.chat_message("AI"):
    ai_response = st.write_stream(get_ai_response(user_query, st.session_state.chat_history))
    
  st.session_state.chat_history.append(AIMessage(ai_response))