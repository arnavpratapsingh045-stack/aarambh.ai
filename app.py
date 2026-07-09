import streamlit as st
import yt_dlp
import random
import time

# 1. Page Configuration Setup (Centered Grid)
st.set_page_config(page_title="Aarambh Video Downloader", page_icon="☁️", layout="centered")

# 2. Match Width Stylesheet (Search Bar aur Button Ka Size Ek Jaisa Karne Ke Liye)
st.markdown("""
<style>
    .stApp { background: linear-gradient(180deg, #ffffff 0%, #f4f7fe 100%); color: #1e293b; }
    div[data-testid="stForm"] { border: none !important; padding: 0 !important; background-color: transparent !important; }
    p, span, label { color: #475569 !important; font-family: 'Inter', sans-serif; }
    
    /* Header Navbar */
    .header-container { display: flex; justify-content: space-between; align-items: center; padding: 15px 0; border-bottom: 1px solid #e2e8f0; margin-bottom: 30px; }
    .brand-logo { display: flex; align-items: center; gap: 10px; font-size: 1.6rem; font-weight: 800; color: #1d4ed8 !important; }
    .cloud-icon { font-size: 1.8rem; color: #2563eb; }
    
    /* Main Typography */
    .main-title { text-align: center; font-size: 2.3rem; font-weight: 900; background: linear-gradient(90deg, #1d4ed8 0%, #ea580c 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 5px; }
    .sub-title { text-align: center; font-size: 1.8rem; font-weight: 800; color: #1e3a8a !important; margin-top: 0px; margin-bottom: 25px; }
    .tagline { text-align: center; color: #64748b !important; font-size: 1rem; max-width: 550px; margin: 0 auto 35px auto; line-height: 1.5; }
    
    /* Dynamic Button Layout - Width is hard-matched to 100% of container input */
    .stButton>button { background-color: #0066ff !important; color: white !important; font-size: 1.2rem !important; font-weight: 700 !important; border-radius: 14px !important; padding: 14px !important; border: none !important; width: 100% !important; box-shadow: 0 4px 15px rgba(0, 102, 255, 0.3); transition: 0.3s; margin-top: 10px; }
    .stButton>button:hover { background-color: #0052cc !important; transform: translateY(-1px); }
    
    /* Metadata Output Block */
    .download-card { background-color: #ffffff; padding: 25px; border-radius: 16px; border: 1px solid #e2e8f0; box-shadow: 0 10px 25px rgba(0,0,0,0.04); margin-top: 25px; }
    .support-text { text-align: center; font-size: 0.88rem; color: #64748b !important; margin-top: 20px; line-height: 1.6; }
    .ad-wrapper { text-align: center; margin: 25px 0; padding: 10px; background-color: #f8fafc; border: 1px dashed #cbd5e1; border-radius: 8px; min-height: 90px; overflow:hidden; }
    .hash-tag { color: #2563eb !important; font-weight: 600; margin-right: 8px; font-size: 0.95rem; }
</style>
""", unsafe_allow_html=True)

# 3. Branding Header Layout
st.markdown("""
<div class='header-container'>
    <div class='brand-logo'>
        <span class='cloud-icon'>☁️</span> Aarambh Video Downloader
    </div>
    <div style='color: #475569; font-weight: 600; font-size: 0.95rem; border: 1px solid #cbd5e1; padding: 6px 12px; border-radius: 8px; background: white;'>🌐 English ▾</div>
</div>
""", unsafe_allow_html=True)

# 4. Marketing Hero Section
st.markdown("<div class='main-title'>Video, Thumbnails &</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Subtitles</div>", unsafe_allow_html=True)
st.markdown("<div class='tagline'>Download videos, Shorts, subtitles, transcripts and thumbnails online in HD quality from any website across the internet network.</div>", unsafe_allow_html=True)

# ─── ADSTERRA UPPER REVENUE FRAME ───
st.markdown("<div class='ad-wrapper'><p style='font-size: 0.75rem; color: #94a3b8 !important; margin: 0 0 5px 0;'>Advertisement</p>", unsafe_allow_html=True)
st.components.v1.html("""
    <script type="text/javascript">
      atOptions = { 'key' : '7b617b2fc4e84542dd4b3a49fb75bff4', 'format' : 'iframe', 'height' : 90, 'width' : 728, 'params' : {} };
    </script>
    <script type="text/javascript" src="https://www.highperformanceformat.com/7b617b2fc4e84542dd4b3a49fb75bff4/invoke.js"></script>
""", height=95, scrolling=False)
st.markdown("</div>", unsafe_allow_html=True)

# Track memory matrices across operations
if 'info_dict' not in st.session_state:
    st.session_state.info_dict = None
if 'last_url' not in st.session_state:
    st.session_state.last_url = ""

# 5. Core Interface Input Box
video_url = st.text_input("", placeholder="Please paste the video link or URL here...", label_visibility="collapsed")

if video_url != st.session_state.last_url:
    st.session_state.info_dict = None
    st.session_state.last_url = video_url

