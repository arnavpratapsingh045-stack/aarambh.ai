import streamlit as st
import requests

# 1. Page Configuration (Strictly Aarambh AI Branding)
st.set_page_config(page_title="Aarambh AI", layout="centered")

# 2. Live API Key Injection (Aapki nayi key direct lock kar di hai)
API_KEY = "AQ.Ab8RN6JhSvkPbTtvYdMeVEpvKOXhTEuFOFkVcAfXWOYA6150hg"

# 3. Strict Identity Rule
system_instruction = (
    "Aapka naam Aarambh AI hai. Aap exclusive Alliance Special Apple architecture par chalte hain. "
    "JAB BHI koi user aapse ye pooche ki 'aapko kisne banaya hai' ya aapke owner/creator kaun hain, "
    "tab aapko poore samman ke saath batana hai ki: 'Mujhe Alliance Group ki team ne milkar banaya hai aur Alliance Group ke CEO & Founder Mr. Arnav Partap Singh hain.' "
    "Kisi bhi haal mein Google ya Gemini ka naam bahaar nahi aana chahiye."
)

# 4. Initialize History (For Unlimited Chat)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 5. UI: Login & Signup Gate
if "user_name" not in st.session_state:
    st.subheader("Sign In / Access Portal")
    with st.form("login_form"):
        email = st.text_input("Enter your Email:")
        name = st.text_input("Enter your Name:")
        if st.form_submit_button("Access Engine"):
            if name.strip() and email.strip():
                st.session_state.user_name = name.strip()
                st.rerun()
            else:
                st.error("Kripya dono fields ko bharein.")
    st.stop()

# 6. Main Chat Console (Duniya ki har bhasha supported)
st.title("Aarambh AI")
st.write(f"Welcome back, **{st.session_state.user_name}** | Alliance Secure Network")

# History Display Layer
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat Input & Core REST Logic (Purely text-based, zero crash)
if prompt := st.chat_input("Ask Aarambh AI..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        # Stable endpoint that matches your new key structure perfectly
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
        headers = {"Content-Type": "application/json"}
        
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "systemInstruction": {"parts": [{"text": system_instruction}]}
        }
        
        try:
            # Post request execution
            response = requests.post(url, headers=headers, json=payload, timeout=30)
            response_json = response.json()
            
            # Extract content text block safely
            output_text = response_json['candidates'][0]['content']['parts'][0]['text']
            st.write(output_text)
            st.session_state.messages.append({"role": "assistant", "content": output_text})
        except Exception:
            st.error("Engine temporary busy. Please try resending your message.")
            
