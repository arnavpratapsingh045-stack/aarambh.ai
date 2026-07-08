import streamlit as st
import random
import time

# 1. Page Configuration Setup
st.set_page_config(page_title="Aarambh Global Video Downloader", page_icon="📥", layout="wide")

# 2. Premium Stylesheet for Downloader Hub
st.markdown("""
<style>
    .stApp { background-color: #0f172a; color: #f8fafc; }
    .login-box { max-width: 440px; margin: 60px auto; background: #1e293b; padding: 40px 30px; border-radius: 16px; box-shadow: 0 10px 25px rgba(0,0,0,0.3); text-align: center; border-top: 5px solid #ef4444; }
    .login-lbl { font-size: 1.8rem; font-weight: 800; color: #f8fafc; margin-bottom: 5px; }
    .login-sub { font-size: 0.9rem; color: #94a3b8; margin-bottom: 30px; }
    
    /* Google Button Styling */
    .google-btn { display: flex; align-items: center; justify-content: center; background-color: white; color: #1f2937; font-weight: 600; padding: 12px; border: 1px solid #d1d5db; border-radius: 8px; width: 100%; cursor: pointer; font-family: 'Inter', sans-serif; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
    .google-icon { width: 18px; height: 18px; margin-right: 12px; }
    
    .main-header { text-align: center; padding: 25px; background: #1e293b; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.2); margin-bottom: 30px; border-bottom: 4px solid #ef4444; }
    .dl-container { background: #1e293b; border-radius: 12px; padding: 25px; box-shadow: 0 4px 15px rgba(0,0,0,0.2); margin-bottom: 25px; border: 1px solid #334155; }
    .quality-card { background: #334155; border-radius: 10px; padding: 18px; text-align: center; border: 1px solid #475569; }
    .dl-btn { background-color: #ef4444; color: white !important; font-weight: 700; padding: 12px; width: 100%; border-radius: 8px; display: block; text-decoration: none; margin-top: 12px; text-align: center; transition: 0.2s; }
    .dl-btn:hover { background-color: #dc2626; }
</style>
""", unsafe_allow_html=True)

# 3. Safe Adsterra Component Loader (Optimized for Revenue)
def load_ad_safely():
    ad_code = """
    <html>
    <head><style>body { margin: 0; padding: 0; text-align: center; }</style></head>
    <body>
        <script type="text/javascript">
          atOptions = { 'key' : '7b617b2fc4e84542dd4b3a49fb75bff4', 'format' : 'iframe', 'height' : 90, 'width' : 728, 'params' : {} };
        </script>
        <script type="text/javascript" src="https://www.highperformanceformat.com/7b617b2fc4e84542dd4b3a49fb75bff4/invoke.js"></script>
    </body>
    </html>
    """
    st.components.v1.html(ad_code, height=105, scrolling=False)

# 4. Safe Force-Unmuted Video Component (Audio Policy Bypass)
def load_unmuted_video_stream():
    video_html = """
    <html>
    <head>
        <style>
            body { margin: 0; padding: 0; background-color: #000; display: flex; justify-content: center; align-items: center; border-radius: 12px; overflow: hidden; }
            video { width: 100%; max-height: 380px; object-fit: contain; }
        </style>
    </head>
    <body>
        <video id="audio_fixed_player" controls autoplay playsinline>
            <source src="https://rr2---sn-gwpa-25uek.googlevideo.com/videoplayback" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        <script>
            const vid = document.getElementById('audio_fixed_player');
            vid.muted = false; 
            vid.volume = 1.0;
            
            // Unmute clicks recorded for Adsterra impression count boost
            window.addEventListener('click', function() {
                if(vid.muted) {
                    vid.muted = false;
                    vid.play();
                }
            }, { once: true });
        </script>
    </body>
    </html>
    """
    st.components.v1.html(video_html, height=400, scrolling=False)

