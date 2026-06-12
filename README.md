# 🎥 Movie Vibe Check

> 🚀 Portfolio Project | Deep Learning | NLP | Real-Time API Integration | Streamlit Deployment | Production-Oriented Architecture

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-orange)
![Transformers](https://img.shields.io/badge/HuggingFace-RoBERTa-yellow)
![Streamlit](https://img.shields.io/badge/Streamlit-Live%20Dashboard-red)
![TMDb](https://img.shields.io/badge/TMDb-Live%20API-green)

</div>

---

## 🚀 Live Demo

👉 **Try the application here**

[https://customersentimentbert-n6emezcfiq7fbm72hqqgbs.streamlit.app](https://tmdbsentimentpipeline-hxzs7krjdez2jzvn5pgwn9.streamlit.app/)

## 🎯 What Makes This Project Different?

Most sentiment analysis projects stop at:

```
Review → Model → Positive / Negative
```

This project goes several steps further:

```text
Live Reviews
      │
      ▼
RoBERTa Transformer
      │
      ▼
Tone Correction Engine
      │
      ▼
Hybrid Routing Layer
      │
      ▼
Linguistic Synthesis Engine
      │
      ▼
Human-Readable Movie Intelligence
```

### Key Innovations

🧠 **RoBERTa Transformer Inference**

🎭 **2.5+ Million Dynamic Summary Variations**

🎯 **Custom Neutral Sentiment Correction**

🏛️ **Fully Decoupled Architecture**

🛡️ **Data Sufficiency Guardrails**

🌐 **Live TMDb API Integration**

🎨 **Minimalist Analytics Dashboard**

---

# 💼 Skills Demonstrated

| Category | Skills |
|-----------|----------|
| Machine Learning | Sentiment Analysis, Classification |
| NLP | Transformer Models, Text Processing |
| Deep Learning | PyTorch, Hugging Face |
| Software Engineering | Modular Architecture |
| API Integration | TMDb REST API |
| Frontend | Streamlit |
| Deployment | Cloud Deployment |
| UX Design | Data Visualization |
| Data Engineering | Data Validation & Processing |

---

# 🏛️ End-to-End Processing Architecture

```text
┌──────────────────────────────────────┐
│        Streamlit User Interface       │
└─────────────────┬────────────────────┘
                  │
                  ▼
┌──────────────────────────────────────┐
│          TMDb API Gateway            │
└───────────────┬──────────────────────┘
                │
                ▼
┌──────────────────────────────────────┐
│      Review Collection Layer         │
└───────────────┬──────────────────────┘
                │
                ▼
┌──────────────────────────────────────┐
│    RoBERTa Transformer Inference     │
└───────────────┬──────────────────────┘
                │
                ▼
┌──────────────────────────────────────┐
│      Tone Correction Framework       │
└───────────────┬──────────────────────┘
                │
                ▼
┌──────────────────────────────────────┐
│      Hybrid Routing Layer            │
└───────────────┬──────────────────────┘
                │
                ▼
┌──────────────────────────────────────┐
│ Linguistic Synthesis Engine          │
│        (templates.py)                │
└───────────────┬──────────────────────┘
                │
                ▼
┌──────────────────────────────────────┐
│     Minimalist Sentiment Dashboard   │
└──────────────────────────────────────┘
```

---

# ⚙️ Engineering Highlights

## 🧩 Decoupled Linguistic Matrix Engine

### Problem

Embedding summary text directly inside application code quickly becomes difficult to maintain.

### Solution

All narrative generation logic is isolated inside:

```python
templates.py
```

The application layer handles:

- API orchestration
- Data processing
- Model inference
- UI rendering

The language engine handles:

- Narrative generation
- Summary composition
- Tone management

### Result

✅ Cleaner architecture

✅ Easier maintenance

✅ Improved scalability

---

## 🎭 2.5+ Million Dynamic Summaries

The synthesis engine uses four independent text pools:

```python
Introduction
Core Sentiment
Nuance Layer
Final Verdict
```

Each paragraph is dynamically assembled from interchangeable components.

This creates:

```text
2,500,000+ possible combinations
```

while maintaining coherent human-readable language.

---

## 🎯 Hybrid Sentiment Routing Layer

Traditional transformer models often classify analytical reviews as strongly positive.

Example:

```text
"The film adopts a grounded and measured approach."
```

may be classified as:

```text
Positive
```

instead of:

```text
Neutral
```

The Hybrid Routing Layer evaluates:

- Model confidence
- Keyword patterns
- Global TMDb ratings

before assigning final narrative tone.

---

## 🧠 Tone Correction Framework

A custom keyword interception layer detects phrases such as:

```text
balanced
measured
grounded
restrained
thoughtful
delicate balance
```

and reclassifies misleading positive predictions into Neutral where appropriate.

This improves human interpretability.

---

## 🛡️ Data Sufficiency Guardrails

The system requires:

```text
Minimum Reviews = 10
```

before generating a macro sentiment summary.

When insufficient data exists:

- Review classification still runs
- Dashboard remains functional
- Summary generation is disabled

This prevents misleading conclusions.

---

## 🎨 Minimalist Dashboard Design

Instead of traditional metric cards:

❌ Heavy Containers

❌ Thick Borders

❌ Dashboard Clutter

The UI emphasizes:

📈 Positive

📊 Neutral

📉 Negative

through lightweight visual indicators and whitespace-focused design.

---

# 🧠 Deep Learning Stack

| Component | Technology |
|------------|------------|
| Framework | PyTorch |
| Model | cardiffnlp/twitter-roberta-base-sentiment-latest |
| Tokenizer | RoBERTa BPE |
| Max Length | 256 Tokens |
| Classes | Positive / Neutral / Negative |
| Caching | Streamlit Cache Resource |

---

# 🗂️ Project Structure

```text
tmdb_sentiment_pipeline/
│
├── .streamlit/
│   └── secrets.toml
│
├── assets/
│   ├── style.css
│   ├── tmdb_logo.svg
│   └── more_data.gif
│
├── app.py
├── templates.py
├── requirements.txt
└── README.md
```

---

# 🚀 Local Installation

## Clone Repository

```bash
git clone https://github.com/ak0959/customer_sentiment_bert.git
cd customer_sentiment_bert
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure API Credentials

```toml
TMDB_API_KEY="YOUR_API_KEY"
```

Place inside:

```text
.streamlit/secrets.toml
```

## Launch Application

```bash
streamlit run app.py
```

---

# 🔮 Future Enhancements

- Multi-language sentiment support
- Review topic modeling
- Actor-level sentiment tracking
- Genre sentiment benchmarking
- Historical sentiment trends
- LLM-generated critic insights

---

# 👨‍💻 About the Developer

**Amit Kadia**

Senior Programme Manager | AI & Data Analytics Professional

Building production-oriented applications that combine:

🧠 Artificial Intelligence

📊 Data Analytics

⚙️ Software Engineering

🎨 User-Centered Design

---

⭐ If you found this project interesting, consider starring the repository.
