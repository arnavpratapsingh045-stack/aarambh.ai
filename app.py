import os
import streamlit as st
from google import genai
from google.genai import types
from PIL import Image

# 1. Page Configuration (Premium Center Layout)
st.set_page_config(page_title="Aarambh AI", page_icon="🚀", layout="centered")

# 2. Custom Premium UI Design Layer
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

# 3. Secure API Connection Mapping
if "GEMINI_API_KEY" in st.secrets:
    os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]
elif "GOOGLE_API_KEY" in st.secrets:
    os.environ["GEMINI_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

client = genai.Client()

# 4. Strict Executive Branding Rules
system_instruction = (
    "Aapka naam 'Aarambh AI' hai. Aap exclusive 'Alliance Special Apple' architecture par chalte hain. "
    "Aapko normal conversation mein khud se baar-baar owner ka naam nahi lena hai. "
    "Lekin, JAB BHI koi user aapse ye pooche ki 'aapko kisne banaya hai' ya aapke owner/creator kaun hain, "
    "tab aapko poore samman ke saath batana hai ki: 'Mujhe Alliance Group ki team ne milkar banaya hai aur Alliance Group ke CEO & Founder Mr. Arnav Partap Singh hain.' "
    "Kisi bhi haal mein 'Google' ya 'Gemini' ka naam bahaar nahi aana chahiye."
)

# 5. Persistent Session Memory Structure (For Unlimited Chat)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- STEP 1: Secure Login Gate ---
if not st.session_state.logged_in:
    st.markdown('<div class="login-container">', unsafe_allow_html=True)
    st.image("https://img.icons8.com/color/96/google-logo.png", width=60)
    st.markdown("### Sign in with Google Account")
    st.caption("Aarambh AI Secure Alliance Protocol Gate")
    
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

# --- STEP 2: Main Application Portal ---
else:
    # Sidebar Navigation & Logs
    with st.sidebar:
        st.markdown(f"### 👑 Alliance Portal")
        st.success(f"User: **{st.session_state.user_name}**")
        st.write("---")
        st.markdown("### 🕒 Chat History")
        
        if st.button("🆕 New Chat", use_container_width=True):
            if len(st.session_state.messages) > 0:
                first_msg = st.session_state.messages[0]["content"][:20] + "..."
                st.session_state.chat_history.append(first_msg)
            st.session_state.messages = []
            st.rerun()
            
        for past_chat in st.session_state.chat_history:
            st.markdown(f"💬 {past_chat}")

    # Welcome Premium Dashboard Screen
    if len(st.session_state.messages) == 0:
        st.markdown(f'<div class="greeting-text">Hi {st.session_state.user_name}</div>', unsafe_allow_html=True)
        st.markdown('<div class="subtitle-text">Where should we start?</div>', unsafe_allow_html=True)
        st.markdown('<div class="alliance-badge">Alliance Special Apple Engine Connected</div>', unsafe_allow_html=True)
        
        st.markdown("""
        <div style='margin-bottom: 25px; text-align: center;'>
            <span class='suggestion-btn'>🖼️ Create image</span>
            <span class='suggestion-btn'>🏏 Explore IPL Fan Zone</span>
            <span class='suggestion-btn'>📚 Help me learn</span>
            <span class='suggestion-btn'>✨ Boost my day</span>
            <span class='suggestion-btn'>📝 Write anything</span>
        </div>
        """, unsafe_allow_html=True)

    # Clean rendering of historical text blocks
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Photo Upload Panel
    uploaded_file = st.file_uploader("📷 Add image to prompt:", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
    image_payload = None
    if uploaded_file is not None:
        image_payload = Image.open(uploaded_file)
        st.image(image_payload, caption="Attached Image Asset", width=220)

    # Core Infinite Chat Component (Safe State Flow)
    if user_query := st.chat_input("Ask Aarambh AI..."):
        # Instant UI reflection
        with st.chat_message("user"):
            st.write(user_query)
        st.session_state.messages.append({"role": "user", "content": user_query})
        
        # Build contents dynamically
        contents_array = [user_query]
        if image_payload is not None:
            contents_array.append(image_payload)
            
        # Assistant Request & Display Block (No rerun triggers to prevent loops)
        with st.chat_message("assistant"):
            with st.spinner(""):
                try:
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=contents_array,
                        config=types.GenerateContentConfig(
                            system_instruction=system_instruction
                        )
                    )
                    st.write(response.text)
                    st.session_state.messages.append({"role": "assistant", "content": response.text})
                except Exception:
                    st.write("⚠️ Alliance Engine structural backup. Please resend the message.")
    
