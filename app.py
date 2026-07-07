import streamlit as st
import yt_dlp

# 1. Page Config Setup
st.set_page_config(page_title="Aarambh Video Downloader", page_icon="☁️", layout="centered")

# Google AdSense Meta Tag Verification (Direct UI Injection)
st.markdown("""
<head>
    <meta name="google-adsense-account" content="ca-pub-4760406725791226">
</head>
""", unsafe_allow_html=True)

# 2. Premium SnapWC Blue/White Theme UI Style
st.markdown("""
<style>
    .stApp { background: linear-gradient(180deg, #ffffff 0%, #f4f7fe 100%); color: #1e293b; }
    div[data-testid="stForm"] { border: none !important; padding: 0 !important; background-color: transparent !important; }
    p, span, label { color: #475569 !important; font-family: 'Inter', sans-serif; }
    
    /* Header Navbar */
    .header-container { display: flex; justify-content: space-between; align-items: center; padding: 15px 0; border-bottom: 1px solid #e2e8f0; margin-bottom: 30px; }
    .brand-logo { display: flex; align-items: center; gap: 10px; font-size: 1.6rem; font-weight: 800; color: #1d4ed8 !important; }
    .cloud-icon { font-size: 1.8rem; color: #2563eb; }
    
    /* Typography Style */
    .main-title { text-align: center; font-size: 2.3rem; font-weight: 900; background: linear-gradient(90deg, #1d4ed8 0%, #ea580c 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 5px; }
    .sub-title { text-align: center; font-size: 1.8rem; font-weight: 800; color: #1e3a8a !important; margin-top: 0px; margin-bottom: 25px; }
    .tagline { text-align: center; color: #64748b !important; font-size: 1rem; max-width: 550px; margin: 0 auto 35px auto; line-height: 1.5; }
    
    /* Core Action Big Blue Button */
    .stButton>button { background-color: #0066ff !important; color: white !important; font-size: 1.2rem !important; font-weight: 700 !important; border-radius: 14px !important; padding: 14px !important; border: none !important; width: 100% !important; box-shadow: 0 4px 15px rgba(0, 102, 255, 0.3); transition: 0.3s; margin-top: 10px; }
    .stButton>button:hover { background-color: #0052cc !important; transform: translateY(-1px); }
    
    /* Result Section Box */
    .download-card { background-color: #ffffff; padding: 25px; border-radius: 16px; border: 1px solid #e2e8f0; box-shadow: 0 10px 25px rgba(0,0,0,0.04); margin-top: 25px; }
    .support-text { text-align: center; font-size: 0.88rem; color: #64748b !important; margin-top: 20px; line-height: 1.6; }
    .ad-wrapper { text-align: center; margin: 25px 0; padding: 10px; background-color: #f8fafc; border: 1px dashed #cbd5e1; border-radius: 8px; min-height: 90px; }
</style>
""", unsafe_allow_html=True)

# 3. Top Navigation Header Bar
st.markdown("""
<div class='header-container'>
    <div class='brand-logo'>
        <span class='cloud-icon'>☁️</span> Aarambh Video Downloader
    </div>
    <div style='color: #475569; font-weight: 600; font-size: 0.95rem; border: 1px solid #cbd5e1; padding: 6px 12px; border-radius: 8px; background: white;'>🌐 English ▾</div>
</div>
""", unsafe_allow_html=True)

# 4. Main Banner Headings
st.markdown("<div class='main-title'>Video, Thumbnails &</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Subtitles</div>", unsafe_allow_html=True)
st.markdown("<div class='tagline'>Download videos, Shorts, subtitles, transcripts and thumbnails online in HD quality from any website across the internet network.</div>", unsafe_allow_html=True)

# ─── GOOGLE ADSENSE UPPER BANNER SLOT ───
st.markdown("""
<div class='ad-wrapper'>
    <p style='font-size: 0.75rem; color: #94a3b8 !important; margin: 0;'>Advertisement</p>
    <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-4760406725791226" data-ad-slot="XXXXXXXXXX" data-ad-format="auto" data-full-width-responsive="true"></ins>
    <script> (adsbygoogle = window.adsbygoogle || []).push({}); </script>
</div>
""", unsafe_allow_html=True)

