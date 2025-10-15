import streamlit as st
import openai
# Set your OpenAI API key
import os
from openai import OpenAI

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
model_name = "openai/gpt-4o-mini"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

# Function to call the OpenAI API
def get_joke_explanation(joke):
    response =  client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"Explain this joke: {joke}",
        }
    ],
    model="gpt-4o-mini",
    )

    explanation = response.choices[0].message.content
    return explanation

# Streamlit application
st.title("Joke Explainer")

# Text box for user input
joke = st.text_area("Enter your joke here:")

# Submit button
if st.button("Submit"):
    if joke:
        explanation = get_joke_explanation(joke)
        st.subheader("Explanation:")
        st.write(explanation)
    else:
        st.warning("Please enter a joke to get an explanation.")