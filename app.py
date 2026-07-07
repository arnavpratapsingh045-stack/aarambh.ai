import streamlit as st
import yt_dlp

# 1. Layout & Interface Settings
st.set_page_config(page_title="Aarambh Video Downloader", page_icon="☁️", layout="centered")

# 2. Advanced Premium SnapWC UI Styling
st.markdown("""
<style>
    .stApp { background: linear-gradient(180deg, #ffffff 0%, #f4f7fe 100%); color: #1e293b; }
    div[data-testid="stForm"] { border: none !important; padding: 0 !important; background-color: transparent !important; }
    p, span, label { color: #475569 !important; font-family: 'Inter', sans-serif; }
    
    /* Navbar styling */
    .header-container { display: flex; justify-content: space-between; align-items: center; padding: 15px 0; border-bottom: 1px solid #e2e8f0; margin-bottom: 30px; }
    .brand-logo { display: flex; align-items: center; gap: 10px; font-size: 1.6rem; font-weight: 800; color: #1d4ed8 !important; }
    .cloud-icon { font-size: 1.8rem; color: #2563eb; }
    
    /* Titles styling */
    .main-title { text-align: center; font-size: 2.3rem; font-weight: 900; background: linear-gradient(90deg, #1d4ed8 0%, #ea580c 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 5px; }
    .sub-title { text-align: center; font-size: 1.8rem; font-weight: 800; color: #1e3a8a !important; margin-top: 0px; margin-bottom: 25px; }
    .tagline { text-align: center; color: #64748b !important; font-size: 1rem; max-width: 550px; margin: 0 auto 35px auto; line-height: 1.5; }
    
    /* Primary Action Buttons */
    .stButton>button { background-color: #0066ff !important; color: white !important; font-size: 1.2rem !important; font-weight: 700 !important; border-radius: 14px !important; padding: 14px !important; border: none !important; width: 100% !important; box-shadow: 0 4px 15px rgba(0, 102, 255, 0.3); transition: 0.3s; }
    .stButton>button:hover { background-color: #0052cc !important; transform: translateY(-1px); }
    
    /* Output Stream Link Option Buttons */
    .dl-btn { display: block; text-align: center; background-color: #10b981 !important; color: white !important; font-size: 1.1rem !important; font-weight: 700 !important; border-radius: 12px !important; padding: 12px !important; text-decoration: none !important; margin-bottom: 12px; box-shadow: 0 4px 12px rgba(16, 185, 129, 0.2); transition: 0.3s; }
    .dl-btn:hover { background-color: #059669 !important; transform: translateY(-1px); }
    
    /* Dynamic UI Cards */
    .download-card { background-color: #ffffff; padding: 25px; border-radius: 16px; border: 1px solid #e2e8f0; box-shadow: 0 10px 25px rgba(0,0,0,0.04); margin-top: 25px; }
    
    /* Native Visual Ad Container Clone */
    .native-ad-box { background-color: #ffffff; padding: 20px; border-radius: 16px; border: 1px solid #e2e8f0; margin: 30px 0; display: flex; align-items: center; gap: 15px; position: relative; }
    .ad-badge { position: absolute; top: 10px; right: 15px; font-size: 0.65rem; background-color: #f1f5f9; padding: 2px 6px; border-radius: 4px; color: #94a3b8 !important; text-transform: uppercase; font-weight: 700; }
    .ad-icon { background-color: #eff6ff; width: 50px; height: 50px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; color: #2563eb; }
</style>
""", unsafe_allow_html=True)

# 3. Top Branding Bar
st.markdown("""
<div class='header-container'>
    <div class='brand-logo'>
        <span class='cloud-icon'>☁️</span> Aarambh Video Downloader
    </div>
    <div style='color: #475569; font-weight: 600; font-size: 0.95rem; border: 1px solid #cbd5e1; padding: 6px 12px; border-radius: 8px; background: white;'>🌐 English ▾</div>
</div>
""", unsafe_allow_html=True)

