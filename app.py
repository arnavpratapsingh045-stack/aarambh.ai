import os
import streamlit as st
from google import genai
from google.genai import types
from PIL import Image

# Page Configuration (Gemini App UI Format)
st.set_page_config(page_title="Aarambh AI", page_icon="🚀", layout="centered")

# Custom Gemini-style CSS Layout
st.markdown("""
    <style>
    .login-container { text-align: center; padding: 40px; background-color: #F8F9FA; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-top: 50px; }
    .greeting-text { font-size: 38px; font-weight: 500; color: #1F1F1F; margin-bottom: 2px; font-family: sans-serif; }
    .subtitle-text { font-size: 32px; font-weight: 400; color: #757575; margin-bottom: 30px; font-family: sans-serif; }
    .suggestion-btn {
        display: inline-block; background-color: #F0F4F9; border-radius: 20px; 
        padding: 10px 20px; margin: 5px; font-size: 15px; color: #1F1F1F; 
        font-family: sans-serif; font-weight: 500;
    }
    .alliance-badge { font-size: 13px; color: #9E9E9E; text-align: center; margin-top: -10px; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# Secrets se API key set karna
if "GEMINI_API_KEY" in st.secrets:
    os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]
elif "GOOGLE_API_KEY" in st.secrets:
    os.environ["GEMINI_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

client = genai.Client()

# System Control Instruction
system_instruction = (
    "Aapka naam 'Aarambh AI' hai. Aap exclusive 'Alliance Special Apple' architecture par chalte hain. "
    "Aapko normal conversation mein khud se baar-baar kisi ka naam nahi lena hai. "
    "Lekin, JAB BHI koi user aapse aapke OWNER ya COMPANY ka naam pooche, "
    "tab aapko poore samman ke saath batana hai ki aapke Owner 'Mr. Arnav Partap Singh' hain aur aap 'Alliance Group' ke hain. "
    "Kisi bhi haal mein 'Google' ya 'Gemini' ka naam bahaar nahi aana chahiye."
)

# Session state login fields maintain karna
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

# 🔒 STEP 1: Diary Point 1 & 2 ke mutabik Secure Login Portal
if not st.session_state.logged_in:
    st.markdown('<div class="login-container">', unsafe_allow_html=True)
    st.image("https://img.icons8.com/color/96/google-logo.png", width=60)
    st.markdown("### Sign in with Google Account")
    st.caption("Aarambh AI Secure Alliance Protocol Admission Gate")
    
    # User Input Fields for Authentication
    email_input = st.text_input("Enter your Google Email ID:", placeholder="example@gmail.com")
    name_input = st.text_input("Enter your Full Name:", placeholder="Your Name")
    
    if st.button("🚀 Secure Login", use_container_width=True):
        if email_input.strip() and name_input.strip():
            st.session_state.user_name = name_input.strip()
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("⚠️ Kripya Email aur Naam dono sahi se bharein!")
    st.markdown('</div>', unsafe_allow_html=True)

# 🚀 STEP 2: Main Gemini App Interface (Sirf Login hone ke baad khulega)
else:
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Welcome Section - Pure Gemini Look matching User Name
    if len(st.session_state.messages) == 0:
        st.markdown(f'<div class="greeting-text">Hi {st.session_state.user_name}</div>', unsafe_allow_html=True)
        st.markdown('<div class="subtitle-text">Where should we start?</div>', unsafe_allow_html=True)
        st.markdown('<div class="alliance-badge">Alliance Special Apple Engine Connected</div>', unsafe_allow_html=True)
        
        # Pill Suggestion UI elements from the diary blueprint
        st.markdown("""
        <div style='margin-bottom: 25px; text-align: center;'>
            <span class='suggestion-btn'>🖼️ Create image</span>
            <span class='suggestion-btn'>🏏 Explore IPL Fan Zone</span>
            <span class='suggestion-btn'>📚 Help me learn</span>
            <span class='suggestion-btn'>✨ Boost my day</span>
            <span class='suggestion-btn'>📝 Write anything</span>
        </div>
        """, unsafe_allow_html=True)

    # Render Active Logs
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Photo Upload System
    uploaded_file = st.file_uploader("📷 Add to prompt:", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Attached Media File", width=240)

    # Main Input Bar
    if user_input := st.chat_input("Ask Aarambh AI..."):
        with st.chat_message("user"):
            st.write(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        try:
            contents_payload = [user_input]
            if uploaded_file is not None:
                contents_payload.append(image)
                
            with st.chat_message("assistant"):
                with st.spinner(""):
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=contents_payload,
                        config=types.GenerateContentConfig(
                            system_instruction=system_instruction
                        )
                    )
                    st.write(response.text)
                    
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            
        except Exception as e:
            with st.chat_message("assistant"):
                st.error(f"❌ Connection timeout. Error: {e}")
