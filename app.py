import os
import re
import urllib.request
import http.cookiejar
import xml.etree.ElementTree as ET
from datetime import datetime
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Route to serve the main frontend page
@app.route('/')
def index():
    return render_template('index.html')

def parse_date_to_key(date_str):
    # Parse date string (e.g. "June 17, 2026" or "May 7, 2026") for sorting
    # Clean up whitespace and any non-breaking spaces
    date_str = date_str.strip().replace('\xa0', ' ')
    try:
        # Match e.g., "June 17, 2026"
        dt = datetime.strptime(date_str, "%B %d, %Y")
        return dt.strftime("%Y-%m-%d")
    except Exception:
        try:
            # Fallback for single digit dates like "June 1, 2026" if needed
            dt = datetime.strptime(date_str, "%B %e, %Y")
            return dt.strftime("%Y-%m-%d")
        except Exception:
            return "0000-00-00"

# API Route to fetch and return release notes as JSON
@app.route('/api/releases')
def get_releases():
    entries = []
    
    # 1. Fetch BigQuery Release Notes (Atom Feed)
    try:
        bq_url = "https://docs.cloud.google.com/feeds/bigquery-release-notes.xml"
        req = urllib.request.Request(
            bq_url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AntigravityFeedReader/1.0'}
        )
        with urllib.request.urlopen(req, timeout=15) as response:
            xml_data = response.read()
        
        root = ET.fromstring(xml_data)
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        
        for entry in root.findall('atom:entry', ns):
            title = entry.find('atom:title', ns)
            title_text = title.text.strip() if title is not None else "Unknown Date"
            
            link_elem = entry.find("atom:link[@rel='alternate']", ns)
            link = link_elem.attrib.get('href') if link_elem is not None else ""
            
            content_elem = entry.find('atom:content', ns)
            content_html = content_elem.text if content_elem is not None else ""
            
            # Rewrite relative paths in BQ content if any
            content_html = re.sub(r'href="/', 'href="https://docs.cloud.google.com/', content_html)
            
            entries.append({
                'source': 'bigquery',
                'title': title_text,
                'date_key': parse_date_to_key(title_text),
                'link': link,
                'content': content_html
            })
    except Exception as e:
        print(f"Error fetching BigQuery feed: {e}")
        
    # 2. Fetch Gemini API Changelog (Scraped HTML Site)
    try:
        gemini_url = "https://ai.google.dev/gemini-api/docs/changelog"
        cj = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')]
        
        with opener.open(gemini_url, timeout=15) as response:
            html = response.read().decode('utf-8')
            
        # Extract headings that match the date format
        matches = list(re.finditer(r'<h2[^>]+id="(\d{2}-\d{2}-\d{4})"[^>]+data-text="([^"]+)"[^>]*>(.*?)</h2>', html))
        
        for i in range(len(matches)):
            start_pos = matches[i].end()
            end_pos = matches[i+1].start() if i + 1 < len(matches) else len(html)
            
            section_html = html[start_pos:end_pos]
            for marker in ['<devsite-', '<div class="devsite-']:
                marker_idx = section_html.find(marker)
                if marker_idx != -1:
                    section_html = section_html[:marker_idx]
            
            # Rewrite relative links in Gemini changelog to absolute links
            section_html = re.sub(r'href="/', 'href="https://ai.google.dev/', section_html)
            
            date_id = matches[i].group(1)
            date_title = matches[i].group(2).strip()
            link = f"https://ai.google.dev/gemini-api/docs/changelog#{date_id}"
            
            entries.append({
                'source': 'gemini',
                'title': date_title,
                'date_key': parse_date_to_key(date_title),
                'link': link,
                'content': section_html.strip()
            })
    except Exception as e:
        print(f"Error fetching Gemini changelog: {e}")

    # Sort entries by date descending
    entries.sort(key=lambda x: x['date_key'], reverse=True)
    
    return jsonify({
        'status': 'success',
        'entries': entries
    })

if __name__ == '__main__':
    # Run locally on port 5000
    app.run(host='127.0.0.1', port=5000, debug=True)
