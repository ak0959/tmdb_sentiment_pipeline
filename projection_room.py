# projection_room.py
import streamlit as st

def render_page():
    st.title("🎬 Inside the Projection Room")
    st.markdown("<p style='color: #9ca3af; font-size: 1.1rem; margin-top: -15px;'>A glimpse into the AI powering Movie Vibe Check</p>", unsafe_allow_html=True)
    st.markdown("<hr style='margin-bottom: 30px; border-color: #374151;'>", unsafe_allow_html=True)
    
    st.markdown("""
    Ever wondered what thousands of moviegoers are really saying about a film beyond the ratings, review scores, and headlines?
    
    **Movie Vibe Check** was built to uncover the audience story hidden inside large collections of movie reviews. Instead of asking you to read dozens of comments across multiple platforms, the application analyzes audience feedback at scale and transforms it into meaningful insights.
    
    The result is a fast, visual snapshot of how people genuinely felt about a movie.
    
    ---
    
    ### 🎥 Step 1: Gathering the Conversation
    Every journey begins with data. When you select a movie, the application retrieves publicly available review content and movie metadata from live online sources. This means the analysis is performed on real audience opinions rather than a static sample dataset.
    
    The objective is simple: capture the conversation happening around a film as accurately as possible.
    
    ### 📝 Step 2: Understanding the Language
    Once the reviews are collected, each one is processed using Natural Language Processing (NLP) techniques. Rather than looking for isolated keywords, the system evaluates the overall context, tone, and sentiment expressed within the review.
    
    For example, a review such as:
    > "The performances were excellent, but the pacing felt uneven."
    
    contains both praise and criticism. Human opinions are often nuanced, and understanding that nuance is one of the key challenges of sentiment analysis. The goal isn't simply to identify positive or negative words—it's to understand the overall feeling being communicated.
    
    ### 🤖 Step 3: Classifying Audience Sentiment
    After processing the language, the application classifies each review into one of three sentiment categories:
    * **🤩 Positive:** Reviews that express strong appreciation, enjoyment, or satisfaction.
    * **🤔 Neutral:** Balanced, analytical, or mixed opinions that contain both strengths and weaknesses.
    * **😞 Negative:** Reviews that communicate disappointment, frustration, or dissatisfaction.
    
    This classification creates a structured view of audience sentiment while preserving the diversity of opinions present in the review dataset.
    
    ### 🎯 Step 4: Looking Beyond Traditional Sentiment Analysis
    One challenge with sentiment analysis is that not every review fits neatly into a positive or negative category. Many movie reviews are thoughtful, measured, and analytical.
    
    For example:
    > "A visually impressive film with strong performances, although the story occasionally loses momentum."
    
    Traditional sentiment models may interpret a review like this as overwhelmingly positive because of the presence of favorable language. **Movie Vibe Check** introduces additional sentiment refinement logic designed to identify these balanced viewpoints and classify them more appropriately. This helps create a more realistic picture of audience opinion and reduces overly optimistic interpretations of mixed reviews.
    
    ### 📊 Step 5: Building the Audience Snapshot
    Once all reviews have been analyzed, the individual classifications are aggregated into a broader sentiment profile. The percentages displayed on screen represent the distribution of audience reactions across the three sentiment categories.
    
    This provides an immediate view of questions such as:
    * Was the movie widely loved?
    * Did it divide audiences?
    * Were reactions generally mixed?
    * Was there significant negative feedback?
    
    Instead of relying on a single score, the platform reveals how opinions are distributed across the audience.
    
    ### 💡 Step 6: Creating the TL;DR Consensus
    Numbers tell part of the story. The next challenge is explaining why audiences felt the way they did.
    
    To accomplish this, **Movie Vibe Check** analyzes the overall sentiment distribution and review patterns before generating a concise audience consensus. Rather than summarizing individual reviews, the system focuses on capturing the broader narrative emerging from the dataset.
    
    The objective is to answer a simple question:
    > "If I could read hundreds of reviews in a few seconds, what would I learn?"
    
    The TL;DR Consensus is designed to provide exactly that.
    
    ---
    
    ### 🎭 Why Audience Sentiment Matters
    Two movies can have identical ratings while generating completely different audience reactions. One film may receive widespread approval with very little criticism. Another may split viewers into passionate supporters and vocal critics. 
    
    A single score often hides these differences. By examining the language behind the ratings, sentiment analysis helps reveal the emotional patterns and audience perceptions that numbers alone cannot capture.
    
    ### 🧠 A Blend of AI and Human-Centered Design
    Movie Vibe Check was created as a portfolio project exploring the intersection of:
    * Artificial Intelligence
    * Natural Language Processing
    * Data Analytics
    * Interactive Dashboard Design
    * Human-Centered User Experiences
    
    The goal was never to replace human opinion. Instead, it was to build a tool that helps make large volumes of audience feedback easier to explore, understand, and enjoy.
    
    So the next time you search for a movie, you're not just looking at a rating. **You're seeing the audience story behind it.**
    """)