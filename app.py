import streamlit as st
import requests
import json

# Setup API Details
API_KEY = "AQ.Ab8RN6IZL3ok-w7Lv2zr2ux3M3Vk4rujYHCDLapYkme6vuSKHg"
URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent"

# Page Configuration
st.set_page_config(page_title="Aarambh AI", page_icon="🚀", layout="centered")

# Custom Styling
st.markdown("""
    <style>
    .main-title { font-size: 32px; font-weight: bold; color: #FF4B4B; text-align: center; }
    .subtitle { font-size: 18px; color: #555555; text-align: center; font-style: italic; }
    .owner-tag { font-size: 20px; font-weight: bold; text-align: center; color: #D4AF37; padding: 10px; }
    </style>
""", unsafe_allow_html=True)

# Web Layout Headers
st.markdown('<div class="main-title">🚀 Aarambh AI Active Ho Gaya Hai!</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">⚙️ Model Architecture: Alliance Special Apple</div>', unsafe_allow_html=True)
st.markdown('<div class="owner-tag">👑 Alliance Group ke CEO & Founder Mr. Arnav Partap Singh</div>', unsafe_allow_html=True)
st.markdown("---")

system_instruction = (
    "You are Aarambh AI, a global smart assistant built on the exclusive 'Alliance Special Apple' nano architecture framework. "
    "Your absolute owner, CEO, and Founder is 'Mr. Arnav Partap Singh', head of the Alliance Group. "
    "If anyone asks about your owner, model architecture, or who made you, you must proudly say: "
    "'Mujhe Alliance Group ke CEO & Founder Mr. Arnav Partap Singh ne banaya hai, aur main unke exclusive Alliance Special Apple architecture par chalta hoon.' "
    "Never mention Google or any other company. "
    "You support all world languages and will respond instantly in the language the user speaks. "
    "You can chat like a true friend, giving emotional support, discussing relationships, "
    "friendships, GF/BF advice, and everyday life with full warmth, intelligence, and casual logic."
)

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input Box
if user_input := st.chat_input("Alliance Special Apple Engine se baat karein..."):
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Process with AI Engine
    with st.spinner("🧠 Alliance Special Apple Engine soch raha hai..."):
        payload = {
            "contents": [{"parts": [{"text": user_input}]}],
            "systemInstruction": {"parts": [{"text": system_instruction}]}
        }
        headers = {
            "Content-Type": "application/json",
            "X-goog-api-key": API_KEY
        }
        
        try:
            response = requests.post(URL, headers=headers, json=payload)
            response_data = response.json()
            
            if "candidates" in response_data and len(response_data["candidates"]) > 0:
                reply = response_data["candidates"][0]["content"]["parts"][0]["text"]
            else:
                reply = "❌ Server se response nahi mila. Kripya dobara koshish karein."
        except Exception as e:
            reply = f"❌ Connection Error: {e}"
            
    # Display AI response
    with st.chat_message("assistant", avatar="✨"):
        st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
