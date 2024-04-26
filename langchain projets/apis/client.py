import streamlit as st
import requests

def open_ai_response(topic):
    try:
      url = "http://localhost:9090/poem/invoke"
      response = requests.post(url, json={"input" : {"topic": topic}})
      return response.json()['output']['content']
    except Exception as e:
      return f"An error occurred: {e}"
    
def ollama_response(topic):
    try:
      url = "http://localhost:9090/essay/invoke"
      response = requests.post(url, json={"input" : {"topic": topic}})
      return response.json()['output']
    except Exception as e:
      return f"An error occurred: {e}"
    
st.title("APIs with Langchain Serve")

input_text1 = st.text_input("Enter a topic for a poem:")
if st.button("Get Poem"):
  st.write(open_ai_response(input_text1))
  
input_text2 = st.text_input("Enter a topic for an essay:") 
if st.button("Get Essay"):
  st.write(ollama_response(input_text2))