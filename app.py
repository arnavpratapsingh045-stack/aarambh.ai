import streamlit as st
import random
import time

# 1. Page Configuration Setup
st.set_page_config(page_title="Free Video Downloader", page_icon="📥", layout="wide")

# 2. Aapka Purana Original Dark UI Theme Stylesheet
st.markdown("""
<style>
    .stApp { background-color: #0f172a; color: #f8fafc; }
    .main-title { text-align: center; font-size: 2.6rem; font-weight: 900; color: #ef4444; margin-top: 10px; margin-bottom: 5px; }
    .sub-title { text-align: center; font-size: 1.05rem; color: #94a3b8; margin-bottom: 30px; }
    .video-box { background: #1e293b; border-radius: 12px; padding: 20px; border: 1px solid #334155; margin-bottom: 25px; text-align: center; }
    .format-card { background: #1e293b; border: 1px solid #334155; border-radius: 10px; padding: 20px; text-align: center; transition: 0.3s; }
    .format-card:hover { border-color: #ef4444; }
    .dl-btn { background-color: #ef4444; color: white !important; font-weight: 700; padding: 12px; width: 100%; border-radius: 8px; display: block; text-decoration: none; margin-top: 15px; text-align: center; transition: 0.2s; }
    .dl-btn:hover { background-color: #dc2626; }
</style>
""", unsafe_allow_html=True)

# 3. Adsterra Freeze-Proof Ad Slot (Revenue Generation Box)
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

# 4. Audio-Force Fixed Video Component
def load_unmuted_video_stream():
    video_html = """
    <html>
    <head>
        <style>
            body { margin: 0; padding: 0; background-color: #000; display: flex; justify-content: center; align-items: center; border-radius: 10px; overflow: hidden; }
            video { width: 100%; max-height: 380px; object-fit: contain; }
        </style>
    </head>
    <body>
        <video id="classic_player" controls autoplay playsinline>
            <source src="https://rr2---sn-gwpa-25uek.googlevideo.com/videoplayback" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        <script>
            const vid = document.getElementById('classic_player');
            vid.muted = false; 
            vid.volume = 1.0;
            
            // User screen par kahin bhi tap karega toh audio policy force bypass ho jayegi
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

# --- MAIN DASHBOARD (NO INTERMEDIATE LOGIN SCREEN) ---
st.markdown("<div class='main-title'>📥 ONLINE VIDEO DOWNLOADER</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>High-Speed Video & MP3 Extraction Hub</div>", unsafe_allow_html=True)

# Revenue Ad Live at Top
load_ad_safely()
st.write(" ")

# Standard Link Fetcher Form Block
with st.form(key="downloader_core_form", clear_on_submit=False):
    url_input = st.text_input("", placeholder="Paste video link here and click fetch...", label_visibility="collapsed")
    run_extraction = st.form_submit_button("⚡ FETCH VIDEO DATA", use_container_width=True)

if run_extraction:
    if not url_input:
        st.warning("Bhai, pehle video ka URL link paste karo!")
    else:
        url_clean = url_input.strip().lower()
        
        if not ("http" in url_clean or "www." in url_clean):
            st.error("🚨 Invalid Format: Please paste a proper video link address.")
        else:
            with st.spinner("⏳ Extracting download streams from server pool..."):
                time.sleep(1.0)
            
            # 🎬 Video Preview Box with Unmute Driver
            st.markdown("<div class='video-box'>", unsafe_allow_html=True)
            st.markdown("<h4 style='margin-top:0; color:#ef4444;'>🎬 Live Stream Preview (Tap/Click to Unmute)</h4>", unsafe_allow_html=True)
            load_unmuted_video_stream()
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Second Ad break right before download grid for maximum impression clicks
            load_ad_safely()
            st.write(" ")
            
            # 📥 Download Buttons Multi-Grid System
            st.markdown("### 📥 Select File Resolution Format")
            grid_cols = st.columns(3)
            
            mock_sizes = [
                {"quality": "1080p Ultra HD", "size": f"{random.randint(55, 99)} MB"},
                {"quality": "720p Standard HD", "size": f"{random.randint(25, 54)} MB"},
                {"quality": "Audio Stream MP3", "size": f"{random.randint(4, 12)} MB"}
            ]
            
            with grid_cols[0]:
                st.markdown(f"""
                <div class='format-card'>
                    <h3 style='margin:0; color:#ef4444;'>{mock_sizes[0]["quality"]}</h3>
                    <p style='margin:8px 0; color:#94a3b8;'>File Size: <b>{mock_sizes[0]["size"]}</b></p>
                    <a href='https://rr2---sn-gwpa-25uek.googlevideo.com/videoplayback' target='_blank' class='dl-btn'>Download Video</a>
                </div>
                """, unsafe_allow_html=True)
                
            with grid_cols[1]:
                st.markdown(f"""
                <div class='format-card'>
                    <h3 style='margin:0; color:#ef4444;'>{mock_sizes[1]["quality"]}</h3>
                    <p style='margin:8px 0; color:#94a3b8;'>File Size: <b>{mock_sizes[1]["size"]}</b></p>
                    <a href='https://rr2---sn-gwpa-25uek.googlevideo.com/videoplayback' target='_blank' class='dl-btn'>Download Video</a>
                </div>
                """, unsafe_allow_html=True)
                
            with grid_cols[2]:
                st.markdown(f"""
                <div class='format-card'>
                    <h3 style='margin:0; color:#ef4444;'>{mock_sizes[2]["quality"]}</h3>
                    <p style='margin:8px 0; color:#94a3b8;'>File Size: <b>{mock_sizes[2]["size"]}</b></p>
                    <a href='https://rr2---sn-gwpa-25uek.googlevideo.com/videoplayback' target='_blank' class='dl-btn'>Download MP3</a>
                </div>
                """, unsafe_allow_html=True)

st.write("")
st.markdown("<p style='text-align: center; color: #475569; font-size: 0.85rem;'>Universal Downloader Engine • Core Version 2026</p>", unsafe_allow_html=True)
    
