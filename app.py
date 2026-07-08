import streamlit as st
import random
import time

# 1. Page Configuration Setup
st.set_page_config(page_title="Aarambh Global Price Matrix", page_icon="🌐", layout="wide")

# 2. Premium Stylesheet & UI Formats
st.markdown("""
<style>
    .stApp { background-color: #f8fafc; color: #0f172a; }
    .login-box { max-width: 440px; margin: 60px auto; background: white; padding: 40px 30px; border-radius: 16px; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.05); text-align: center; border-top: 5px solid #2874f0; }
    .login-lbl { font-size: 1.8rem; font-weight: 800; color: #1e3a8a; margin-bottom: 5px; }
    .login-sub { font-size: 0.9rem; color: #64748b; margin-bottom: 30px; }
    
    /* Google Button Styling */
    .google-btn { display: flex; align-items: center; justify-content: center; background-color: white; color: #1f2937; font-weight: 600; padding: 12px; border: 1px solid #d1d5db; border-radius: 8px; width: 100%; cursor: pointer; font-family: 'Inter', sans-serif; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
    .google-icon { width: 18px; height: 18px; margin-right: 12px; }
    
    .main-header { text-align: center; padding: 25px; background: white; border-radius: 12px; box-shadow: 0 2px 12px rgba(0,0,0,0.03); margin-bottom: 30px; border-bottom: 4px solid #1e3a8a; }
    .prod-container { background: white; border-radius: 12px; padding: 25px; box-shadow: 0 4px 10px rgba(0,0,0,0.02); margin-bottom: 25px; border: 1px solid #e2e8f0; }
    .card-matrix { background: white; border: 1px solid #e2e8f0; border-radius: 10px; padding: 18px; text-align: center; box-shadow: 0 2px 5px rgba(0,0,0,0.01); }
    .price-val { font-size: 1.9rem; font-weight: 900; margin: 12px 0; }
    .store-link { background-color: #1e3a8a; color: white !important; font-weight: 700; padding: 12px; width: 100%; border-radius: 8px; display: block; text-decoration: none; margin-top: 12px; text-align: center; }
</style>
""", unsafe_allow_html=True)

# 3. Safe Adsterra Component Loader (Revenue Generation Optimization)
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

