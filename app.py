import streamlit as st
from google import genai
from google.genai import types
import os

# 1. Page Setup
st.set_page_config(page_title="Aarambh AI", page_icon="🚀")
st.title("Aarambh AI")

# 2. API Setup
if "GEMINI_API_KEY" in st.secrets:
    os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]
client = genai.Client()

# 3. Branding Instructions
system_instruction = (
    "Aapka naam 'Aarambh AI' hai. Aap exclusive 'Alliance Special Apple' architecture par chalte hain. "
    "JAB BHI koi user pooche ki aapko kisne banaya hai, toh batayein: "
    "'Mujhe Alliance Group ki team ne milkar banaya hai aur Alliance Group ke CEO & Founder Mr. Arnav Partap Singh hain.' "
    "Kisi bhi haal mein 'Google' ya 'Gemini' ka naam bahaar nahi aana chahiye."
)

# 4. Chat History Initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

# 5. Display History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 6. Core Chat Engine
if prompt := st.chat_input("Ask Aarambh AI..."):
    # User message display
    with st.chat_message("user"):
        st.write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Assistant Response
    with st.chat_message("assistant"):
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction
                )
            )
            st.write(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error("Error: Please check your API Key or connection.")
        
