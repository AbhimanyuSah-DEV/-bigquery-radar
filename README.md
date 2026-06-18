# BigQuery Release Radar 📡

A premium, modern web dashboard to fetch, view, filter, and tweet the latest official Google BigQuery release notes. 

Built using a **Python Flask** backend and a responsive, vanilla **HTML/CSS/JS** frontend.

---

## ✨ Features

- **Automatic Feed Parser**: Connects to the official Google Cloud RSS feed, fetches, parses, and splits daily entries containing multiple updates into individual, readable cards.
- **Sleek Dark Mode**: Designed with a high-fidelity dark-themed design system featuring glassmorphism, responsive grid layout, and custom typography.
- **Filter & Search**: Instantly filter updates by type badges (*Feature*, *Announcement*, *Issue*, *Deprecation*, *General*) or use keyword search.
- **Tweet Selection Mode**:
  - Select one or more updates using checkboxes to compile a single combined tweet.
  - Direct **"Tweet Update"** buttons on individual cards for quick sharing.
  - Real-time character count preview with warnings when approaching/exceeding X's 280-character limit.
- **Dynamic Refresh**: Live refresh button with status indicator and spinner.

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask (standard library XML element parsing for zero external parser dependencies)
- **Frontend**: Vanilla CSS variables, HTML5 Semantic Tags, JavaScript (ES6+), FontAwesome Icons, Google Fonts (Outfit & Plus Jakarta Sans)

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
│   └── index.html          # Core responsive UI with custom XML feed parser & Tweet Composer
├── .gitignore              # Ignored files (venv, caches, etc.)
└── README.md               # Project documentation
```
