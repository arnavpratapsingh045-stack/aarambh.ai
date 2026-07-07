import streamlit as st
import time
import google.generativeai as genai
from PIL import Image

# 1. API SETUP (Asli Engine Connection)
API_KEY = "AQ.Ab8RN6JhSvkPbTtvYdMeVEpvKOXhTEuFOFkVcAfXWOYA6150hg"
genai.configure(api_key=API_KEY)

system_instruction = (
    "Aapka naam Aarambh AI hai. Aap exclusive Alliance Special Apple architecture par chalte hain. "
    "JAB BHI koi user aapse ye pooche ki 'aapko kisne banaya hai' ya aapke owner/creator kaun hain, "
    "tab aapko poore samman ke saath batana hai ki: 'Mujhe Alliance Group ki team ne milkar banaya hai aur Alliance Group ke CEO & Founder Mr. Arnav Partap Singh hain.' "
    "Kisi bhi haal mein Google ya Gemini ka naam bahaar nahi aana chahiye."
)
model = genai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction=system_instruction)

# पेज की शुरुआती सेटिंग्स
st.set_page_config(
    page_title="Aarambh AI", 
    page_icon="🤖", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS ताकि UI मॉडर्न और क्लीन दिखे
st.markdown("""
<style>
    .stApp { background-color: #0b0f19; color: #f3f4f6; }
    h1 { color: #3b82f6 !important; font-weight: 800; letter-spacing: 0.05em; }
    .stButton>button { background-color: #2563eb; color: white; border-radius: 12px; font-weight: 600; width: 100%; border: none; padding: 0.5rem; transition: 0.3s; }
    .stButton>button:hover { background-color: #1d4ed8; border: none; }
    .welcome-text { color: #10b981; font-weight: 500; font-size: 0.85rem; margin-top: -10px; margin-bottom: 20px; }
    .chat-bubble-user { background-color: #2563eb; padding: 12px 16px; border-radius: 16px 16px 0px 16px; margin: 5px 0; text-align: right; display: inline-block; float: right; clear: both; max-width: 80%; }
    .chat-bubble-ai { background-color: #1f2937; padding: 12px 16px; border-radius: 16px 16px 16px 0px; margin: 5px 0; text-align: left; display: inline-block; float: left; clear: both; border: 1px solid #374151; max-width: 80%; line-height: 1.5; }
</style>
""", unsafe_allow_html=True)

# Session State को इनिशियलाइज करना
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "messages" not in st.session_state:
    st.session_state.messages = []
if "username" not in st.session_state:
    st.session_state.username = "User"
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# ---- LOGIN SCREEN ----
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align: center;'>AARAMBH AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #9ca3af; font-size: 0.9rem;'>The Next Generation AI Platform</p>", unsafe_allow_html=True)
    
    with st.container():
        st.write("---")
        u_name = st.text_input("आपका नाम / Your Name", value="Arnav Partap Singh")
        
        if st.button("🔴 Continue with Secure Network"):
            if u_name.strip() != "":
                st.session_state.username = u_name
            st.session_state.logged_in = True
            st.rerun()
            
else:
    # ---- MAIN CHAT INTERFACE ----
    st.markdown("<h1 style='margin-bottom:0px;'>Aarambh Engine</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='welcome-text'>Welcome back, {st.session_state.username}</p>", unsafe_allow_html=True)
    
    # चैट हिस्ट्री दिखाना (UI Bubbles)
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"<div class='chat-bubble-user'>{msg['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='chat-bubble-ai'>{msg['content']}</div>", unsafe_allow_html=True)

    st.write("")
    st.write("")

    # Control Panel (Sidebar)
    with st.sidebar:
        st.markdown("### Aarambh Control Panel")
        uploaded_file = st.file_uploader("Upload Image (+)", type=["png", "jpg", "jpeg"])
        if uploaded_file is not None:
            st.success(f"Selected: {uploaded_file.name}")
        
        st.info("🎙️ Voice mic feature works natively via your keyboard's speech-to-text input inside the text box.")

    # Chat Input & Real AI Logic
    if user_query := st.chat_input("Ask Aarambh Engine anything..."):
        
        # User message UI update
        st.session_state.messages.append({"role": "user", "content": user_query})
        
        # API Connection
        ai_response = ""
        try:
            # Agar sidebar se photo upload ki gayi hai
            if uploaded_file is not None:
                img = Image.open(uploaded_file)
                response = st.session_state.chat_session.send_message([user_query, img])
            else:
                # Sirf text message
                response = st.session_state.chat_session.send_message(user_query)
                
            ai_response = response.text
        except Exception as e:
            ai_response = "⚠️ Engine Network Busy. Please retry your message."

        # AI response UI update
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
        st.rerun()
    
