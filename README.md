# BigQuery Release Radar 📡

A premium, modern web dashboard to fetch, view, filter, bookmark, and tweet the latest official Google BigQuery release notes. 

Built using a **Python Flask** backend and a high-fidelity **Glassmorphism HTML/CSS/JS** frontend.

🔗 **Live Demo**: [https://bigquery-radar.vercel.app/](https://bigquery-radar.vercel.app/)

---

## ✨ Features

- **💎 Premium Glassmorphic Design**: 
  - Obsidian-space theme utilizing frosted glass panels (`backdrop-filter: blur(16px)`), neon glows, and thin radiant borders.
  - Interactive smooth animations (scaling hover states, rotating loaders, and springy theme switches).
- **📡 Automatic Feed Parser**: Connects to the official Google Cloud XML feed, fetches, parses, and splits daily entries containing multiple updates into individual, category-tagged cards.
- **⭐ Bookmarks/Favorites**: Star individual release notes to save them locally (persisted via `localStorage`). Easily browse them using the **Bookmarked** filter channel in the sidebar.
- **📊 Live Insights/Analytics**: Collapsible analytics panel displaying stats on parsed releases and features count.
- **🐦 Enhanced Tweet Composer**:
  - Select one or more cards to compile an compiled digest tweet, or tweet cards individually.
  - Dynamic template selector: Choose between **⚡ Punchy**, **📝 Detailed**, and **💡 Developer** layouts.
  - Interactive hashtag chips (`#BigQuery`, `#GoogleCloud`, `#GCP`) to toggle tags instantly before launching.
  - Real-time character count preview with warnings for X's 280-character limit.
- **⚡ Smart Caching**: Feeds are cached in local storage for instant loads on startup, refreshing seamlessly in the background.

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask (standard library XML parsing for zero external parser dependencies)
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
├── app.py                  # Flask application & Feed API Endpoint
├── templates/
│   └── index.html          # Core Glassmorphic UI with caching, bookmarks & tweet templates
├── .gitignore              # Ignored files (venv, caches, etc.)
└── README.md               # Updated project documentation
```

---

## 👤 Author

- **Abhimanyu Sah** - [@AbhimanyuSah-DEV](https://github.com/AbhimanyuSah-DEV)

