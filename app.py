import os
import streamlit as st
import pandas as pd
import requests
import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from datetime import datetime
import numpy as np
import base64
import random

# Import the external text template registries
import templates
import importlib
importlib.reload(templates)  # Forces Streamlit to read your text updates on every refresh

# 1. External Asset Integration Helper
def local_css(file_name):
    """Loads a local CSS file with proper unsafe raw HTML rendering."""
    if os.path.exists(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# 2. Main Operational Runtime Initialization (Local Model Loading)
local_css(r"assets/style.css")

TMDB_API_KEY = st.secrets["TMDB_API_KEY"]
LOCAL_LOGO_PATH = r"assets/tmdb_logo.svg"
MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment-latest"

@st.cache_resource
def load_production_transformer():
    """Loads the tokenizer and weights into local memory using caching to prevent reloads."""
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)
    return tokenizer, model, device

tokenizer, model, device = load_production_transformer()

# 3. Authentic Human Consensus Synthesis Engine (Dynamic Registry Router)
def generate_human_consensus(fantastic, neutral, bad, title, vote_avg=None):
    total = len(fantastic) + len(neutral) + len(bad)
    if total == 0:
        return "Not enough data to parse an audience baseline right now."
        
    f_pct = (len(fantastic) / total) * 100
    n_pct = (len(neutral) / total) * 100
    b_pct = (len(bad) / total) * 100

    # Initialize isolated random state seeded by movie identity to ensure unique stability
    seed_value = sum(ord(c) for c in title) + int(f_pct * 100)
    local_rng = random.Random(seed_value)

    # Resolve positive percentage keys from external phrase registry
    if f_pct >= 85: f_key = "high"
    elif f_pct >= 70: f_key = "mid"
    elif f_pct >= 55: f_key = "low"
    else: f_key = "rare"
    f_phrase = local_rng.choice(templates.PHRASE_REGISTRY["fantastic"][f_key])

    # Resolve negative percentage keys from external phrase registry
    if b_pct >= 75: b_key = "critical"
    elif b_pct >= 55: b_key = "heavy"
    elif b_pct >= 35: b_key = "moderate"
    elif b_pct >= 15: b_key = "noticeable"
    elif b_pct > 0: b_key = "trace"
    else: b_key = "none"
    b_phrase = local_rng.choice(templates.PHRASE_REGISTRY["bad"][b_key])

    # HYBRID ROUTING LAYER: Intercept balanced/sober macro profiles
    is_measured_success = False
    if vote_avg and (6.0 <= vote_avg <= 8.0) and (f_pct >= 65):
        is_measured_success = True

    if is_measured_success:
        pool_intro = [
            "The critical conversation surrounding '{title}' presents an interesting case study, displaying a reception that is highly favorable yet distinctly reserved and grounded in its enthusiasm.",
            "While '{title}' has built a dedicated emotional following, the broader commentary handles the narrative with a highly analytical, measured perspective."
        ]
        pool_cores = [
            "Data streams indicate that while {f_phrase} point out the clear structural strengths of the framework, the praise focuses heavily on its realistic execution rather than ecstatic hype.",
            "The logs show that {f_phrase} admire the emotional and stylistic sincerity, keeping the active discussion focused on its sober, deeply human approach."
        ]
        pool_nuances = [
            "This balanced viewpoint ensures that {b_phrase} don't derail the film's standing, as the minor critiques read more like objective observations than outright hostile complaints.",
            "Even with {b_phrase} addressing pacing or adaptation choices, the general tone preserves a steady, reflective focus."
        ]
        pool_verdicts = [
            "Ultimately, it stands as a project that commands respect for its grounded execution, proving that a film doesn't need loud block-buster fireworks to make a meaningful connection.",
            "It leaves behind a lasting legacy defined by steady, quiet appreciation rather than volatile internet noise."
        ]
    else:
        if f_pct >= 75: tier_key = "FANTASTIC"
        elif f_pct >= 60: tier_key = "FAVORABLE"
        elif b_pct >= 55: tier_key = "CRITICAL"
        else: tier_key = "POLARIZED"
        
        pool_intro = templates.TIER_REGISTRY[tier_key]["intros"]
        pool_cores = templates.TIER_REGISTRY[tier_key]["cores"]
        pool_nuances = templates.TIER_REGISTRY[tier_key]["nuances"]
        pool_verdicts = templates.TIER_REGISTRY[tier_key]["verdicts"]

    # Select pieces and extract tokens dynamically
    s1 = local_rng.choice(pool_intro).format(title=title, f_phrase=f_phrase, b_phrase=b_phrase)
    s2 = local_rng.choice(pool_cores).format(title=title, f_phrase=f_phrase, b_phrase=b_phrase)
    s3 = local_rng.choice(pool_nuances).format(title=title, f_phrase=f_phrase, b_phrase=b_phrase)
    s4 = local_rng.choice(pool_verdicts).format(title=title, f_phrase=f_phrase, b_phrase=b_phrase)

    return f"{s1} {s2} {s3} {s4}"

