# app.py

import streamlit as st
import openai
import os

# Set up OpenAI API
openai.api_type = "azure"
openai.api_base = "https://openailisterr.openai.azure.com/"
openai.api_version = "2023-09-15-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to generate response using OpenAI
def generate_response(prompt):
    response = openai.Completion.create(
        engine="Productlabelgeneration",
        prompt=prompt,
        temperature=0.3,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    return response.choices[0].text.strip()

# Streamlit app
def main():
    st.title("OpenAI GPT-3.5 Streamlit App")

    # Input prompt from the user
    user_prompt = st.text_area("Enter your prompt:", "")

    if st.button("Generate Response"):
        # Generate response using OpenAI API
        if user_prompt:
            st.markdown("### Generated Response:")
            response_text = generate_response(user_prompt)
            st.write(response_text)
        else:
            st.warning("Please enter a prompt.")

if __name__ == "__main__":
    main()