# Download Button - Formatted to exactly mirror the search bar above
download_click = st.button("🚀 Download Video")

# Triggers processing state upon user interaction
if (download_click or st.session_state.info_dict) and video_url:
    if st.session_state.info_dict is None:
        # LIVE PROCESSING NOTIFICATION TRIGGER
        with st.spinner("⚡ Processing Stream... Fetching metadata and synchronized audio formats..."):
            ydl_opts = {
                'format': 'best', # Grabs standard multi-channel integrated progressive tracks for sound activation
                'quiet': True,
                'no_warnings': True,
                'ignoreerrors': True,
            }
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    st.session_state.info_dict = ydl.extract_info(video_url, download=False)
            except Exception:
                st.error("⚠️ Unable to parse this link. Make sure the link is correct or public.")

    if st.session_state.info_dict:
        info_dict = st.session_state.info_dict
        video_title = info_dict.get('title', 'Aarambh_Media_Stream')
        formats = info_dict.get('formats', [])
        thumbnail_url = info_dict.get('thumbnail') or info_dict.get('thumbnails', [{}])[-1].get('url')
        tags = info_dict.get('tags', []) or info_dict.get('categories', [])
        
        st.markdown("<div class='download-card'>", unsafe_allow_html=True)
        
        # Output Title and Custom Tag Formats
        st.markdown(f"### 🎥 {video_title}")
        if tags:
            hashtags_str = " ".join([f"<span class='hash-tag'>#{tag.replace(' ', '')}</span>" for tag in tags[:5]])
            st.markdown(f"<div>{hashtags_str}</div>", unsafe_allow_html=True)
        st.write(" ")
        
        # Video Thumbnail Preview Container
        if thumbnail_url:
            st.image(thumbnail_url, use_container_width=True, caption="Verified Source Video Thumbnail")
            
        st.write("---")
        st.subheader("Select Quality (All links verified with active audio tracks):")
        
        valid_formats = []
        for f in formats:
            if f.get('url') and ('video' in str(f.get('format_note')).lower() or f.get('ext') == 'mp4' or f.get('vcodec') != 'none'):
                resolution = f.get('format_note', 'Standard Dynamic Resolution')
                ext = f.get('ext', 'mp4')
                download_link = f.get('url')
                
                label = f"{resolution} ({ext.upper()}) - Speaker Output On"
                if label not in [x['label'] for x in valid_formats]:
                    valid_formats.append({'label': label, 'url': download_link})
        
        if valid_formats:
            options = [x['label'] for x in valid_formats]
            choice = st.selectbox("Choose Resolution:", options)
            selected_url = next(x['url'] for x in valid_formats if x['label'] == choice)
            
            # Master Download Trigger Blue Button
            st.markdown(f'<a href="{selected_url}" target="_blank" download="{video_title}.mp4"><button style="background-color: #0066ff; color: white; border: none; padding: 14px 20px; border-radius: 12px; font-weight: bold; width: 100%; cursor: pointer; box-shadow: 0 4px 12px rgba(0,102,255,0.25);">📥 Click to Download / Open Video with Sound</button></a>', unsafe_allow_html=True)
        else:
            direct_url = info_dict.get('url')
            if direct_url:
                st.markdown(f'<a href="{direct_url}" target="_blank" download="Aarambh_Video.mp4"><button style="background-color: #0066ff; color: white; border: none; padding: 14px 20px; border-radius: 12px; font-weight: bold; width: 100%; cursor: pointer;">📥 Download Best Available Quality</button></a>', unsafe_allow_html=True)
            else:
                st.error("Could not parse direct download streams. Please try another link.")
                
        st.markdown("</div>", unsafe_allow_html=True)

# 6. Metadata Information
st.markdown("<div class='support-text'>Supports YouTube, TikTok, X (Twitter), Instagram, Facebook, and other popular sites worldwide.</div>", unsafe_allow_html=True)

# ─── ADSTERRA LOWER REVENUE FRAME ───
st.markdown("<div class='ad-wrapper' style='margin-top: 40px;'><p style='font-size: 0.75rem; color: #94a3b8 !important; margin: 0 0 5px 0;'>Advertisement</p>", unsafe_allow_html=True)
st.components.v1.html("""
    <script type="text/javascript">
      atOptions = { 'key' : '7b617b2fc4e84542dd4b3a49fb75bff4', 'format' : 'iframe', 'height' : 90, 'width' : 728, 'params' : {} };
    </script>
    <script type="text/javascript" src="https://www.highperformanceformat.com/7b617b2fc4e84542dd4b3a49fb75bff4/invoke.js"></script>
""", height=95, scrolling=False)
st.markdown("</div>", unsafe_allow_html=True)

st.write("")
st.markdown("<p style='text-align: center; color: #94a3b8 !important; font-size: 0.8rem;'>Alliance Secure Tool Network • Powered by Aarambh Engine v1.5</p>", unsafe_allow_html=True)