# 4. Star Distribution Modeling Helper
def simulate_star_breakdown(total_votes, vote_average):
    if total_votes == 0:
        return [0, 0, 0, 0, 0]
    target_mean = vote_average / 2.0
    tiers = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    variance = 0.65
    probs = np.exp(-((tiers - target_mean) ** 2) / (2 * variance))
    probs /= probs.sum()
    raw_counts = np.round(probs * total_votes).astype(int)
    diff = total_votes - raw_counts.sum()
    raw_counts[4] += diff
    return np.clip(raw_counts, 0, None).tolist()

# 5. Sidebar Input Architecture
st.sidebar.title("Find Your Film")
search_input = st.sidebar.text_input("Type Movie Title Here:", value="")

movie_options = {}
movie_id = None

if search_input.strip():
    search_url = "https://api.themoviedb.org/3/search/movie"
    search_params = {"api_key": TMDB_API_KEY, "query": search_input}
    try:
        search_url_res = requests.get(search_url, params=search_params)
        if search_url_res.status_code == 200:
            results = search_url_res.json().get("results", [])
            for movie in results[:10]:
                release_year = movie.get("release_date", "0000")[:4]
                display_title = f"{movie.get('title')} ({release_year})"
                movie_options[display_title] = movie.get("id")
    except Exception as e:
        st.sidebar.error(f"Search API Stalled: {str(e)}")

if movie_options:
    selected_movie = st.sidebar.selectbox("Select matching movie entry:", list(movie_options.keys()))
    movie_id = movie_options[selected_movie]
else:
    if search_input.strip(): st.sidebar.warning("No dynamic database matches discovered.")
    else: st.sidebar.info("Type a keyword above to generate matching options.")

spill_tea_clicked = st.sidebar.button("Spill the Tea ☕")

# Main Title Render
st.title("🎬 The Movie Vibe Check")
st.markdown("<p style='color: #9ca3af; font-size: 1.1rem; margin-top: -15px;'>A sophisticated look at audience sentiment trends using deep learning.</p>", unsafe_allow_html=True)
st.markdown("<hr style='margin-bottom: 30px; border-color: #374151;'>", unsafe_allow_html=True)

