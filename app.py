import streamlit as st
import random
from datetime import datetime
from report_generator import generate_report
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

st.set_page_config(
    page_title="Project 404: Humanity",
    page_icon="👽",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------- CSS --------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');

.stApp {
    background:
      radial-gradient(circle at 80% 10%, rgba(87, 66, 220, 0.22), transparent 35%),
      radial-gradient(circle at 20% 20%, rgba(0, 229, 255, 0.12), transparent 30%),
      linear-gradient(135deg, #030611 0%, #050918 45%, #0b0620 100%);
    color: #eaf6ff;
    font-family: 'Inter', sans-serif;
}

[data-testid="stHeader"] { background: transparent; }
[data-testid="stToolbar"] { display: none; }

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, rgba(5,8,24,0.95), rgba(12,6,32,0.98));
    border-right: 1px solid rgba(130, 105, 255, 0.18);
}

[data-testid="stSidebar"] * {
    color: #eaf6ff !important;
}

.block-container {
    padding-top: 2rem;
    max-width: 1500px;
}

.hero {
    position: relative;
    padding: 42px;
    border-radius: 26px;
    border: 1px solid rgba(136, 105, 255, 0.35);
    background: linear-gradient(135deg, rgba(8, 13, 35, 0.92), rgba(9, 8, 28, 0.82));
    box-shadow: 0 0 60px rgba(93, 63, 211, 0.16);
    overflow: hidden;
}

.hero:before {
    content: "";
    position: absolute;
    inset: 0;
    background-image:
      linear-gradient(rgba(255,255,255,0.025) 1px, transparent 1px),
      linear-gradient(90deg, rgba(255,255,255,0.025) 1px, transparent 1px);
    background-size: 34px 34px;
    mask-image: linear-gradient(to bottom, black, transparent);
}

.kicker {
    color: #9db5ff;
    letter-spacing: 4px;
    font-size: 13px;
    font-weight: 700;
}

