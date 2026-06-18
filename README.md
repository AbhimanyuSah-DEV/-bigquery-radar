# GCP & Gemini Release Radar 📡

A premium, modern web dashboard to fetch, view, filter, bookmark, and tweet the latest official release notes for Google BigQuery and the Gemini API.

Built using a **Python Flask** backend and a high-fidelity **Glassmorphism HTML/CSS/JS** frontend.

🔗 **Live Demo**: [https://bigquery-radar.vercel.app/](https://bigquery-radar.vercel.app/)

---

## ✨ Features

- **💎 Premium Glassmorphic Design**: 
  - Obsidian-space theme utilizing frosted glass panels (`backdrop-filter: blur(16px)`), neon glows, and thin radiant borders.
  - Interactive smooth animations (scaling hover states, rotating loaders, and springy theme switches).
- **📡 Dual Feed Integration**:
  - Connects to the official **Google BigQuery** Atom feed.
  - Scrapes the official **Gemini API** changelog page using cookie jar redirect handling.
  - Aggregates, clean relative paths, parses bullet items into individual updates, and sorts everything chronologically in a single unified timeline.
- **🏷️ Feed Source Filters**: Choose to view "All Feeds", "BigQuery" only, or "Gemini API" only with dedicated source badge tags on cards.
- **⭐ Bookmarks/Favorites**: Star individual release notes to save them locally (persisted via `localStorage`). Easily browse them using the **Bookmarked** filter channel in the sidebar.
- **📊 Live Insights/Analytics**: Analytics panel displaying stats on aggregated releases and features count.
- **🐦 Enhanced Tweet Composer**:
  - Select one or more cards to compile a digest tweet, or tweet cards individually.
  - Dynamic template selector: Choose between **⚡ Punchy**, **📝 Detailed**, and **💡 Developer** layouts.
  - Smart hashtags toggle: Automatically selects `#BigQuery` or `#Gemini` based on the sources of your selected updates.
  - Real-time character count preview with warnings for X's 280-character limit.
- **⚡ Smart Caching**: Feeds are cached in local storage for instant loads on startup, refreshing seamlessly in the background.

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask (standard library XML parsing & HTML scraping for zero external scraping dependencies)
- **Frontend**: Glassmorphism CSS variables, HTML5 Semantic Elements, JavaScript (ES6+), FontAwesome Icons, Google Fonts (Outfit & Plus Jakarta Sans)

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher installed.

### Installation & Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AbhimanyuSah-DEV/-bigquery-radar.git
   cd -bigquery-radar
   ```

2. **Install dependencies**:
   ```bash
   pip install flask
   ```

3. **Run the Flask development server**:
   ```bash
   python app.py
   ```

4. **Access the application**:
   Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your web browser.

---

## 📁 Project Structure

```text
├── app.py                  # Flask application & Dual Feed API Endpoints
├── templates/
│   └── index.html          # Glassmorphic UI dashboard with multi-source filtering & caching
├── vercel.json             # Vercel serverless deployment config
├── requirements.txt        # Production Python dependencies
├── .gitignore              # Ignored files (venv, caches, etc.)
└── README.md               # Updated project documentation
```

---

## 👤 Author

- **Abhimanyu Sah** - [@AbhimanyuSah-DEV](https://github.com/AbhimanyuSah-DEV)
