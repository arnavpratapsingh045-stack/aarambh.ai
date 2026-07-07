import streamlit as st
import yt_dlp
import os

# 1. Page Config & Premium Dark Mode Style (Aarambh Branding)
st.set_page_config(page_title="Aarambh Video Downloader", page_icon="📥", layout="centered")

st.markdown("""
<style>
    .stApp { background-color: #0b0f19; color: #f3f4f6; }
    h1 { color: #3b82f6 !important; font-weight: 800; text-align: center; }
    .download-card { background-color: #1f2937; padding: 20px; border-radius: 12px; border: 1px solid #374151; margin-top: 20px; }
    .stButton>button { background-color: #10b981; color: white; border-radius: 8px; width: 100%; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.title("📥 Aarambh Video Downloader")
st.markdown("<p style='text-align: center; color: #9ca3af;'>Paste any link (YT, FB, Insta, Browser) • Download High Quality</p>", unsafe_allow_html=True)

# 2. Input Layer
video_url = st.text_input("Enter Video Link here:", placeholder="https://...")

if video_url:
    st.info("🔄 Processing link... Fetching available formats and qualities...")
    
    # yt-dlp configurations
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            video_title = info_dict.get('title', 'Aarambh_Download')
            formats = info_dict.get('formats', [])
            
        st.success(f"🎥 **Video Found:** {video_title}")
        
        st.markdown("<div class='download-card'>", unsafe_allow_html=True)
        st.subheader("Select Quality to Download:")
        
        valid_formats = []
        for f in formats:
            if f.get('url') and (f.get('ext') == 'mp4' or 'video' in str(f.get('format_note'))):
                resolution = f.get('format_note', 'Standard Quality')
                ext = f.get('ext', 'mp4')
                download_link = f.get('url')
                
                label = f"{resolution} ({ext.upper()})"
                if label not in [x['label'] for x in valid_formats]:
                    valid_formats.append({'label': label, 'url': download_link})
        
        if valid_formats:
            options = [x['label'] for x in valid_formats]
            choice = st.selectbox("Choose Resolution:", options)
            
            selected_url = next(x['url'] for x in valid_formats if x['label'] == choice)
            
            st.markdown(f'<a href="{selected_url}" target="_blank"><button style="background-color: #2563eb; color: white; border: none; padding: 12px 20px; border-radius: 8px; font-weight: bold; width: 100%; cursor: pointer;">🚀 Click Here to Download / Open Video</button></a>', unsafe_allow_html=True)
        else:
            direct_url = info_dict.get('url')
            if direct_url:
                st.markdown(f'<a href="{direct_url}" target="_blank"><button style="background-color: #2563eb; color: white; border: none; padding: 12px 20px; border-radius: 8px; font-weight: bold; width: 100%; cursor: pointer;">🚀 Download Best Quality Available</button></a>', unsafe_allow_html=True)
            else:
                st.error("Could not parse direct download streams. Please try another link.")
                
        st.markdown("</div>", unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"⚠️ Unable to parse this link. Make sure the link is correct or public.")

st.write("")
st.write("")
st.markdown("<p style='text-align: center; color: #4b5563; font-size: 0.8rem;'>Alliance Secure Downloader Engine v1.0</p>", unsafe_allow_html=True)
    