# 6. Pipeline Analysis Execution Context
if spill_tea_clicked and movie_id:
    with st.spinner("Processing local vectorized batch analysis..."):
        base_url = "https://api.themoviedb.org/3/movie"
        params = {"api_key": TMDB_API_KEY}
        det_res = requests.get(f"{base_url}/{movie_id}", params=params)
        cred_res = requests.get(f"{base_url}/{movie_id}/credits", params=params)
        rev_res = requests.get(f"{base_url}/{movie_id}/reviews", params=params)
        
        if det_res.status_code == 200 and cred_res.status_code == 200 and rev_res.status_code == 200:
            movie_data = det_res.json()
            cred_data = cred_res.json()
            review_data = rev_res.json()
            
            title = movie_data.get("title", "Unknown Title")
            tagline = movie_data.get("tagline", "")
            global_votes = movie_data.get("vote_count", 0)
            vote_avg = movie_data.get("vote_average", 0.0)
            total_reviews = review_data.get("total_results", 0)
            poster_path = movie_data.get("poster_path", "")
            backdrop_path = movie_data.get("backdrop_path", "")
            raw_date = movie_data.get("release_date", "")
            formatted_date = datetime.strptime(raw_date, "%Y-%m-%d").strftime("%d-%b-%Y") if raw_date else "N/A"
            
            crew_list = cred_data.get("crew", [])
            directors = [m.get("name") for m in crew_list if m.get("job") == "Director"]
            cast_list = cred_data.get("cast", [])
            leads = [f"{c.get('name')} ({c.get('character')})" for c in cast_list[:3]]
            supporting = [f"{c.get('name')} ({c.get('character')})" for c in cast_list[3:8]]
            
            # Local Batch Matrix Inference
            reviews_list = review_data.get("results", [])
            text_batch = [rev.get("content", "").strip() for rev in reviews_list if rev.get("content", "").strip()]
            
            fantastic_bucket = []
            neutral_bucket = []
            bad_bucket = []
            
            if len(text_batch) > 0:
                inputs = tokenizer(text_batch, padding=True, truncation=True, max_length=256, return_tensors="pt").to(device)
                with torch.no_grad():
                    outputs = model(**inputs)
                    probs = F.softmax(outputs.logits, dim=-1).cpu().numpy()
                
                for idx, prob in enumerate(probs):
                    review_text = text_batch[idx]
                    pred_class = prob.argmax()
                    
                    # TONE FIX ADJUSTMENT: Reclassify balanced text profiles into Neutral
                    lowercase_review = review_text.lower()
                    if pred_class == 2 and any(kw in lowercase_review for kw in ["delicate balance", "grounded approach", "measured tone", "analytical"]):
                        pred_class = 1
                    
                    if pred_class == 2: fantastic_bucket.append(review_text)
                    elif pred_class == 1: neutral_bucket.append(review_text)
                    else: bad_bucket.append(review_text)
            
            backdrop_url = f"https://image.tmdb.org/t/p/original{backdrop_path}" if backdrop_path else ""
            poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else ""
            
            # Assemble Star Breakdown Elements
            star_counts = simulate_star_breakdown(global_votes, vote_avg)
            star_bars_html = ""
            for star_idx, count in enumerate(reversed(star_counts)):
                star_num = 5 - star_idx
                pct = (count / global_votes) * 100 if global_votes > 0 else 0
                star_bars_html += f'<div class="hero-rating-bar-container"><div style="display: flex; justify-content: space-between; font-size: 0.85rem; color: #ffffff;"><strong>⭐ {star_num} Stars</strong><span style="color: #cbd5e1;">{count:,} ({pct:.1f}%)</span></div><div class="hero-rating-bar-bg"><div class="hero-rating-bar-fill" style="width: {pct}%;"></div></div></div>'

            # Open Landscape Hero Profile Panel
            st.markdown(f"""
<div class="movie-hero-panel" style="background-image: linear-gradient(to right, rgba(17, 24, 39, 0.75) 30%, rgba(31, 41, 55, 0.1) 100%), url('{backdrop_url}');">
<div class="hero-poster-column">
<img src="{poster_url}" class="hero-poster-img" alt="Poster"/>
</div>
<div class="hero-details-column">
<h2 style="margin-top: 0; font-size: 2.2rem; margin-bottom: 5px; color: #ffffff;">{title}</h2>
<p style="font-style: italic; color: #f3f4f6; margin-top: 0; margin-bottom: 20px; font-size: 1.05rem;">"{tagline}"</p>
<p style="margin: 6px 0; color:#f3f4f6;"><strong>Release Date:</strong> {formatted_date}</p>
<p style="margin: 6px 0; color:#f3f4f6;"><strong>Director:</strong> {', '.join(directors) if directors else 'Unknown'}</p>
<p style="margin: 6px 0; color:#f3f4f6;"><strong>Lead Cast:</strong> {', '.join(leads) if leads else 'N/A'}</p>
<p style="margin: 6px 0; color:#f3f4f6;"><strong>Supporting Cast:</strong> {', '.join(supporting) if supporting else 'N/A'}</p>
<p style="margin: 15px 0 0 0; font-size: 0.95rem; color: #e5e7eb;">Global Ratings: {global_votes:,} votes &nbsp;|&nbsp; Text Reviews: {total_reviews}</p>
</div>
<div class="hero-ratings-column">
<p style="margin-top: 0; margin-bottom: 12px; font-weight: bold; color: #ffffff; font-size: 1rem;">Global Rating Breakdown:</p>
{star_bars_html}
</div>
</div>
""", unsafe_allow_html=True)
            
            # CONDITIONAL INTERFACE OVERLAY: Summaries require at least 10 text reviews
            if total_reviews < 10:
                gif_html = ""
                gif_path = r"assets/more data.gif"
                
                if os.path.exists(gif_path):
                    with open(gif_path, "rb") as f:
                        encoded_gif = base64.b64encode(f.read()).decode("utf-8")
                    gif_html = f'<img src="data:image/gif;base64,{encoded_gif}" class="hungry-gif-element" alt="Hungry for Data"/>'
                else:
                    gif_html = '<div style="font-size: 4rem;">🧀</div>'
                
                st.markdown(f"""
                <div class="hungry-card-wrapper">
                    <div class="hungry-text-side">
                        <h3 style="margin-top: 0; margin-bottom: 12px; color: #ffffff; font-size: 1.6rem;">The Oracle is Hungry for Data!</h3>
                        <p style="color: #9ca3af; margin: 0; line-height: 1.75; font-size: 1.05rem;">
                            This movie currently holds only <strong>{total_reviews}</strong> text review{'s' if total_reviews != 1 else ''} on the native platform registry. 
                            Our sentiment pipeline needs a baseline threshold of at least <strong>10 text reviews</strong> to calculate accurate macro metrics 
                            and write an un-biased consensus summary. Feed me more data to run a full Vibe Check!
                        </p>
                    </div>
                    <div class="hungry-gif-side">
                        {gif_html}
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                total_analyzed = len(fantastic_bucket) + len(neutral_bucket) + len(bad_bucket)
                pct_fantastic = (len(fantastic_bucket) / total_analyzed) * 100 if total_analyzed > 0 else 0
                pct_neutral = (len(neutral_bucket) / total_analyzed) * 100 if total_analyzed > 0 else 0
                pct_bad = (len(bad_bucket) / total_analyzed) * 100 if total_analyzed > 0 else 0
                
                # Minimalist Floating Emoji Metrics (Borders & Card Containers completely stripped)
                m_col1, m_col2, m_col3 = st.columns(3)
                with m_col1: 
                    st.markdown(f"""
                    <div style="text-align: center; margin-bottom: 15px;">
                        <span style="font-size: 3.2rem; display: block; margin-bottom: 5px;">🤩</span>
                        <span style="font-size: 1.8rem; font-weight: bold; color: #ffffff;">{pct_fantastic:.1f}%</span>
                    </div>
                    """, unsafe_allow_html=True)
                with m_col2: 
                    st.markdown(f"""
                    <div style="text-align: center; margin-bottom: 15px;">
                        <span style="font-size: 3.2rem; display: block; margin-bottom: 5px;">🤔</span>
                        <span style="font-size: 1.8rem; font-weight: bold; color: #ffffff;">{pct_neutral:.1f}%</span>
                    </div>
                    """, unsafe_allow_html=True)
                with m_col3: 
                    st.markdown(f"""
                    <div style="text-align: center; margin-bottom: 15px;">
                        <span style="font-size: 3.2rem; display: block; margin-bottom: 5px;">😞</span>
                        <span style="font-size: 1.8rem; font-weight: bold; color: #ffffff;">{pct_bad:.1f}%</span>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Consensus Summary Layout Box
                st.markdown("<br><h3 style='font-size: 1.4rem;'>📌 The TL;DR Consensus</h3>", unsafe_allow_html=True)
                summary_text = generate_human_consensus(fantastic_bucket, neutral_bucket, bad_bucket, title, vote_avg)
                st.markdown(f'<div class="summary-box">{summary_text}</div>', unsafe_allow_html=True)
                
            # UNIFIED REVIEW DISPLAY: Renders the column rows for ALL search results regardless of total count
            st.markdown("<br><h3 style='font-size: 1.4rem;'>💬 Real Reviews</h3>", unsafe_allow_html=True)
            r_col1, r_col2, r_col3 = st.columns(3)
            with r_col1:
                st.markdown('<p class="review-column-header" style="color: #28a745;">🟢 Fantastic Reviews</p>', unsafe_allow_html=True)
                if fantastic_bucket:
                    for text in fantastic_bucket[:5]: st.markdown(f'<div class="review-card">{text[:320]}...</div>', unsafe_allow_html=True)
                else: st.caption("No text records available in this sentiment class.")
            with r_col2:
                st.markdown('<p class="review-column-header" style="color: #ffc107;">🟡 Neutral Reviews</p>', unsafe_allow_html=True)
                if neutral_bucket:
                    for text in neutral_bucket[:5]: st.markdown(f'<div class="review-card">{text[:320]}...</div>', unsafe_allow_html=True)
                else: st.caption("No text records available in this sentiment class.")
            with r_col3:
                st.markdown('<p class="review-column-header" style="color: #dc3545;">🔴 Bad Reviews</p>', unsafe_allow_html=True)
                if bad_bucket:
                    for text in bad_bucket[:5]: st.markdown(f'<div class="review-card">{text[:320]}...</div>', unsafe_allow_html=True)
                else: st.caption("No text records available in this sentiment class.")
        else:
            st.error("Failed to extract operational metadata records from TMDb channels.")
elif spill_tea_clicked:
    st.sidebar.error("Select an active movie entry first from the search results.")
else:
    st.markdown(f"""
<div class="welcome-container">
<h2 style="color: #f9fafb; margin-bottom: 10px; font-weight: bold;">The Cinema Oracle is Resting... 👁️</h2>
<p style="color: #9ca3af; font-size: 1.05rem; max-width: 650px; margin: 0 auto 25px auto;">
The deep learning model is fully calibrated on your memory registers and waiting for data. Type a film title into the 
sidebar input to discover entries, select your target, and run a live sentiment consensus Vibe Check.
</p>
</div>
""", unsafe_allow_html=True)

# 7. Integrated HTML Flexbox Footer
st.markdown("<br>", unsafe_allow_html=True)
svg_content = ""
if os.path.exists(LOCAL_LOGO_PATH):
    try:
        with open(LOCAL_LOGO_PATH, "r", encoding="utf-8") as f:
            svg_content = f.read()
    except:
        pass

if not svg_content:
    svg_content = '<div style="font-weight: bold; color: #01b4e4; border: 2px solid #01b4e4; padding: 4px 12px; border-radius: 4px; text-align: center;">TMDB</div>'

st.markdown(f"""
<div class="footer-container">
<div class="footer-logo-wrapper">
{svg_content}
</div>
<p class="footer-text">
This product uses the TMDb API but is not endorsed or certified by TMDb. All catalog metadata entries, credits, poster matrices, and text reviews are fetched dynamically via live open database infrastructure channels.
</p>
</div>
""", unsafe_allow_html=True)