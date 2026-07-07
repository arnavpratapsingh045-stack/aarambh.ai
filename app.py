import streamlit as st
import time

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
    .chat-bubble-ai { background-color: #1f2937; padding: 12px 16px; border-radius: 16px 16px 16px 0px; margin: 5px 0; text-align: left; display: inline-block; float: left; clear: both; border: 1px solid #374151; max-width: 80%; }
</style>
""", unsafe_content_rule=True)

# Session State को इनिशियलाइज करना (डेटा स्टोर रखने के लिए)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "messages" not in st.session_state:
    st.session_state.messages = []
if "username" not in st.session_state:
    st.session_state.username = "User"

# ---- POINT 1 & 2: LOGIN OR SIGNUP SCREEN ----
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align: center;'>AARAMBH AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #9ca3af; font-size: 0.9rem;'>The Next Generation AI Platform</p>", unsafe_allow_html=True)
    
    with st.container():
        st.write("---")
        # नाम इनपुट (डिफ़ॉल्ट रूप से आपका नाम सेट है)
        u_name = st.text_input("आपका नाम / Your Name", value="Arnav Partap Singh")
        
        # Google Email लॉगिन बटन का सिमुलेशन
        if st.button("🔴 Continue with Google Email"):
            if u_name.strip() != "":
                st.session_state.username = u_name
            st.session_state.logged_in = True
            st.rerun()
            
else:
    # ---- MAIN CHAT INTERFACE ----
    # POINT 3 & 2: Aarambh Engine Header & Welcome User Message
    st.markdown("<h1 style='margin-bottom:0px;'>Aarambh Engine</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='welcome-text'>Welcome {st.session_state.username}</p>", unsafe_allow_html=True)
    
    # चैट हिस्ट्री दिखाना
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"<div class='chat-bubble-user'>{msg['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='chat-bubble-ai'>{msg['content']}</div>", unsafe_allow_html=True)

    # स्पेसिंग के लिए खाली जगह
    st.write("")
    st.write("")

    # POINT 5: File/Photo Upload Option UI (+ Icon की जगह Streamlit Expander या file_uploader)
    with st.sidebar:
        st.markdown("### Aarambh Control Panel")
        uploaded_file = st.file_uploader("Upload Image/Media (+)", type=["png", "jpg", "jpeg", "mp4"])
        if uploaded_file is not None:
            st.success(f"Selected: {uploaded_file.name}")
        
        st.info("🎙️ Voice mic feature works natively via your keyboard's speech-to-text input inside the text box.")

    # POINT 4, 5, 7: Chat Input (सभी भाषाओं को सपोर्ट करता है)
    if user_query := st.chat_input("Ask Aarambh Engine anything..."):
        
        # यूजर का मैसेज स्क्रीन पर जोड़ें
        st.session_state.messages.append({"role": "user", "content": user_query})
        st.markdown(f"<div class='chat-bubble-user'>{user_query}</div>", unsafe_allow_html=True)
        
        # AI रिस्पॉन्स की प्रोसेसिंग लॉजिक
        clean_query = user_query.lower()
        ai_response = ""
        
        # POINT 6: Identity Filter (क्रिएटर की जानकारी पूछने पर)
        if any(x in clean_query for x in ["kisne banaya", "who created", "who made you", "creator", "owner", "founder"]):
            ai_response = "मुझे **Alliance Group** के **AI Technology Team** ने बनाया है। और Alliance Group के CEO & Founder **Arnav Partap Singh** हैं।"
        
        # POINT 8: Anti-Gemini Branding (नाम छिपाने के लिए)
        elif any(x in clean_query for x in ["gemini", "google"]):
            ai_response = "मैं **Aarambh AI** हूँ, जिसे **Aarambh Engine** द्वारा संचालित किया जाता है। मेरा संबंध किसी अन्य ब्रांड से नहीं है।"
            
        else:
            # यहाँ आपका लाइव AI मॉडल रिस्पॉन्स देगा (अभी के लिए मॉक रिस्पॉन्स सेट है)
            ai_response = f"यह 'Aarambh Engine' का सुरक्षित रिस्पॉन्स है। अनलिमिटेड चैट मोड चालू है। आपने पूछा: '{user_query}'"

        # AI का जवाब रेंडर करना
        time.sleep(0.5)  # रियल फील देने के लिए थोड़ा सा डिले
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
        st.markdown(f"<div class='chat-bubble-ai'>{ai_response}</div>", unsafe_allow_html=True)
        st.rerun()
    