# Initialize session states for stable processing
if 'info_dict' not in st.session_state:
    st.session_state.info_dict = None
if 'last_url' not in st.session_state:
    st.session_state.last_url = ""

# 5. Live Link Parser Input Box
video_url = st.text_input("", placeholder="Please paste the video link or URL here...", label_visibility="collapsed")

# Reset data if URL changes
if video_url != st.session_state.last_url:
    st.session_state.info_dict = None
    st.session_state.last_url = video_url

# Big Blue Download Button exactly below the link input box
download_click = st.button("🚀 Download Video")

# Process when button is clicked or if it's already processed for this URL
if (download_click or st.session_state.info_dict) and video_url:
    
    if st.session_state.info_dict is None:
        with st.spinner("⚡ Aarambh Engine Processing... Fetching available formats and qualities..."):
            ydl_opts = {
                'format': 'best',
                'quiet': True,
                'no_warnings': True,
                'ignoreerrors': True,
            }
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    st.session_state.info_dict = ydl.extract_info(video_url, download=False)
            except Exception:
                st.error("⚠️ Unable to parse this link. Make sure the link is correct or public.")

    # Render results if info_dict is active
    if st.session_state.info_dict:
        info_dict = st.session_state.info_dict
        video_title = info_dict.get('title', 'Aarambh_Media_Stream')
        formats = info_dict.get('formats', [])
        
        st.success(f"🎥 **Video Found:** {video_title[:60]}...")
        
        st.markdown("<div class='download-card'>", unsafe_allow_html=True)
        st.subheader("Select Quality to Download:")
        
        valid_formats = []
        for f in formats:
            if f.get('url') and (f.get('ext') == 'mp4' or 'video' in str(f.get('format_note')).lower()):
                resolution = f.get('format_note', 'Standard Quality')
                ext = f.get('ext', 'mp4')
                download_link = f.get('url')
                
                label = f"{resolution} ({ext.upper()})"
                if label not in [x['label'] for x in valid_formats]:
                    valid_formats.append({'label': label, 'url': download_link})
        
        # Original dropdown selector layout
        if valid_formats:
            options = [x['label'] for x in valid_formats]
            choice = st.selectbox("Choose Resolution:", options)
            
            selected_url = next(x['url'] for x in valid_formats if x['label'] == choice)
            
            st.markdown(f'<a href="{selected_url}" target="_blank"><button style="background-color: #0066ff; color: white; border: none; padding: 14px 20px; border-radius: 12px; font-weight: bold; width: 100%; cursor: pointer; box-shadow: 0 4px 12px rgba(0,102,255,0.25);">🚀 Click Here to Download / Open Video</button></a>', unsafe_allow_html=True)
        else:
            direct_url = info_dict.get('url')
            if direct_url:
                st.markdown(f'<a href="{direct_url}" target="_blank"><button style="background-color: #0066ff; color: white; border: none; padding: 14px 20px; border-radius: 12px; font-weight: bold; width: 100%; cursor: pointer;">🚀 Download Best Quality Available</button></a>', unsafe_allow_html=True)
            else:
                st.error("Could not parse direct download streams. Please try another link.")
                
        st.markdown("</div>", unsafe_allow_html=True)

# 6. Platforms Supported List Info
st.markdown("<div class='support-text'>Supports YouTube, TikTok, X (Twitter), Instagram, Facebook, and other popular sites worldwide.</div>", unsafe_allow_html=True)

# ─── GOOGLE ADSENSE LOWER BANNER SLOT ───
st.markdown("""
<div class='ad-wrapper' style='margin-top: 40px;'>
    <p style='font-size: 0.75rem; color: #94a3b8 !important; margin: 0;'>Advertisement</p>
    <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-4760406725791226" data-ad-slot="XXXXXXXXXX" data-ad-format="auto" data-full-width-responsive="true"></ins>
    <script> (adsbygoogle = window.adsbygoogle || []).push({}); </script>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")
st.markdown("<p style='text-align: center; color: #94a3b8 !important; font-size: 0.8rem;'>Alliance Secure Tool Network • Powered by Aarambh Engine v1.5</p>", unsafe_allow_html=True)
        
