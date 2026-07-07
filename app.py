import streamlit as st
import google.generativeai as genai

# 1. API Configuration & Secure Hardlocked Key
API_KEY = "AQ.Ab8RN6JhSvkPbTtvYdMeVEpvKOXhTEuFOFkVcAfXWOYA6150hg"
genai.configure(api_key=API_KEY)

# Strict Identity Rules
system_instruction = (
    "Aapka naam Aarambh AI hai. Aap exclusive Alliance Special Apple architecture par chalte hain. "
    "JAB BHI koi user aapse ye pooche ki 'aapko kisne banaya hai' ya aapke owner/creator kaun hain, "
    "tab aapko poore samman ke saath batana hai ki: 'Mujhe Alliance Group ki team ne milkar banaya hai aur Alliance Group ke CEO & Founder Mr. Arnav Partap Singh hain.' "
    "Kisi bhi haal mein Google ya Gemini ka naam bahaar nahi aana chahiye."
)

# Initialize Model Engine Safely
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash", 
    system_instruction=system_instruction
)

# 2. पेज की शुरुआती सेटिंग्स
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
    
    /* Native Chat Alignment fixes to prevent styling breaking during streams */
    .stChatMessage { background-color: transparent !important; border: none !important; }
    .chat-bubble-user { background-color: #2563eb; padding: 12px 16px; border-radius: 16px 16px 0px 16px; color: white; text-align: left; display: inline-block; max-width: 100%; }
    .chat-bubble-ai { background-color: #1f2937; padding: 12px 16px; border-radius: 16px 16px 16px 0px; color: #f3f4f6; text-align: left; display: inline-block; border: 1px solid #374151; max-width: 100%; line-height: 1.5; }
</style>
""", unsafe_allow_html=True)

# Session State को इनिशियलाइज करना
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
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
        
        if st.button("🔴 Continue with Alliance Secure Network"):
            if u_name.strip() != "":
                st.session_state.username = u_name
            st.session_state.logged_in = True
            st.rerun()
            
else:
    # ---- MAIN CHAT INTERFACE ----
    st.markdown("<h1 style='margin-bottom:0px;'>Aarambh Engine</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='welcome-text'>Welcome back, {st.session_state.username}</p>", unsafe_allow_html=True)
    
    # चैट हिस्ट्री दिखाना (Render directly from the official active chat session history)
    for msg in st.session_state.chat_session.history:
        role_class = "chat-bubble-user" if msg.role == "user" else "chat-bubble-ai"
        with st.chat_message(msg.role):
            st.markdown(f"<div class='{role_class}'>{msg.parts[0].text}</div>", unsafe_allow_html=True)

    # Control Panel (Sidebar)
    with st.sidebar:
        st.markdown("### Aarambh Control Panel")
        st.info("🎙️ Voice mic feature works natively via your keyboard's speech-to-text input inside the text box.")
        if st.button("🗑️ Clear Chat History", use_container_width=True):
            st.session_state.chat_session = model.start_chat(history=[])
            st.rerun()

    # Chat Input & Core Official Engine Logic (No loops, zero crash)
    if user_query := st.chat_input("Ask Aarambh Engine anything..."):
        
        # Display user message instantly
        with st.chat_message("user"):
            st.markdown(f"<div class='chat-bubble-user'>{user_query}</div>", unsafe_allow_html=True)
        
        # Process and Stream AI output natively
        with st.chat_message("assistant"):
            try:
                response = st.session_state.chat_session.send_message(user_query)
                st.markdown(f"<div class='chat-bubble-ai'>{response.text}</div>", unsafe_allow_html=True)
            except Exception:
                st.markdown("<div class='chat-bubble-ai'>⚠️ Connection temporary reset. Please resend your message.</div>", unsafe_allow_html=True)
        
        st.rerun()
            