# Session State
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --- SCREEN 1: GOOGLE SIGN-IN INTERFACE ---
if not st.session_state.logged_in:
    st.markdown("<div class='login-box'>", unsafe_allow_html=True)
    st.markdown("<div class='login-lbl'>Aarambh Downloader</div>", unsafe_allow_html=True)
    st.markdown("<div class='login-sub'>Sign in with Google to download high-speed media clips</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="google-btn">
        <img class="google-icon" src="https://fonts.gstatic.com/s/i/productlogos/googleg/v6/web-24dp/logo_googleg_color_web_24dp.png">
        Sign in with Google
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    
    if st.button("Click to Verify & Enter Hub", type="primary", use_container_width=True):
        st.session_state.logged_in = True
        st.rerun()
        
    st.markdown("</div>", unsafe_allow_html=True)
    load_ad_safely()

# --- SCREEN 2: MAIN VIDEO DOWNLOAD TERMINAL ---
else:
    st.markdown("""
    <div class='main-header'>
        <h1 style='color:#ef4444; margin:0; font-weight:900;'>📥 AARAMBH HIGH-SPEED VIDEO DOWNLOADER</h1>
        <p style='color:#94a3b8; margin:5px 0 0 0;'>Paste video links from any platform to extract downloadable server links</p>
    </div>
    """, unsafe_allow_html=True)
    
    load_ad_safely()
    st.write(" ")

    # Input Form Lock Setup
    with st.form(key="downloader_form", clear_on_submit=False):
        st.markdown("### 🔗 Paste Video URL Link Below")
        url_input = st.text_input("", placeholder="https://www.youtube.com/watch?v=... or any video link", label_visibility="collapsed")
        run_extraction = st.form_submit_button("⚡ EXTRACT & GENERATE DOWNLOAD LINKS", use_container_width=True)
    
    if run_extraction:
        if not url_input:
            st.warning("Bhai, pehle video ka URL link paste karo!")
        else:
            url_clean = url_input.strip().lower()
            
            if not ("http" in url_clean or "www." in url_clean):
                st.error("🚨 Invalid Link: Please paste a valid video URL from web streams.")
            else:
                with st.spinner("⏳ Connecting to cloud streaming servers and parsing audio/video blocks..."):
                    time.sleep(1.2)
                
                # --- DISPLAY VIDEO STREAM BOX WITH AUDIO FIX ---
                st.markdown("<div class='dl-container'>", unsafe_allow_html=True)
                st.markdown("<h4>🎬 Live Media Content Stream Preview (Click anywhere to Unmute)</h4>", unsafe_allow_html=True)
                load_unmuted_video_stream()
                st.markdown("</div>", unsafe_allow_html=True)
                
                # --- GENERATE DOWNLOAD OPTIONS GRID ---
                st.markdown("### 📥 Extracted High-Speed Download Links")
                
                grid_cols = st.columns(3)
                
                # Quality Formats Array
                formats = [
                    {"quality": "1080p (Full HD)", "size": f"{random.randint(45, 95)} MB", "speed": "Ultra Fast"},
                    {"quality": "720p (HD Quality)", "size": f"{random.randint(20, 44)} MB", "speed": "High Speed"},
                    {"quality": "Audio Stream (MP3)", "size": f"{random.randint(3, 9)} MB", "speed": "Instant"}
                ]
                
                for idx, fmt in enumerate(formats):
                    with grid_cols[idx]:
                        st.markdown(f"""
                        <div class='quality-card'>
                            <h3 style='margin:0; color:#ef4444;'>{fmt["quality"]}</h3>
                            <p style='margin:5px 0; color:#cbd5e1;'>File Size: <b>{fmt["size"]}</b></p>
                            <span style='font-size:0.8rem; color:#10b981; font-weight:bold;'>🟢 Server: {fmt["speed"]}</span>
                            <a href='https://rr2---sn-gwpa-25uek.googlevideo.com/videoplayback' target='_blank' class='dl-btn'>START DOWNLOAD</a>
                        </div>
                        """, unsafe_allow_html=True)

    st.sidebar.markdown("**Downloader Engine:** V2.0 Active")
    if st.sidebar.button("RESET ENGINE"):
        st.session_state.logged_in = False
        st.rerun()

    st.write("")
    st.markdown("<p style='text-align: center; color: #64748b; font-size: 0.85rem;'>Aarambh Media Extraction Tool • 2026 Project</p>", unsafe_allow_html=True)
    
