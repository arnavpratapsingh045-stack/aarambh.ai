import streamlit as st
import yt_dlp

# 1. Page Config (Browser Title)
st.set_page_config(page_title="Aarambh Video Downloader", page_icon="☁️", layout="centered")

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
    
    /* Direct Download Buttons styling */
    .dl-btn { display: block; text-align: center; background-color: #0066ff !important; color: white !important; font-size: 1.05rem !important; font-weight: 700 !important; border-radius: 12px !important; padding: 12px !important; text-decoration: none !important; margin-bottom: 12px; box-shadow: 0 4px 12px rgba(0, 102, 255, 0.2); transition: 0.3s; }
    .dl-btn:hover { background-color: #0052cc !important; transform: translateY(-1px); }
    
    /* Result Cards */
    .download-card { background-color: #ffffff; padding: 25px; border-radius: 16px; border: 1px solid #e2e8f0; box-shadow: 0 10px 25px rgba(0,0,0,0.04); margin-top: 25px; }
    .support-text { text-align: center; font-size: 0.88rem; color: #64748b !important; margin-top: 20px; line-height: 1.6; }
    .ad-wrapper { text-align: center; margin: 25px 0; padding: 10px; background-color: #f8fafc; border: 1px dashed #cbd5e1; border-radius: 8px; min-height: 90px; }
</style>
""", unsafe_allow_html=True)

# 3. Top Navigation Header
st.markdown("""
<div class='header-container'>
    <div class='brand-logo'>
        <span class='cloud-icon'>☁️</span> Aarambh Video Downloader
    </div>
    <div style='color: #475569; font-weight: 600; font-size: 0.95rem; border: 1px solid #cbd5e1; padding: 6px 12px; border-radius: 8px; background: white;'>🌐 English ▾</div>
</div>
""", unsafe_allow_html=True)

# 4. Main Headings
st.markdown("<div class='main-title'>Video, Thumbnails &</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Subtitles</div>", unsafe_allow_html=True)
st.markdown("<div class='tagline'>Download high-speed viral content, standard media, and any web video from across the internet network. Clean, fast, and 100% free.</div>", unsafe_allow_html=True)

# ─── GOOGLE ADSENSE UPPER BANNER ───
st.markdown("""
<div class='ad-wrapper'>
    <p style='font-size: 0.75rem; color: #94a3b8 !important; margin: 0;'>Advertisement</p>
    <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-XXXXXXXXXXXXXXXX" data-ad-slot="XXXXXXXXXX" data-ad-format="auto" data-full-width-responsive="true"></ins>
    <script> (adsbygoogle = window.adsbygoogle || []).push({}); </script>
</div>
""", unsafe_allow_html=True)

# 5. Link Input Box
video_url = st.text_input("", placeholder="Please paste the video link or URL here...", label_visibility="collapsed")

if video_url:
    st.info("⚡ Aarambh Engine Processing... Fetching direct secure video endpoints.")
    
    # Advanced bypass configurations for adult sites, open links, and social platforms
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
        'ignoreerrors': True,
        # Fake a real desktop browser to prevent adult site firewalls from blocking
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
        }
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            
            if info_dict is None:
                st.error("⚠️ Stream error. Link is protected or restricted by the website host.")
            else:
                video_title = info_dict.get('title', 'Aarambh_Media_Stream')
                formats = info_dict.get('formats', [])
                
                st.success(f"🎬 **Media Connected:** {video_title[:60]}...")
                
                # Link ke bilkul niche direct download card layout
                st.markdown("<div class='download-card'>", unsafe_allow_html=True)
                st.subheader("📥 Direct Download Links Available:")
                
                valid_formats = []
                for f in formats:
                    # Collect and filter video qualities
                    if f.get('url') and ('video' in str(f.get('format_note')).lower() or f.get('height') or f.get('ext') == 'mp4'):
                        height = f.get('height', 'Standard')
                        ext = f.get('ext', 'mp4')
                        download_link = f.get('url')
                        
                        label = f"Download Video {height}p ({ext.upper()})"
                        if label not in [x['label'] for x in valid_formats]:
                            valid_formats.append({'label': label, 'url': download_link})
                
                # Dropdown hata kar, seedhe list format mein buttons de rahe hain
                if valid_formats:
                    # Sirf top 4 high qualities show karenge taaki page clutter na ho
                    for stream in valid_formats[:4]:
                        st.markdown(f'<a href="{stream["url"]}" target="_blank" class="dl-btn">🚀 {stream["label"]}</a>', unsafe_allow_html=True)
                else:
                    # Fallback Single link button if format filtering skips
                    direct_url = info_dict.get('url')
                    if direct_url:
                        st.markdown(f'<a href="{direct_url}" target="_blank" class="dl-btn">🚀 Download Best Quality (Direct Stream)</a>', unsafe_allow_html=True)
                    else:
                        st.error("Could not trace clean video endpoints. Try refreshing the link.")
                        
                st.markdown("</div>", unsafe_allow_html=True)
                
    except Exception:
        st.error("⚠️ Extraction timed out. Engine couldn't load the media target.")

# 6. Footer Info & Ads
st.markdown("<div class='support-text'>Supports YouTube, TikTok, X (Twitter), Instagram, Facebook, and all open web networks worldwide.</div>", unsafe_allow_html=True)

# ─── GOOGLE ADSENSE LOWER BANNER ───
st.markdown("""
<div class='ad-wrapper' style='margin-top: 40px;'>
    <p style='font-size: 0.75rem; color: #94a3b8 !important; margin: 0;'>Advertisement</p>
    <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-XXXXXXXXXXXXXXXX" data-ad-slot="XXXXXXXXXX" data-ad-format="auto" data-full-width-responsive="true"></ins>
    <script> (adsbygoogle = window.adsbygoogle || []).push({}); </script>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")
st.markdown("<p style='text-align: center; color: #94a3b8 !important; font-size: 0.8rem;'>Alliance Secure Tool Network • Powered by Aarambh Engine v1.8</p>", unsafe_allow_html=True)

