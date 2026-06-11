# Project 404: Humanity

Concept
-------
In the year 5000, an alien civilization studies extinct humanity. Users enter a human topic (e.g., Instagram, exams, cricket, money, marriage, love, food) and the app generates a funny, emotional, cinematic alien-style report.

This repository contains the initial UI skeleton and project structure using Streamlit.

Files
-----
- app.py — Streamlit app (home, create report form, about)
- requirements.txt — Python dependencies
- README.md — This file
- architecture.md — High-level architecture and notes
- .gitignore — Standard ignores

Run locally
-----------
1. Create a virtual environment (recommended)
   python -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows

2. Install dependencies
   pip install -r requirements.txt

3. Run the app
   streamlit run app.py

Notes
-----
- This is an early prototype focused on UI and UX.
- No external APIs or keys are included yet; the report generator is a placeholder.
- Designed to be Replit-friendly.