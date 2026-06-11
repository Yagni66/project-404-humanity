# Architecture — Project 404: Humanity (initial)

This document describes the current minimal architecture and planned components.

Current (v0)
------------
- Single Streamlit frontend (`app.py`) with:
  - Home page (title, tagline, explanation, Start button)
  - Sidebar navigation: Home / Create Report / About
  - Create Report page: form fields (topic, tone, style, emotion) and a placeholder result area
- No backend or external services. Everything runs in-process in Streamlit.

Planned (future)
---------------
- Report generation component (AI/text engine)
  - Could be an internal model or an API-backed service
  - Will be called after form submission; responses rendered in the app
- Templates and orchestration
  - Template system for different report styles and tones
  - Retry / caching / rate-limiting if external APIs are used
- Persistence
  - Optional: save generated reports, allow browsing past reports
- Tests and CI
  - Unit tests for templating logic and form validation
  - CI to run linting and minimal app checks

Notes on design choices
-----------------------
- Keep UI minimal and friendly for quick iteration (Replit / local)
- Start with in-app placeholders to separate UI work from AI integration
- Accessibility and clear copy are priorities for storytelling-focused UX