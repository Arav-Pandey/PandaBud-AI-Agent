import streamlit as st
import os
from google import genai

def fetch_gemini(text):
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    res = client.models.generate_content(
        model="gemini-3-flash-preview",   # free tier model
        contents=text,
    )
    return res.text

def main():
    try:
        st.header("Personal PandaBud AI Agent")

        text = st.text_input("Ask a question to the PandaBud")
    
        if text:
            st.subheader("PandaBud's Response:")
            with st.spinner("PandaBud is thinking..."):
                st.markdown(fetch_gemini(text))
    except Exception as e:
        st.header(f"Error Occurred: {e}")


if __name__ == "__main__":
    main()
