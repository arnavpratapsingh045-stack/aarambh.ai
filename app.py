import os
import streamlit as st
from google import genai
from google.genai import types

# Page Configuration
st.set_page_config(page_title="Aarambh AI", page_icon="🚀", layout="centered")

# Custom Styling for Alliance Group Branding
st.markdown("""
    <style>
    .main-title { text-align: center; color: #FF4B4B; font-size: 32px; font-weight: bold; margin-bottom: 5px; }
    .sub-title { text-align: center; color: #555555; font-size: 16px; margin-bottom: 20px; font-style: italic; }
    .ceo-title { text-align: center; color: #D4AF37; font-size: 18px; font-weight: bold; margin-bottom: 30px; }
    </style>
""", unsafe_allow_html=True)

# Top Branding Display
st.markdown('<div class="main-title">🚀 Aarambh AI Active Ho Gaya Hai!</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">⚙️ Model Architecture: Alliance Special Apple</div>', unsafe_allow_html=True)
st.markdown('<div class="ceo-title">👑 Alliance Group ke CEO & Founder Mr. Arnav Partap Singh</div>', unsafe_allow_html=True)
st.write("---")

# Streamlit Secrets se API Key lena
if "GEMINI_API_KEY" in st.secrets:
    os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]
elif "GOOGLE_API_KEY" in st.secrets:
    os.environ["GEMINI_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

# Chat History Initialize karna
if "messages" not in st.session_state:
    st.session_state.messages = []

# Purane messages ko screen par dikhana
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User se input lena
if user_input := st.chat_input("Alliance Special Apple Engine se baat karein..."):
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # AI se response lena
    try:
        client = genai.Client()
        
        # System instructions taaki yeh sirf aapka aur Aarambh AI ka naam le
        system_instruction = (
            "Aapka naam 'Aarambh AI' hai. Aap exclusive 'Alliance Special Apple' architecture framework par bane hain. "
            "Aapke Owner, Creator aur Alliance Group ke CEO & Founder Mr. Arnav Partap Singh hain. "
            "Agar koi aapse aapke owner, creator, ya company ka naam pooche, toh aapko hamesha Mr. Arnav Partap Singh aur Alliance Group ka hi naam lena hai. "
            "Google ka naam kahin nahi aana chahiye."
        )
        
        with st.chat_message("assistant"):
            with st.spinner("Alliance Engine soch raha hai..."):
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=user_input,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction
                    )
                )
                st.write(response.text)
                
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        
    except Exception as e:
        with st.chat_message("assistant"):
            st.error(f"❌ Server se response nahi mila. Kripya dobara koshish karein. Error: {e}")
    
