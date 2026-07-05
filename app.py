import os
import streamlit as st
from google import genai
from google.genai import types
from PIL import Image

# Page Configuration (Gemini App Look)
st.set_page_config(page_title="Aarambh AI", page_icon="✨", layout="centered")

# Custom CSS to mimic official clean look
st.markdown("""
    <style>
    .greeting-text { font-size: 38px; font-weight: 500; color: #1F1F1F; margin-bottom: 2px; font-family: sans-serif; }
    .subtitle-text { font-size: 32px; font-weight: 400; color: #757575; margin-bottom: 30px; font-family: sans-serif; }
    .suggestion-btn {
        display: inline-block; background-color: #F0F4F9; border-radius: 20px; 
        padding: 10px 20px; margin: 5px; font-size: 15px; color: #1F1F1F; 
        border: none; cursor: pointer; font-family: sans-serif; font-weight: 500;
    }
    .alliance-badge { font-size: 13px; color: #9E9E9E; text-align: center; margin-top: -10px; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# Secrets se API key setup
if "GEMINI_API_KEY" in st.secrets:
    os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]
elif "GOOGLE_API_KEY" in st.secrets:
    os.environ["GEMINI_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

client = genai.Client()

# System instruction strictly handling name prompts
system_instruction = (
    "Aapka naam 'Aarambh AI' hai. Aap exclusive 'Alliance Special Apple' architecture par chalte hain. "
    "Aapko normal conversation mein khud se baar-baar owner ka naam nahi lena hai. "
    "Lekin, JAB BHI koi user aapse aapke OWNER ya COMPANY ka naam pooche (jaise: aapke owner kaun hain, company kaun si hai), "
    "tab aapko poore samman ke saath batana hai ki aapke Owner 'Mr. Arnav Partap Singh' hain aur aap 'Alliance Group' ke hain. "
    "Kisi bhi haal mein 'Google' ya 'Gemini' ka naam bahaar nahi aana chahiye."
)

# Chat History Setup
if "messages" not in st.session_state:
    st.session_state.messages = []

# Top Gemini-style interface (Sirf tabhi dikhega jab chat khali ho)
if len(st.session_state.messages) == 0:
    st.markdown('<div class="greeting-text">Hi Arnav Partap</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle-text">Where should we start?</div>', unsafe_allow_html=True)
    st.markdown('<div class="alliance-badge">Alliance Special Apple Engine Active</div>', unsafe_allow_html=True)
    
    # Pill Suggestion UI elements from the screenshot
    st.markdown("""
    <div style='margin-bottom: 25px;'>
        <span class='suggestion-btn'>🖼️ Create image</span>
        <span class='suggestion-btn'>🏏 Explore IPL Fan Zone</span>
        <span class='suggestion-btn'>📚 Help me learn</span>
        <span class='suggestion-btn'>✨ Boost my day</span>
        <span class='suggestion-btn'>📝 Write anything</span>
    </div>
    """, unsafe_allow_html=True)

# Render existing chat logs
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Media uploader (Plus icon representation)
uploaded_file = st.file_uploader("📷 Add to prompt:", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Attached Media", width=250)

# Main Chat input box matching bottom bar query
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
            st.error(f"❌ Connection timeout. Try again. Error: {e}")