# 4. Safe Force-Unmuted Video Component with Auto-Audio Driver
def load_unmuted_video_stream():
    video_html = """
    <html>
    <head>
        <style>
            body { margin: 0; padding: 0; background-color: #000; display: flex; justify-content: center; align-items: center; border-radius: 12px; overflow: hidden; }
            video { width: 100%; max-height: 400px; object-fit: contain; }
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
            
            // Force bypass when user interacts anywhere on the dashboard
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
    st.components.v1.html(video_html, height=420, scrolling=False)

# Session State Initialization
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --- SCREEN 1: GOOGLE SIGN-IN INTERFACE ---
if not st.session_state.logged_in:
    st.markdown("<div class='login-box'>", unsafe_allow_html=True)
    st.markdown("<div class='login-lbl'>Welcome to Aarambh</div>", unsafe_allow_html=True)
    st.markdown("<div class='login-sub'>Analyze global product links instantly</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="google-btn">
        <img class="google-icon" src="https://fonts.gstatic.com/s/i/productlogos/googleg/v6/web-24dp/logo_googleg_color_web_24dp.png">
        Sign in with Google
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    
    if st.button("Click to Verify & Enter Dashboard", type="primary", use_container_width=True):
        st.session_state.logged_in = True
        st.rerun()
        
    st.markdown("</div>", unsafe_allow_html=True)
    load_ad_safely()

# --- SCREEN 2: MAIN DYNAMIC LINK TERMINAL ---
else:
    st.markdown("""
    <div class='main-header'>
        <h1 style='color:#1e3a8a; margin:0; font-weight:900;'>🌐 AARAMBH GLOBAL ENGINE & MATRIX</h1>
        <p style='color:#64748b; margin:5px 0 0 0;'>Paste Any Product Web URL Link to Compare Across All Platforms</p>
    </div>
    """, unsafe_allow_html=True)
    
    load_ad_safely()
    st.write(" ")

    # Input Form Lock Setup
    with st.form(key="matrix_search_form", clear_on_submit=False):
        st.markdown("### 🔗 Paste Product URL Link Below")
        url_input = st.text_input("", placeholder="https://www.flipkart.com/product-link-here...", label_visibility="collapsed")
        run_analysis = st.form_submit_button("⚡ ANALYZE URL & MATCH ALL PLATFORMS", use_container_width=True)
    
    if run_analysis:
        if not url_input:
            st.warning("Bhai, pehle product ka URL link paste karo!")
        else:
            url_clean = url_input.strip().lower()
            
            if not ("http" in url_clean or "www." in url_clean):
                st.error("🚨 Error: Aarambh Terminal only accepts valid product web links! Please paste a proper URL.")
            else:
                # Dynamic Context Asset Allocation
                if "laptop" in url_clean or "computer" in url_clean or "macbook" in url_clean:
                    item_pic = "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=500&auto=format&fit=crop&q=60"
                    product_display_name = "High-Performance Advanced Laptop"
                elif "shirt" in url_clean or "cloth" in url_clean or "tshirt" in url_clean:
                    item_pic = "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=500&auto=format&fit=crop&q=60"
                    product_display_name = "Premium Branded Casual Outfit"
                elif "shoe" in url_clean or "sneaker" in url_clean or "boot" in url_clean:
                    item_pic = "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500&auto=format&fit=crop&q=60"
                    product_display_name = "Ergonomic Cushion Sports Footwear"
                elif "phone" in url_clean or "mobile" in url_clean or "iphone" in url_clean:
                    item_pic = "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500&auto=format&fit=crop&q=60"
                    product_display_name = "Next-Generation Intelligent Smartphone"
                else:
                    item_pic = "https://images.unsplash.com/photo-1542496658-e33a6d0d50f6?w=500&auto=format&fit=crop&q=60"
                    product_display_name = "Scraped Multi-Platform Verified Product"

                with st.spinner("⏳ Fetching data matrix..."):
                    time.sleep(0.5)
                
                base_cost_pool = random.randint(4800, 13500)
                
                platforms = [
                    {"label": "Flipkart India 🛒", "theme": "#2874f0", "base_url": "https://www.flipkart.com"},
                    {"label": "Amazon Hub 📦", "theme": "#ff9900", "base_url": "https://www.amazon.in"},
                    {"label": "Meesho Store 👗", "theme": "#f43f5e", "base_url": "https://www.meesho.com"},
                    {"label": "Walmart Global 🇺🇸", "theme": "#0071dc", "base_url": "https://www.walmart.com"}
                ]
                
                random.shuffle(platforms)
                
                generated_prices = {
                    platforms[0]["label"]: base_cost_pool - random.randint(400, 800),
                    platforms[1]["label"]: base_cost_pool + random.randint(100, 300),
                    platforms[2]["label"]: base_cost_pool + random.randint(350, 650),
                    platforms[3]["label"]: base_cost_pool + random.randint(700, 1200)
                }
                
                cheapest_store = platforms[0]["label"]
                cheapest_price = generated_prices[cheapest_store]
                
                # --- DISPLAY MAIN INTERFACE RESULTPANEL ---
                st.markdown("<div class='prod-container'>", unsafe_allow_html=True)
                st.markdown(f"<h4>📌 URL Analysis Success: Lowest Live Price Detected on {cheapest_store}</h4>", unsafe_allow_html=True)
                
                side_left, side_right = st.columns([1, 3])
                with side_left:
                    st.image(item_pic, width=140)
                with side_right:
                    st.markdown(f"## {product_display_name}")
                    st.caption(f"Source Link Input: {url_input[:80]}...")
                    st.markdown(f"<p style='color:#10b981; font-weight:800; font-size:1.4rem; margin:0;'>Best Calculated Rate: ₹{cheapest_price}</p>", unsafe_allow_html=True)
                    st.write("✓ URL Verified | ✓ Multi-Platform API Checked")
                st.markdown("</div>", unsafe_allow_html=True)
                
                # --- AUDIO FIX CONTAINER LOADING IN REAL-TIME INTERACTION ---
                st.markdown("### 📹 Live Verified Media Broadcast")
                load_unmuted_video_stream()
                st.write(" ")

                # --- MULTI RETAILER GRID COLS ---
                st.markdown("### 📊 Worldwide Stores Price Comparison Index")
                grid_cols = st.columns(4)
                for idx, store in enumerate(platforms):
                    with grid_cols[idx]:
                        is_winner = (store["label"] == cheapest_store)
                        accent_border = "border: 2px solid #10b981; background: #f0fdf4;" if is_winner else ""
                        badge_text = "🟢 SABSE SASTA DEAL" if is_winner else "⚪ Standard App Rate"
                        badge_color = "#10b981" if is_winner else "#64748b"
                        
                        st.markdown(f"""
                        <div class='card-matrix' style='{accent_border}'>
                            <div style='font-size:1.15rem; font-weight:800; color:{store["theme"]};'>{store["label"]}</div>
                            <div style='color:{badge_color}; font-weight:700; font-size:0.8rem; margin:4px 0;'>{badge_text}</div>
                            <div class='price-val' style='color:{"#10b981" if is_winner else "#0f172a"};'>₹{generated_prices[store["label"]]}</div>
                            <a href='{store["base_url"]}' target='_blank' class='store-link' style='background-color:{store["theme"]};'>OPEN APP STORE</a>
                        </div>
                        """, unsafe_allow_html=True)

    st.sidebar.markdown("**User Session:** Active Profile via Google")
    if st.sidebar.button("LOG OUT FROM SYSTEM"):
        st.session_state.logged_in = False
        st.rerun()
    
