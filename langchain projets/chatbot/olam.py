# Import necessary libraries
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# setup the environment variables
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")

# create the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a very smart and intelligent chatbot that can answer questions about the world."),
        ("human", "Question: {question}"),
    ]
)

# create the chatbot
llm = Ollama(model="codellama")

# create the output parser
output_parser = StrOutputParser()

# create the chain
chain = prompt | llm | output_parser

# create the streamlit app
st.title("Chatbot")
st.markdown("This is a chatbot that can answer questions about the world.")
input_text = st.text_input("Enter your question here:")

if input_text:
    # Use a placeholder to display the loading status
    placeholder = st.empty()
    with st.spinner('Thinking...'):
        # Invoke the chain asynchronously
        response_future = chain.invoke({"question": input_text})
        try:
            # Display the response
            placeholder.write(response_future)
        except Exception as e:
            st.error(f"An error occurred: {e}")
