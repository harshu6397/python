# import nescessary library

from langchain.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langserve import add_routes
from fastapi import FastAPI
import uvicorn
import os
from dotenv import load_dotenv

# load the environment variables
load_dotenv()

# setup the environment variables
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")

app = FastAPI(
  title="Chatbot API",
  description="This is a chatbot API that can answer questions about the world.",
  version="0.1.0"
)

open_ai_llm = ChatOpenAI()
ollama_llm = Ollama(model="llama3")

prompt1 = ChatPromptTemplate.from_template("Write me a poem about {topic} in 100 words or less.")
prompt2 = ChatPromptTemplate.from_template("Write me a Essay about {topic} in 100 words or less.")

add_routes(
  app,
  prompt1 | open_ai_llm,
  path='/poem'
)

add_routes(
  app,
  prompt2 | ollama_llm,
  path='/essay'
)

if __name__ == "__main__":
  uvicorn.run(app, host="localhost", port=9090)