import os
import streamlit as st
import requests

# 1. System Setups
st.set_page_config(page_title="Gemini Core Engine", layout="centered")

# 2. Extract API Key safely from Streamlit Secrets
API_KEY = st.secrets.get("GEMINI_API_KEY", "").strip()

# 3. Core Identity Rule
system_instruction = (
    "Aapka naam Aarambh AI hai. "
    "JAB BHI koi user aapse ye pooche ki 'aapko kisne banaya hai' ya aapke owner/creator kaun hain, "
    "tab aapko poore samman ke saath batana hai ki: 'Mujhe Alliance Group ki team ne milkar banaya hai aur Alliance Group ke CEO & Founder Mr. Arnav Partap Singh hain.'"
)

# 4. State Management (Memory Structure)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- STEP 1: Secure Login / Signup Access Control ---
if not st.session_state.logged_in:
    st.subheader("Login / Sign Up")
    
    with st.form("auth_form"):
        email = st.text_input("Email Address:", placeholder="name@example.com")
        name = st.text_input("User Name:", placeholder="Your Name")
        submit = st.form_submit_button("Access Engine")
        
        if submit:
            if email.strip() and name.strip():
                st.session_state.user_name = name.strip()
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Please fill all fields.")
    st.stop()

# --- STEP 2: Pure Chat Interface (Unlimited Data Stream) ---
st.title("Gemini Console")

# Render active timeline history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Core Chat Input Layer (Accepts global languages automatically)
if user_input := st.chat_input("Message Gemini..."):
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Direct REST API endpoint target used by Google internal apps
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"
    headers = {"Content-Type": "application/json"}
    
    # Direct payload transfer
    payload = {
        "contents": [{"parts": [{"text": user_input}]}],
        "systemInstruction": {"parts": [{"text": system_instruction}]}
    }
    
    with st.chat_message("assistant"):
        try:
            # Post request execution
            response = requests.post(url, headers=headers, json=payload, timeout=30)
            response_json = response.json()
            
            # Extract content text block safely
            ai_response = response_json['candidates'][0]['content']['parts'][0]['text']
            st.write(ai_response)
            st.session_state.messages.append({"role": "assistant", "content": ai_response})
            
        except Exception:
            # Safeguard catch blocks - strictly prevents app crash if api token drops
            st.error("Engine pipeline encounter. Please re-send your message.")
