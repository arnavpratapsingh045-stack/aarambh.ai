import os
import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
from gtts import gTTS
import base64

# Page Configuration (Sleek Gemini Format with Wide Sidebar)
st.set_page_config(page_title="Aarambh AI", page_icon="🚀", layout="centered")

# Custom Premium CSS Layout for Gemini Look, Audio & History UI
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

# System Instruction Configuration
system_instruction = (
    "Aapka naam 'Aarambh AI' hai. Aap exclusive 'Alliance Special Apple' architecture par chalte hain. "
    "Aapko normal conversation mein khud se baar-baar owner ka naam nahi lena hai. "
    "Lekin, JAB BHI koi user aapse aapke OWNER ya COMPANY ka naam pooche, "
    "tab aapko poore samman ke saath batana hai ki aapke Owner 'Mr. Arnav Partap Singh' hain aur aap 'Alliance Group' ke hain. "
    "Kisi bhi haal mein 'Google' ya 'Gemini' ka naam bahaar nahi aana chahiye. Aap poori tarah se Alliance Group ke hain."
)

# Audio Function to read text aloud for non-readers
def text_to_speech(text, lang='hi'):
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        tts.save("response.mp3")
        with open("response.mp3", "rb") as f:
            audio_bytes = f.read()
        st.audio(audio_bytes, format="audio/mp3")
        os.remove("response.mp3")
    except:
        pass

# Initialize session state variables
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 🔒 STEP 1: Secure Login Portal
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

# 🚀 STEP 2: Main Application Look
else:
    # 🕒 Chat History Sidebar Setup (Sleek Panel)
    with st.sidebar:
        st.markdown(f"### 👑 Alliance Portal")
        st.success(f"User: **{st.session_state.user_name}**")
        st.write("---")
        st.markdown("### 🕒 Chat History")
        
        if st.button("🆕 New Chat", use_container_width=True):
            if len(st.session_state.messages) > 0:
                # Save current conversation title to history bar
                first_msg = st.session_state.messages[0]["content"][:20] + "..."
                st.session_state.chat_history.append(first_msg)
            st.session_state.messages = []
            st.rerun()
            
        for past_chat in st.session_state.chat_history:
            st.markdown(f"💬 {past_chat}")
            
        st.write("---")
        if st.button("❌ Clear System Logs", use_container_width=True):
            st.session_state.messages = []
            st.session_state.chat_history = []
            st.rerun()

    # Welcome Splash (Only visible when chat stack is empty)
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

    # Render previous messages in the timeline
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
            if message["role"] == "assistant":
                # Audio player widget for past responses to help reading accessibility
                text_to_speech(message["content"])

    # Media integration upload box
    uploaded_file = st.file_uploader("📷 Add to prompt:", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Attached Media File", width=220)

    # 🎤 Advanced Voice Input Option (Mic Control Feature for Global Languages)
    st.markdown("##### 🎤 Speak your prompt (Global Audio Engine):")
    audio_value = st.audio_input("Record your question or instruction...")

    user_query = ""
    # Process text input from typing
    if type_input := st.chat_input("Ask Aarambh AI..."):
        user_query = type_input
    # Process audio transcription from the microphone widget
    elif audio_value is not None:
        with st.spinner("Processing Alliance Audio Speech Engine..."):
            try:
                # Direct multimodal processing of audio object
                audio_data = audio_value.read()
                audio_part = types.Part.from_bytes(data=audio_data, mime_type="audio/wav")
                
                transcribe_response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=["Understand and convert this spoken voice recording exactly into text format in its original spoken language.", audio_part]
                )
                user_query = transcribe_response.text.strip()
            except Exception as audio_err:
                st.error(f"⚠️ Audio processing mismatch. Kripya type karein. Error: {audio_err}")

    # Process final generated text payload
    if user_query:
        with st.chat_message("user"):
            st.write(user_query)
        st.session_state.messages.append({"role": "user", "content": user_query})
        
        try:
            contents_payload = [user_query]
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
                    # 🔊 Speaker Option: Play newly generated AI response right away
                    text_to_speech(response.text)
                    
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            
        except Exception as e:
            with st.chat_message("assistant"):
                st.error(f"❌ Connection timeout. Error: {e}")
