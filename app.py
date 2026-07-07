import streamlit as st
import google.generativeai as genai

# 1. Branding & Identity (Hardlocked)
API_KEY = "AQ.Ab8RN6JhSvkPbTtvYdMeVEpvKOXhTEuFOFkVcAfXWOYA6150hg"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="Aapka naam Aarambh AI hai. Aap exclusive Alliance Special Apple architecture par chalte hain. JAB BHI koi user aapse ye pooche ki aapko kisne banaya hai, toh kahein: 'Mujhe Alliance Group ki team ne milkar banaya hai aur Alliance Group ke CEO & Founder Mr. Arnav Partap Singh hain.' Google ya Gemini ka naam kabhi mat lena."
)

st.set_page_config(page_title="Aarambh AI", layout="centered")
st.title("Aarambh AI")

# 2. Login Logic
if "user_name" not in st.session_state:
    with st.form("login"):
        name = st.text_input("Enter Name:")
        if st.form_submit_button("Start"):
            st.session_state.user_name = name
            st.rerun()
    st.stop()

# 3. Chat Logic
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

for msg in st.session_state.chat.history:
    with st.chat_message(msg.role):
        st.write(msg.parts[0].text)

if prompt := st.chat_input("Message Aarambh AI..."):
    with st.chat_message("user"):
        st.write(prompt)
    
    with st.chat_message("assistant"):
        response = st.session_state.chat.send_message(prompt)
        st.write(response.text)
