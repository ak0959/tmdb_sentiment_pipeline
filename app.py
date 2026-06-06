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

# 3. Authentic Human Consensus Synthesis Engine (Vernacular Translation Layer)
def generate_human_consensus(fantastic, neutral, bad, title):
    total = len(fantastic) + len(neutral) + len(bad)
    if total == 0:
        return "Not enough data to parse an audience baseline right now."
        
    f_pct = (len(fantastic) / total) * 100
    n_pct = (len(neutral) / total) * 100
    b_pct = (len(bad) / total) * 100

    # Initialize isolated random state seeded by movie identity to ensure unique stability
    seed_value = sum(ord(c) for c in title) + int(f_pct * 100)
    local_rng = random.Random(seed_value)

    # Convert positive percentages into conversational human descriptions
    if f_pct >= 85: 
        f_phrase = local_rng.choice(["the vast majority of people", "nearly everyone who watched it", "almost the entire audience"])
    elif f_pct >= 70: 
        f_phrase = local_rng.choice(["a clear majority of viewers", "most fans", "a massive chunk of the crowd"])
    elif f_pct >= 55: 
        f_phrase = local_rng.choice(["a solid majority", "a good number of people", "more than half the viewers"])
    else: 
        f_phrase = local_rng.choice(["a small group of enthusiasts", "only a fraction of viewers", "a minor subset of fans"])

    # Convert negative percentages into conversational human descriptions
    if b_pct >= 75: 
        b_phrase = local_rng.choice(["almost the entire thread is filled with complaints", "critics completely dominate the conversation"])
    elif b_pct >= 55: 
        b_phrase = local_rng.choice(["most people walked away pretty disappointed", "a major chunk of the crowd felt let down"])
    elif b_pct >= 35: 
        b_phrase = local_rng.choice(["a significant portion of critical feedback", "a pretty large group of unhappy viewers"])
    elif b_pct >= 15: 
        b_phrase = local_rng.choice(["a noticeable minority of critics", "a decent sized group of complaints"])
    elif b_pct > 0: 
        b_phrase = local_rng.choice(["only a tiny handful of complaints", "barely a whisper of negative feedback", "a very small minority of critics"])
    else: 
        b_phrase = "virtually zero critical pushback"

    pool_intro = []
    pool_core = []
    pool_nuance = []
    pool_verdict = []

    # TIER A: Highly Positive Consensus
    if f_pct >= 75:
        pool_intro = [
            f"The reaction to '{title}' is incredibly strong, with fans lining up to celebrate almost every major choice the filmmakers made.",
            f"It's rare to see this much agreement online, but the reception for '{title}' is leaning heavily into absolute praise.",
            f"The general vibe surrounding '{title}' is electric, proving that it hit exactly the right notes with its audience."
        ]
        pool_core = [
            f"Looking at the commentary, {f_phrase} walked away absolutely glowing, focusing on how well the story keeps you locked in.",
            f"With {f_phrase} keeping an enthusiastic tone, the discussions are dominated by appreciation for the cast and its pure entertainment value.",
            f"The consensus shows {f_phrase} giving a big thumbs-up to the film's overall ambition and scale."
        ]
        pool_nuance = [
            f"Critical notes are pretty hard to find here—with {b_phrase}, the positive momentum stays completely unchallenged.",
            f"The logs show an incredibly quiet critical camp with {b_phrase}, meaning most viewers simply sat back and enjoyed the ride.",
            f"Even with {b_phrase} pointing out minor flaws, those complaints are completely drowned out by the positive energy."
        ]
        pool_verdict = [
            "It's safe to say this one has found a permanent spot among fan favorites, cementing a legacy that will hold up well over time.",
            "Ultimately, it marks a massive win for everyone involved, proving that when a film connects this deeply, the enthusiasm sticks around.",
            "This is the exact kind of reception that turns a standard theatrical release into a lasting community favorite."
        ]

    # TIER B: Moderately Favorable Consensus
    elif f_pct >= 60:
        pool_intro = [
            f"The general feedback for '{title}' is comfortably positive, showing that it successfully won over a solid majority of viewers.",
            f"Most people are walking away happy with '{title}', even if the online threads feature a few healthy debates.",
            f"The baseline consensus for '{title}' leans quite favorable, suggesting its core narrative landed well with everyday fans."
        ]
        pool_core = [
            f"The metrics mirror this, showing that {f_phrase} had great things to say about the standout set pieces and character chemistry.",
            f"With {f_phrase} keeping a favorable tone, the general commentary spends a lot of time appreciating the visual style.",
            f"It looks like {f_phrase} felt the core entertainment value easily carried the day."
        ]
        pool_nuance = [
            f"That leaves {b_phrase} picking apart minor structural issues or character arcs.",
            f"We are seeing {b_phrase} pointing out issues with the editing, but it hasn't disrupted the broader positive reception.",
            f"While some viewed it as a safe, middle-of-the-road entry, {b_phrase} stays low enough to keep the win secure."
        ]
        pool_verdict = [
            "It might not be a flawless masterpiece to everyone, but it clearly left a strong impression that will keep it relevant for fans.",
            "At the end of the day, it's a solid win that shows the film has plenty of genuine staying power with the audience.",
            "The final numbers point to a successful run that completely justified the excitement surrounding its release."
        ]

    # TIER C: Heavily Critical Consensus
    elif b_pct >= 55:
        pool_intro = [
            f"The feedback for '{title}' faces a steep uphill battle, with a massive wave of critical pushback dominating the reviews.",
            f"Reactions to '{title}' trend heavily negative, with a clear majority of viewers expressing deep disappointment.",
            f"It's safe to say '{title}' missed the mark for most people, triggering a wave of vocal frustration online."
        ]
        pool_core = [
            f"The feedback is unforgiving, showing that {b_phrase} focused entirely on structural flaws and script issues.",
            f"With {b_phrase} keeping a critical tone, the active threads are filled with complaints about clunky pacing and messy character motivations.",
            f"The data outlines a tough reality, where {b_phrase} felt the creative risks taken simply failed to connect with the room."
        ]
        pool_nuance = [
            f"Even though {f_phrase} tried to defend the film's visual style, their voices are completely buried under the critiques.",
            f"A tiny group of defenders—amounting to just {f_phrase}—points to standout individual performances, but it isn't enough to save the baseline score.",
            f"With {f_phrase} coming back positive, the community consensus is remarkably united in its disappointment."
        ]
        pool_verdict = [
            "It's going to face a massive challenge in winning over film fans long-term, leaving a heavily troubled legacy behind.",
            "Ultimately, the final numbers suggest a project that struggled to balance its massive ambitions with a cohesive execution.",
            "This is a tough layout for any release, and the current vibe indicates it won't be remembered as a fan favorite anytime soon."
        ]

    # TIER D: Polarized / Split / Mixed Consensus
    else:
        pool_intro = [
            f"The conversation around '{title}' is highly polarized, creating an intriguing split across independent review spaces.",
            f"Audiences are completely divided over '{title}', with no single opinion managing to dominate the forums.",
            f"The baseline reception for '{title}' is sitting in a classic middle ground, generating an intense back-and-forth online."
        ]
        pool_core = [
            "For every comment praising an incredible action set piece or a brilliant performance, there is a counter-point pulling apart structural flaws.",
            "Discussions are completely fragmented, with fans fiercely debating whether the unique tone worked or completely tanked.",
            "The threads show a direct clash between viewers who loved the experimental style and traditionalists who wanted a cleaner plot."
        ]
        pool_nuance = [
            f"The metrics confirm this deep divide, showing a nearly even split where {f_phrase} runs directly into critical pushback.",
            f"With a solid chunk of viewers viewing it as an average, safe experience, the remaining camps are locked in a tight tug-of-war.",
            f"The pipeline clocked a highly balanced spread, making it a true textbook definition of a split room."
        ]
        pool_verdict = [
            "This exact pattern guarantees that the film will keep provoking lively debates rather than settling into a quiet consensus.",
            "At the end of the day, it's a project that refuses to leave people indifferent, which is often a win in its own unique way.",
            "The split vibe ensures that its ultimate legacy will completely depend on what individual viewers look for in a film."
        ]

    s1 = local_rng.choice(pool_intro)
    s2 = local_rng.choice(pool_core)
    s3 = local_rng.choice(pool_nuance)
    s4 = local_rng.choice(pool_verdict)

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
                    
                    if pred_class == 2: fantastic_bucket.append(review_text)
                    elif pred_class == 1: neutral_bucket.append(review_text)
                    else: bad_bucket.append(review_text)
            
            backdrop_url = f"https://image.tmdb.org/t/p/original{backdrop_path}" if backdrop_path else ""
            poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else ""
            
            # Assemble Star Breakdown Elements (Flush Left String Building)
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
            
            # DATA BOUNDARY CHECK: Side-by-Side Flexbox warning card using Base64 Local Image parsing
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
                
                # Semantic Metric Cards
                m_col1, m_col2, m_col3 = st.columns(3)
                with m_col1: st.markdown(f'<div class="metric-card accent-fantastic"><p class="metric-header" style="color: #28a745;">🎉 Fantastic</p><p class="metric-value">{pct_fantastic:.1f}%</p></div>', unsafe_allow_html=True)
                with m_col2: st.markdown(f'<div class="metric-card accent-neutral"><p class="metric-header" style="color: #ffc107;">🔆 Neutral</p><p class="metric-value">{pct_neutral:.1f}%</p></div>', unsafe_allow_html=True)
                with m_col3: st.markdown(f'<div class="metric-card accent-bad"><p class="metric-header" style="color: #dc3545;">❌ Not Good At All</p><p class="metric-value">{pct_bad:.1f}%</p></div>', unsafe_allow_html=True)
                
                # Consensus Summary Layout Box
                st.markdown("<br><h3 style='font-size: 1.4rem;'>📌 The TL;DR Consensus</h3>", unsafe_allow_html=True)
                summary_text = generate_human_consensus(fantastic_bucket, neutral_bucket, bad_bucket, title)
                st.markdown(f'<div class="summary-box">{summary_text}</div>', unsafe_allow_html=True)
                
                # Masonry Review Grid Rows
                st.markdown("<h3 style='font-size: 1.4rem;'>💬 Real Reviews</h3>", unsafe_allow_html=True)
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
This product uses the TMDb API but is not endorsed or certified by TMDb. All catalog metadata entries, credits, poster matrices, and text rows are fetched dynamically via live open database infrastructure channels.
</p>
</div>
""", unsafe_allow_html=True)