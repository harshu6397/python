# Import necessary libraries
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# setup the environment variables
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")

# create the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a  very smart and Intelligent chatbot that can answer questions about the world."),
        ("human", "Question: {question}"),
    ]
)

# create the chatbot
llm = ChatOpenAI(streaming=True)

# create the output parser
output_parser = StrOutputParser()

# craete the chain
chain = prompt | llm | output_parser

# create the streamlit app
st.title("Chatbot")
st.markdown("This is a chatbot that can answer questions about the world.")
input_text = st.text_input("Enter your question here:")
if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)