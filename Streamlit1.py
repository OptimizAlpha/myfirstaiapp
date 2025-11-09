##pip install --upgrade langchain langchain-google-genai streamlit
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import streamlit as st
import os

# Set your Google API key
os.environ['GOOGLE_API_KEY'] = "AIzaSyBCzSXWvD8jIx_gYAn6jjtJsJVKXRP6Reo"

# Create the prompt
slides_template = """
Create a presentation outline with {number} slides on the following topic: {topic}.
The target audience is {audience}.

For each slide, provide:
1. A concise title
2. 2-3 key bullet points or a short paragraph of content
3. A thought-provoking question or discussion point related to the slide's content

Format the output as follows:

Slide 1: [Title]
- Content
- Content
Questions/Discussion: [Relevant question or discussion point]

Slide 2: [Title]
... and so on
"""

slides_prompt = PromptTemplate(
    template=slides_template,
    input_variables=["number", "topic", "audience"]
    )

# Initialize Gemini model
gemini_model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Create the chain using the LCEL (LangChain Expression Language)
slides_chain = slides_prompt | gemini_model

# Streamlit UI
st.header("Slide Generator")
st.subheader("Generate slides using Generative AI")

topic = st.text_input("Topic")
audience = st.text_input("Enter the target audience (e.g., investors, students):")
number = st.number_input("Number of slides", min_value=1, max_value=10, value=1, step=1)

##audience = "general audience"

if st.button("Generate"):
    st.write("Generating slides...")
    response = slides_chain.invoke({"number": number, "topic": topic, "audience": audience})
    st.write(response.content)

    


