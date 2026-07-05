import os
import streamlit as st
from google import genai
from google.genai import types
from PIL import Image

# Page Configuration (Android, iPhone, Laptop sabhi ke liye perfect layout)
st.set_page_config(page_title="Aarambh AI", page_icon="🚀", layout="wide")

# Custom Styling (Alliance Group Colors & Premium Look)
st.markdown("""
    <style>
    .main-title { text-align: center; color: #FF4B4B; font-size: 36px; font-weight: bold; margin-bottom: 5px; }
    .sub-title { text-align: center; color: #555555; font-size: 16px; margin-bottom: 10px; font-style: italic; }
    .ceo-title { text-align: center; color: #D4AF37; font-size: 20px; font-weight: bold; margin-bottom: 25px; }
    .sidebar-text { font-size: 14px; font-weight: 500; }
    </style>
""", unsafe_allow_html=True)

# Streamlit Secrets se API Key automatic load karna
if "GEMINI_API_KEY" in st.secrets:
    os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]
elif "GOOGLE_API_KEY" in st.secrets:
    os.environ["GEMINI_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

# Client Initialize karna
client = genai.Client()

# AI ki internal programming (Kahin bhi Google/Gemini ka naam nahi aana chahiye)
system_instruction = (
    "Aapka naam 'Aarambh AI' hai. Aap exclusive 'Alliance Special Apple' architecture framework par bane hain. "
    "Aapke Owner, Creator aur Alliance Group ke CEO & Founder Mr. Arnav Partap Singh hain. "
    "Aap duniya ki sabhi bhashayein (Hindi, English, Spanish, French, etc.) samajhte aur bolte hain. "
    "Agar koi aapse aapke owner, creator, company ya model ke baare mein pooche, toh aapko hamesha Mr. Arnav Partap Singh aur Alliance Group ka hi naam lena hai. "
    "Aapko kisi bhi haal mein 'Google' ya 'Gemini' ka naam bahaar nahi lena hai. Aap poori tarah se Alliance Group ke hain."
)

# Sidebar Setup (Login Simulation & Chat History)
with st.sidebar:
    st.markdown("### 🔐 User Account")
    # First Step: Login display
    st.success("🟢 Logged in via Alliance Secure Port")
    st.markdown("**Welcome, Arnav!** 👋")
    st.write("---")
    
    st.markdown("### 🕒 Chat History")
    st.info("Aapki purani baatein yahan save ho rahi hain.")
    if st.button("🆕 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Main Screen Branding Display
st.markdown('<div class="main-title">🚀 Aarambh AI Active Ho Gaya Hai!</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">⚙️ Model Architecture: Alliance Special Apple</div>', unsafe_allow_html=True)
st.markdown('<div class="ceo-title">👑 Alliance Group ke CEO & Founder Mr. Arnav Partap Singh</div>', unsafe_allow_html=True)
st.write("---")

# Chat History Initialize karna
if "messages" not in st.session_state:
    st.session_state.messages = []

# Purane messages ko screen par render karna
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Multi-modal Feature: Photo Upload (+ Icon replacement)
uploaded_file = st.file_uploader("📷 Analyse karne ke liye koi photo upload karein (Optional):", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image for Alliance Engine", use_container_width=True)

# User se chat input lena (Global Language Supported)
if user_input := st.chat_input("Alliance Special Apple Engine se baat karein..."):
    # User message show karna
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # AI Generation Process
    try:
        contents_payload = [user_input]
        
        # Agar photo upload hui hai toh use payload mein jodna
        if uploaded_file is not None:
            contents_payload.append(image)
            
        with st.chat_message("assistant"):
            with st.spinner("Alliance Engine soch raha hai..."):
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
            st.error(f"❌ Server se response nahi mila. Kripya dobara koshish karein. Error: {e}")