# 4. Hero Grid Headers
st.markdown("<div class='main-title'>Video, Thumbnails &</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Subtitles</div>", unsafe_allow_html=True)
st.markdown("<div class='tagline'>Download videos, Shorts, subtitles, transcripts and thumbnails online in HD up to 8K. Supports 10,000+ websites.</div>", unsafe_allow_html=True)

# 5. Core Operational Input Box
video_url = st.text_input("", placeholder="Please paste the video link or share URL here...", label_visibility="collapsed")

# Big Interactive Processing Trigger Action Button
download_trigger = st.button("🚀 Download Video")

if download_trigger and video_url:
    st.info("🔄 Aarambh Engine is processing network packets... Please wait.")
    
    # Fully Unrestricted Adult Network Core Configurations 
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
        'ignoreerrors': True,
        'nocheckcertificate': True,  # Bypass secure structural certificate requirements
        'prefer_insecure': True,      # Bypasses restricted cloud proxy validation blocks
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://google.com/'
        }
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            
            if info_dict is None:
                st.error("⚠️ Stream link error. Server rejected request or link is private.")
            else:
                video_title = info_dict.get('title', 'Aarambh_Media_File')
                formats = info_dict.get('formats', [])
                
                st.success(f"🎥 **Found:** {video_title[:50]}...")
                
                # Directly Render download links under input box area
                st.markdown("<div class='download-card'>", unsafe_allow_html=True)
                st.subheader("📥 Direct Resolution Options Available:")
                
                valid_formats = []
                for f in formats:
                    if f.get('url') and (f.get('height') or 'video' in str(f.get('format_note')).lower() or f.get('ext') == 'mp4'):
                        height = f.get('height', 'HD')
                        ext = f.get('ext', 'mp4')
                        download_link = f.get('url')
                        
                        label = f"Click Here to Download Video {height}p ({ext.upper()})"
                        if label not in [x['label'] for x in valid_formats]:
                            valid_formats.append({'label': label, 'url': download_link})
                
                if valid_formats:
                    # Give distinct colored buttons for each resolution found instantly
                    for stream in valid_formats[:4]:
                        st.markdown(f'<a href="{stream["url"]}" target="_blank" class="dl-btn">🔥 {stream["label"]}</a>', unsafe_allow_html=True)
                else:
                    direct_url = info_dict.get('url')
                    if direct_url:
                        st.markdown(f'<a href="{direct_url}" target="_blank" class="dl-btn">🔥 Download Best Available Stream</a>', unsafe_allow_html=True)
                    else:
                        st.error("Failed to parse file source. Refresh link and try again.")
                st.markdown("</div>", unsafe_allow_html=True)
                
    except Exception:
        st.error("⚠️ Core Engine timed out. Adult host network drop. Try refreshing the link stream.")

# 6. Supported details layout footer
st.markdown("<p style='text-align: center; font-size: 0.88rem; color: #64748b !important; margin-top:25px;'>Supports YouTube, TikTok, X (Twitter), Instagram, Facebook, xHamster, Pornhub and other popular sites worldwide.</p>", unsafe_allow_html=True)

# 🛠️ CLONED NATIVE AD GRID (Visual Ad Blocks for Professional Feel)
st.markdown("""
<div class='native-ad-box'>
    <div class='ad-badge'>Ad</div>
    <div class='ad-icon'>🌐</div>
    <div>
        <h4 style='margin:0; font-size:1rem; color:#1e293b;'>Aarambh Tool Suite - 100% Free Tools</h4>
        <p style='margin:2px 0 0 0; font-size:0.85rem; color:#64748b !important;'>Convert, compress, and edit media streams online natively in your web browser environment.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: #94a3b8 !important; font-size: 0.8rem; margin-top:50px;'>Alliance Secure Downloader Net • Powered by Aarambh Engine v2.0</p>", unsafe_allow_html=True)
