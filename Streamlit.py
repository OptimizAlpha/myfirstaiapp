from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import streamlit as st
import os

# Set your Google API key
os.environ['GOOGLE_API_KEY'] = "AIzaSyBCzSXWvD8jIx_gYAn6jjtJsJVKXRP6Reo"

# Create the prompt
tweet_template = "Give me {number} tweets on {topic}"
tweet_prompt = PromptTemplate(template=tweet_template, input_variables=["number", "topic"])

# Initialize Gemini model
gemini_model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Create the chain using the LCEL (LangChain Expression Language)
tweet_chain = tweet_prompt | gemini_model

# Streamlit UI
st.header("Tweet Generator by Anil")
st.subheader("Generate tweets using Generative AI")

topic = st.text_input("Topic")
number = st.number_input("Number of tweets", min_value=1, max_value=10, value=1, step=1)

if st.button("Generate"):
    st.write("Generating tweets...")
    response = tweet_chain.invoke({"number": number, "topic": topic})
    st.write(response.content)

    





