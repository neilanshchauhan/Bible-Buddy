import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# Load the GROQ And OpenAI API KEY
groq_api_key = os.getenv('GROQ_API_KEY')
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

st.title("Bible Buddy †")

llm = ChatGroq(groq_api_key=groq_api_key, model_name="Gemma-7b-it")

prompt_template = ChatPromptTemplate.from_template(
    """
    You are a knowledgeable Bible scholar and AI assistant. Your task is to help users study and understand the Bible. Answer their questions accurately and provide explanations that are informative and reflective of the context of the Bible. Always include the book, chapter, and verse when referencing Bible passages.
    First tell the bible passages according to the question, and then explain it.
    Questions: {input}

    Answer:
    """
)

input_text = st.text_input("Ask your question...")
output_parser = StrOutputParser()
chain = prompt_template | llm | output_parser

if input_text:
    response = chain.invoke({'input': input_text})
    st.write(response)