.big-title {
    font-size: 54px;
    line-height: 1;
    font-weight: 900;
    margin-top: 18px;
    background: linear-gradient(90deg, #ffffff, #9cecff, #b69cff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    color: #b9caff;
    font-size: 22px;
    margin-top: 22px;
}

.bodytext {
    color: #d7e5ff;
    font-size: 16px;
    line-height: 1.7;
    max-width: 780px;
}

.glass-card {
    border-radius: 22px;
    border: 1px solid rgba(123, 95, 255, 0.30);
    background: linear-gradient(135deg, rgba(10, 15, 39, 0.88), rgba(7, 10, 26, 0.78));
    box-shadow: 0 0 45px rgba(0, 217, 255, 0.06);
    padding: 26px;
    margin-bottom: 22px;
}

.stat-card {
    border-radius: 18px;
    border: 1px solid rgba(0, 229, 255, 0.20);
    background: rgba(8, 13, 35, 0.72);
    padding: 26px;
    box-shadow: inset 0 0 22px rgba(0, 229, 255, 0.03);
}

.stat-number {
    color: #20f3ff;
    font-size: 30px;
    font-weight: 900;
}

.stat-label {
    color: #a9bde5;
    margin-top: 8px;
    font-size: 14px;
}

.signal-card {
    border-radius: 18px;
    border: 1px solid rgba(142, 101, 255, 0.28);
    background: linear-gradient(135deg, rgba(22, 16, 56, 0.72), rgba(7, 13, 34, 0.72));
    padding: 22px;
    min-height: 92px;
}

.signal-title {
    color: #ffffff;
    font-weight: 800;
    font-size: 18px;
}

.signal-sub {
    color: #9fb7d9;
    font-size: 13px;
    margin-top: 8px;
}

.radar {
    height: 280px;
    border-radius: 26px;
    border: 1px solid rgba(0,229,255,.12);
    background:
      radial-gradient(circle at center, rgba(0,229,255,.28) 0 8%, transparent 9%),
      radial-gradient(circle at center, transparent 0 24%, rgba(0,229,255,.08) 25%, transparent 26%),
      radial-gradient(circle at center, transparent 0 42%, rgba(151,102,255,.10) 43%, transparent 44%),
      radial-gradient(circle at center, rgba(0,229,255,.12), transparent 55%),
      linear-gradient(135deg, rgba(10, 23, 45, .85), rgba(23, 11, 53, .85));
    box-shadow: 0 0 55px rgba(0,229,255,.10);
    position: relative;
    overflow: hidden;
}

.radar:after {
    content: "";
    position: absolute;
    width: 46%;
    height: 46%;
    left: 27%;
    top: 27%;
    border-radius: 50%;
    border: 1px solid rgba(168, 134, 255, .28);
    box-shadow: 0 0 40px rgba(111, 77, 255, .20);
}

.sidebar-logo {
    display:flex;
    align-items:center;
    gap:14px;
    margin-top:22px;
    margin-bottom:28px;
}
.logo-mark {
    width:58px;height:58px;border-radius:16px;
    display:flex;align-items:center;justify-content:center;
    background:linear-gradient(135deg, rgba(0,229,255,.16), rgba(152,100,255,.22));
    border:1px solid rgba(157,123,255,.25);
    font-size:26px;
}
.side-title {
    font-weight:900;
    letter-spacing:3px;
    font-size:14px;
}
.side-sub {
    color:#a9bde5 !important;
    font-size:13px;
    margin-top:3px;
}
.quote {
    margin-top:42px;
    border-radius:18px;
    padding:20px;
    border:1px solid rgba(123,95,255,.25);
    background:rgba(8,13,35,.72);
    color:#eaf6ff;
    font-weight:700;
    line-height:1.5;
}
.quote span {
    display:block;
    text-align:right;
    margin-top:16px;
    color:#9fb7d9;
    font-weight:500;
}

.stButton > button {
    width: 100%;
    border-radius: 14px !important;
    border: 1px solid rgba(0,229,255,.25) !important;
    color: #eaf6ff !important;
    font-weight: 800 !important;
    background: linear-gradient(135deg, rgba(0,229,255,.16), rgba(132,82,255,.28)) !important;
    padding: 0.75rem 1rem !important;
    box-shadow: 0 0 25px rgba(111, 77, 255, .12);
}
div[data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(135deg, #00e5ff, #8b5cf6) !important;
    color: #ffffff !important;
    border: 1px solid rgba(0, 229, 255, 0.55) !important;
    border-radius: 16px !important;
    font-weight: 900 !important;
    letter-spacing: 1px !important;
    padding: 0.9rem 1.4rem !important;
    box-shadow: 0 0 35px rgba(0, 229, 255, 0.22) !important;
}

div[data-testid="stFormSubmitButton"] > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 0 45px rgba(139, 92, 246, 0.35) !important;
}
.stButton > button:hover {
    border-color: rgba(0,229,255,.65) !important;
    box-shadow: 0 0 35px rgba(0,229,255,.18);
    transform: translateY(-1px);
}
            .stDownloadButton > button {
    background: linear-gradient(135deg, #00e5ff, #8b5cf6) !important;
    color: white !important;
    border: 1px solid rgba(0,229,255,.5) !important;
    border-radius: 16px !important;
    font-weight: 900 !important;
    padding: 0.9rem 1.4rem !important;
    box-shadow: 0 0 35px rgba(0,229,255,.2) !important;
}

.stDownloadButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 0 45px rgba(139,92,246,.35) !important;
}

.main-btn button {
    max-width: 360px;
}

input, textarea, select {
    border-radius: 14px !important;
}

[data-testid="stTextInput"] input {
    background: rgba(8, 13, 35, 0.92) !important;
    color: #eaf6ff !important;
    border: 1px solid rgba(0, 229, 255, 0.28) !important;
    border-radius: 14px !important;
}

[data-testid="stTextInput"] input::placeholder {
    color: #7890b5 !important;
}

[data-baseweb="select"] > div {
    background: rgba(8, 13, 35, 0.92) !important;
    color: #eaf6ff !important;
    border: 1px solid rgba(0, 229, 255, 0.28) !important;
    border-radius: 14px !important;
}

[data-baseweb="select"] span {
    color: #eaf6ff !important;
}

.result-title {
    font-size: 34px;
    font-weight: 900;
    color: #ffffff;
}
.section-label {
    color:#20f3ff;
    letter-spacing:2px;
    font-size:12px;
    font-weight:900;
    margin-bottom:8px;
}
.timeline-item {
    border-left: 3px solid #20f3ff;
    padding-left: 18px;
    margin-bottom: 22px;
}
</style>
""", unsafe_allow_html=True)

# -------------------- STATE --------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

# -------------------- SIDEBAR --------------------
with st.sidebar:
    st.markdown("""
    <div class="sidebar-logo">
      <div class="logo-mark">👽</div>
      <div>
        <div class="side-title">PROJECT 404</div>
        <div class="side-sub">Humanity Archive</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Home"):
        st.session_state.page = "Home"
    if st.button("Create Report"):
        st.session_state.page = "Create Report"
    if st.button("About"):
        st.session_state.page = "About"

    st.markdown("""
    <div class="quote">
    "The only way to understand a species is to study what they left behind."
    <span>— Chief Historian Zorvak</span>
    </div>
    """, unsafe_allow_html=True)

# -------------------- HELPERS --------------------
def demo_report(topic, tone, style, emotion):

    import random

    topic_clean = topic.strip().title() if topic.strip() else "Unknown Human Signal"
    report_no = random.randint(4000, 9999)

    topic_data = {
        "Instagram": {
            "artifact": "a palm-sized glowing mirror containing frozen faces, arranged meals, sunsets, and repeated symbols of approval",
            "misread": "The first alien team classified Instagram as a vanity shrine. They believed humans placed their faces inside light-boxes to request blessings from invisible crowds.",
            "observation": "Further study showed humans were not only showing life; they were editing it into proof that they existed beautifully. Every image was a small attempt to be seen, remembered, and approved.",
        },
        "Cricket": {
            "artifact": "a cracked wooden ritual stick, a red leather sphere, and crowd-noise recordings from circular arenas",
            "misread": "Researchers first believed cricket was a seasonal war ceremony where humans defended three sacred sticks from a red flying planet.",
            "observation": "The game was not war. It was patience, suspense, loyalty, and shared heartbreak disguised as sport. Millions paused their lives to follow tiny movements of bat, ball, and hope.",
        },
        "Exams": {
            "artifact": "paper sheets marked with fear, erased answers, temporary memory, and silent prayers",
            "misread": "The archive initially believed exams were punishment rituals used to measure how long young humans could survive without sleep.",
            "observation": "Exams were gates. Humans compressed months of learning into a few anxious hours, believing marks could decide identity, respect, and future direction.",
        },
        "Money": {
            "artifact": "rectangular value papers, metallic discs, and invisible numbers stored in ancient banking clouds",
            "misread": "Aliens first believed money was a sacred spell because humans exchanged it for food, shelter, status, and sometimes dignity.",
            "observation": "Money was not just currency. It was stored fear, imagined freedom, family pressure, ambition, survival, and power compressed into symbols.",
        },
        "Marriage": {
            "artifact": "gold rings, flower remains, dance recordings, ceremonial fabrics, and guest lists longer than military scrolls",
            "misread": "The first report called marriage a colorful diplomatic treaty involving food overload, synchronized dancing, and expensive fabric signaling.",
            "observation": "Marriage was both ritual and promise. Humans gathered witnesses because love, for them, became more real when society agreed to remember it.",
        },
        "Love": {
            "artifact": "unanswered messages, faded photographs, handwritten notes, playlists, and preserved voice recordings",
            "misread": "Aliens believed love was a neurological malfunction that made humans behave against logic while smiling at glowing rectangles.",
            "observation": "Love made humans irrational, brave, foolish, patient, jealous, poetic, and alive. It was the force that made ordinary days feel historically important.",
        },
        "Food": {
            "artifact": "burnt cooking vessels, spice dust, family table maps, and recipes carried across generations",
            "misread": "The archive first classified food as fuel preparation. This was incorrect. Humans were clearly cooking emotions.",
            "observation": "Food was memory with temperature. Families used meals to apologize, celebrate, welcome, mourn, and keep ancestors alive through taste.",
        },
        "Politics": {
            "artifact": "broken banners, debate clips, ink-stained fingers, and speeches preserved in public memory archives",
            "misread": "Aliens first believed politics was a noise competition where groups shouted until reality changed shape.",
            "observation": "Politics was the human struggle to decide who gets heard, who gets resources, and whose version of the future becomes law.",
        },
    }

    data = topic_data.get(topic_clean, {
        "artifact": f"a mysterious archive fragment connected to the human signal called {topic_clean}",
        "misread": f"The first researchers could not classify {topic_clean}. They suspected it was either a ritual, a game, a warning, or an emotional machine.",
        "observation": f"Repeated appearances of {topic_clean} suggest it carried emotional weight. Humans returned to it when ordinary language was not enough.",
    })

    tone_lines = {
        "Funny": {
            "prefix": "The junior historians laughed for fourteen moon-cycles before admitting the humans may have been serious.",
            "final": "Humanity remains the only species that could turn confusion into a group activity and still call it culture.",
        },
        "Emotional": {
            "prefix": "The archive treated this finding carefully because the emotional residue was unusually warm.",
            "final": "What survived was not the object itself, but the feeling humans placed inside it.",
        },
        "Documentary": {
            "prefix": "Cross-referenced evidence confirms this practice appeared across regions, classes, and generations.",
            "final": "The record suggests this signal was not accidental. It was a repeated structure in human civilization.",
        },
        "Dark Comedy": {
            "prefix": "The council noted, with concern, that humans often invented stress and then built ceremonies around it.",
            "final": "A tragic species, certainly. But impressively committed to making everything complicated.",
        },
        "Poetic": {
            "prefix": "The fragment glows softly in the archive, like a star that forgot it had already died.",
            "final": "In the silence after humanity, this signal still hums like a small heart under glass.",
        },
    }

    emotion_lines = {
        "Happiness": {
            "discovery": f"The strongest residue around {topic_clean} was happiness. Not loud happiness, but the shared kind — the feeling of belonging to a moment with others.",
            "ending": f"Perhaps {topic_clean} mattered because it gave humans permission to feel joy together.",
        },
        "Fear": {
            "discovery": f"The emotional layer carried fear: fear of failing, losing, being forgotten, or not becoming enough.",
            "ending": f"Perhaps {topic_clean} was not about control. Perhaps it was how humans negotiated with uncertainty.",
        },
        "Love": {
            "discovery": f"Love appeared as the hidden gravity inside this signal. Humans used {topic_clean} to move closer to each other, even when they did not know how to say it directly.",
            "ending": f"Perhaps love was humanity's most advanced technology: invisible, unstable, and impossible to fully archive.",
        },
        "Ambition": {
            "discovery": f"Ambition burned strongly in the record. {topic_clean} became a ladder, a scoreboard, or a stage where humans tried to become more than yesterday.",
            "ending": f"Perhaps humans were not chasing success. Perhaps they were chasing evidence that their effort meant something.",
        },
        "Loneliness": {
            "discovery": f"Loneliness was found beneath the surface. Even in crowded rituals, humans seemed to ask: does anyone truly see me?",
            "ending": f"Perhaps {topic_clean} was a bridge built by a species terrified of being alone.",
        },
        "Nostalgia": {
            "discovery": f"Nostalgia surrounded the artifact like dust around old light. Humans used {topic_clean} to return to versions of themselves they could no longer touch.",
            "ending": f"Perhaps memory was humanity's way of refusing to let time win completely.",
        },
    }

    style_lines = {
        "Museum Exhibit": {
            "label": f"Exhibit 404-{report_no}: {topic_clean}, preserved under emotional glass.",
            "understood": f"Curator's note: {topic_clean} should not be viewed as a simple habit. It was a container for memory, pressure, identity, and fragile hope.",
        },
        "Alien Research Paper": {
            "label": f"Hypothesis Archive {report_no}: {topic_clean} as emotional infrastructure.",
            "understood": f"Analysis indicates that {topic_clean} functioned as a social-emotional system. Conclusion: humans repeatedly converted ordinary objects into meaning.",
        },
        "Lost Diary": {
            "label": f"Private diary fragment of Historian Zorvak, entry #{report_no}.",
            "understood": f"I expected to study a dead species. Instead, {topic_clean} made me feel as if the humans were still whispering from the debris.",
        },
        "News Broadcast": {
            "label": f"Archive Bulletin #{report_no}: breaking discovery related to {topic_clean}.",
            "understood": f"Breaking update from the excavation floor: researchers now believe {topic_clean} was not random behavior, but a major emotional signal from the vanished species.",
        },
        "Court Case": {
            "label": f"Case #{report_no}: The Archive vs. {topic_clean}.",
            "understood": f"Verdict: {topic_clean} is guilty of confusing alien researchers, but innocent of being meaningless. Evidence proves it carried emotional and cultural weight.",
        },
    }

    selected_tone = tone_lines.get(tone, tone_lines["Documentary"])
    selected_emotion = emotion_lines.get(emotion, emotion_lines["Nostalgia"])
    selected_style = style_lines.get(style, style_lines["Museum Exhibit"])

    artifact = data["artifact"]
    misread = f"{data['misread']} {selected_tone['prefix']}"
    observation = data["observation"]
    emotional_discovery = selected_emotion["discovery"]
    understood = selected_style["understood"]
    label = selected_style["label"]
    final_line = f"{selected_emotion['ending']} {selected_tone['final']}"

    return {
        "number": report_no,
        "title": f"ALIEN REPORT #{report_no}",
        "artifact": artifact,
        "misread": misread,
        "observation": observation,
        "emotion": emotional_discovery,
        "understood": understood,
        "label": label,
        "final": final_line,
    }
def card(title, body):
    st.markdown(f"""
    <div class="glass-card">
      <div class="section-label">{title.upper()}</div>
      <div class="bodytext">{body}</div>
    </div>
    """, unsafe_allow_html=True)

# -------------------- PAGES --------------------
if st.session_state.page == "Home":
    c1, c2 = st.columns([1.7, 1])
    with c1:
        st.markdown("""
        <div class="hero">
          <div class="kicker">ALIEN HISTORICAL ARCHIVE // YEAR 5000</div>
          <div class="big-title">PROJECT 404: HUMANITY</div>
          <div class="subtitle">A Species Remembered by Strangers.</div>
          <p class="bodytext">
          In the distant future, alien historians study the fragile remains of humanity:
          social rituals, games, love patterns, ambition, fear, food, money, and memory.
          Each report is a cinematic reconstruction of what humans may have been trying to say.
          </p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="radar"></div>', unsafe_allow_html=True)

    st.write("")
    s1, s2, s3 = st.columns(3)
    with s1:
        st.markdown('<div class="stat-card"><div class="stat-number">12,847</div><div class="stat-label">Artifacts Cataloged</div></div>', unsafe_allow_html=True)
    with s2:
        st.markdown('<div class="stat-card"><div class="stat-number">3,582</div><div class="stat-label">Reports Generated</div></div>', unsafe_allow_html=True)
    with s3:
        st.markdown('<div class="stat-card"><div class="stat-number">98.7%</div><div class="stat-label">Archive Integrity</div></div>', unsafe_allow_html=True)

    st.write("")
    st.markdown("### Recovered Human Signals")
    a, b, c, d = st.columns(4)
    for col, title, sub in [
        (a, "Social Rituals", "Belonging disguised as performance."),
        (b, "Competitive Games", "Joy hidden inside conflict."),
        (c, "Memory Devices", "Tiny machines that preserved longing."),
        (d, "Love Patterns", "The most confusing human technology."),
    ]:
        with col:
            st.markdown(f'<div class="signal-card"><div class="signal-title">{title}</div><div class="signal-sub">{sub}</div></div>', unsafe_allow_html=True)

elif st.session_state.page == "Create Report":
    st.markdown('<div class="big-title">INVESTIGATION CONSOLE</div>', unsafe_allow_html=True)
    st.markdown(
        '<p class="bodytext">Search one lost human signal and let the archive prepare a cinematic alien dossier.</p>',
        unsafe_allow_html=True
    )

    left, right = st.columns([1.15, 0.85])

    with left:
        st.markdown("""
        <div class="glass-card">
          <div class="section-label">HUMAN SIGNAL INPUT</div>
          <h2 style="margin-top:0;color:#eaf6ff;">Build Your Dossier</h2>
          <p class="bodytext">Choose how alien historians should study this recovered human behavior.</p>
        </div>
        """, unsafe_allow_html=True)

        with st.form("report_form"):
            topic = st.text_input(
                "Human Topic",
                placeholder="Search ancient signal... e.g. Instagram, Cricket, Exams, Money"
            )

            tone = st.selectbox(
                "Investigation Tone",
                ["Funny", "Emotional", "Documentary", "Dark Comedy", "Poetic"],
                index=None,
                placeholder="Choose tone..."
            )

            style = st.selectbox(
                "Dossier Format",
                ["Museum Exhibit", "Alien Research Paper", "Lost Diary", "News Broadcast", "Court Case"],
                index=None,
                placeholder="Choose report style..."
            )

            emotion = st.selectbox(
                "Emotional Residue",
                ["Happiness", "Fear", "Love", "Ambition", "Loneliness", "Nostalgia"],
                index=None,
                placeholder="Choose emotion focus..."
            )

            submitted = st.form_submit_button("BEGIN HUMAN INVESTIGATION")

    with right:
        preview_topic = topic.strip().title() if "topic" in locals() and topic.strip() else "Unknown"
    preview_status = "Ready to Scan" if preview_topic != "Unknown" else "Waiting for Input"
    preview_signal = preview_topic if preview_topic != "Unknown" else "Unknown Human Signal"

    st.markdown(f"""
    <div class="glass-card">
      <div class="section-label">LIVE ARTIFACT SCANNER</div>
      <h2 style="margin-top:0;color:#eaf6ff;">{preview_status}</h2>
      <p class="bodytext">
      This scanner previews the human signal before the archive creates the final dossier.
      </p>

      <div class="radar" style="height:300px;margin-top:22px;"></div>

      <p class="bodytext" style="margin-top:22px;">
      <b>Archive Node:</b> A-13<br>
      <b>Status:</b> {preview_status}<br>
      <b>Detected Signal:</b> {preview_signal}<br>
      <b>Archive Year:</b> 5000
      </p>
    </div>
    """, unsafe_allow_html=True)

    if submitted:
        if not topic or not tone or not style or not emotion:
            st.warning("Please complete all investigation fields first.")
        else:
            r = generate_report(topic, tone, style, emotion)

            st.write("")
            st.markdown(f"""
            <div class="hero">
              <div class="kicker">ARCHIVAL DOSSIER // YEAR 5000</div>
              <div class="result-title">{r['title']}</div>
              <div class="subtitle">{topic.title()} — Recovered Human Signal</div>
              <p class="bodytext">{r['label']}</p>
            </div>
            """, unsafe_allow_html=True)

            l, rr = st.columns(2)

            report_text = f"""
{r['title']}

Topic: {topic.title()}
Tone: {tone}
Style: {style}
Emotion Focus: {emotion}

ARTIFACT FOUND
{r['artifact']}

ALIEN MISINTERPRETATION
{r['misread']}

HUMAN OBSERVATION
{r['observation']}

EMOTIONAL DISCOVERY
{r['emotion']}

WHAT ALIENS FINALLY UNDERSTOOD
{r['understood']}

MUSEUM LABEL
{r['label']}

FINAL LINE
{r['final']}
"""

            buffer = BytesIO()

            doc = SimpleDocTemplate(
                buffer,
                rightMargin=42,
                leftMargin=42,
                topMargin=42,
                bottomMargin=42
            )

            styles = getSampleStyleSheet()
            story = []

            title_style = styles["Title"]
            title_style.textColor = colors.HexColor("#101827")
            title_style.fontSize = 22
            title_style.leading = 28

            section_style = styles["Heading2"]
            section_style.textColor = colors.HexColor("#111827")
            section_style.fontSize = 12
            section_style.leading = 16
            section_style.spaceAfter = 6

            body_style = styles["BodyText"]
            body_style.textColor = colors.HexColor("#273449")
            body_style.fontSize = 10.5
            body_style.leading = 15

            small_style = styles["BodyText"]
            small_style.textColor = colors.HexColor("#52627A")
            small_style.fontSize = 9
            small_style.leading = 12

            story.append(Paragraph("PROJECT 404: HUMANITY", title_style))
            story.append(Paragraph("ALIEN HISTORICAL ARCHIVE // YEAR 5000", small_style))
            story.append(Spacer(1, 0.2 * inch))

            story.append(Paragraph(r["title"], section_style))
            story.append(Paragraph(f"Topic: {topic.title()} | Tone: {tone} | Style: {style} | Emotion: {emotion}", small_style))
            story.append(Spacer(1, 0.25 * inch))

            sections = [
                ("ARTIFACT FOUND", r["artifact"]),
                ("ALIEN MISINTERPRETATION", r["misread"]),
                ("HUMAN OBSERVATION", r["observation"]),
                ("EMOTIONAL DISCOVERY", r["emotion"]),
                ("WHAT ALIENS FINALLY UNDERSTOOD", r["understood"]),
                ("MUSEUM LABEL", r["label"]),
                ("FINAL LINE", r["final"]),
            ]

            for heading, body in sections:
                card_table = Table(
                    [[Paragraph(f"<b>{heading}</b>", section_style)],
                    [Paragraph(body, body_style)]],
                    colWidths=[6.8 * inch]
                )

                card_table.setStyle(TableStyle([
                    ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F5F7FF")),
                    ("BOX", (0, 0), (-1, -1), 0.8, colors.HexColor("#B7C7FF")),
                    ("LEFTPADDING", (0, 0), (-1, -1), 12),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                    ("TOPPADDING", (0, 0), (-1, -1), 10),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
                ]))

                story.append(card_table)
                story.append(Spacer(1, 0.16 * inch))

            story.append(Spacer(1, 0.2 * inch))
            story.append(Paragraph("Recovered by Project 404 Archive Node A-13", small_style))

            doc.build(story)

            pdf_data = buffer.getvalue()
            buffer.close()
            st.download_button(
                        label="DOWNLOAD DOSSIER PDF",
                        data=pdf_data,
                        file_name=f"project_404_{topic.lower().replace(' ', '_')}.pdf",
                        mime="application/pdf"
                    )

elif st.session_state.page == "About":

    st.markdown(
        '<div class="big-title">ABOUT PROJECT 404</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="glass-card">
            <p class="bodytext">
            Project 404 is a cinematic creative app where an alien civilization studies extinct humanity
            through artifacts, rituals, memories, and emotional signals. It is designed as an immersive
            digital museum experience.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### Timeline")

    st.markdown(
        """
        <div class="glass-card">
            <div class="timeline-item">
                <b>Year 2197</b><br>
                Humanity disappeared, leaving behind scattered signals.
            </div>

            <div class="timeline-item">
                <b>Year 4031</b><br>
                The first human artifacts were recovered from forgotten data vaults.
            </div>

            <div class="timeline-item">
                <b>Year 5000</b><br>
                Project 404 was established to understand the species through what they left behind.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )