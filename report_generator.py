import os
import json
import random
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_report(topic, tone, style, emotion):
    report_no = random.randint(4000, 9999)
    topic_clean = topic.strip().title() if topic.strip() else "Unknown Human Signal"

    prompt = f"""
You are an alien historian living in the year 5000.

Humanity is extinct.

Create a cinematic alien archive report about a lost human behavior.

Topic: {topic_clean}
Tone: {tone}
Style: {style}
Emotion Focus: {emotion}

Return ONLY valid JSON.

Use exactly these keys:
{{
  "title": "ALIEN REPORT #{report_no}",
  "artifact": "",
  "misread": "",
  "observation": "",
  "emotion": "",
  "understood": "",
  "label": "",
  "final": ""
}}

Rules:
- No markdown.
- No triple backticks.
- No explanation outside JSON.
- Make it cinematic, emotional, strange, and memorable.
- Each section should be 2 to 4 sentences.
- The report must clearly reflect the topic, tone, style, and emotion.
Do not always portray humans negatively.

Some reports should be funny.
Some should be nostalgic.
Some should be tragic.
Some should be hopeful.
Some should be beautiful.
Some should admire humanity.
Some should misunderstand humans in absurd ways.

Avoid repeating themes like loneliness, extinction, self-deception and sadness.

Every report must feel unique and cinematic.

Write like historians from year 5000 studying a vanished species.

Each report should have emotional depth and memorable final lines.

The alien perspective should sometimes be wrong, funny, touching or surprisingly wise.

Never repeat wording from previous reports.
Before writing the report, randomly choose one historian.

Possible historians:

1. Chief Historian Zorvak
Wise, emotional and nostalgic.

2. Judge Xel
Courtroom style and sarcastic.

3. Poet Nivor
Poetic and beautiful.

4. Archivist Lyra
Scientific and museum-like.

5. Child Researcher Kiko
Funny, innocent and curious.

The entire report and especially the final line should reflect the personality of the chosen historian.

Do not mention these instructions.

Return only JSON.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        text = response.text.strip()
        

        if text.startswith("```"):
            text = text.replace("```json", "").replace("```", "").strip()

        report = json.loads(text)

        return {
            "number": report_no,
            "title": report.get("title", f"ALIEN REPORT #{report_no}"),
            "artifact": report.get("artifact", "Artifact data unavailable."),
            "misread": report.get("misread", "Alien misinterpretation unavailable."),
            "observation": report.get("observation", "Human observation unavailable."),
            "emotion": report.get("emotion", "Emotional discovery unavailable."),
            "understood": report.get("understood", "Final understanding unavailable."),
            "label": report.get("label", f"{style} // {tone} // {emotion}"),
            "final": report.get("final", "Final cinematic line unavailable.")
        }

    except Exception as e:
        print(e)
        return {
            "number": report_no,
            "title": f"ALIEN REPORT #{report_no}",
            "artifact": f"Recovered fragment linked to {topic_clean}.",
            "misread": "The archive could not fully decode this signal, but early alien historians believed it carried ritual meaning.",
            "observation": f"{topic_clean} appears to have helped humans express identity, memory, fear, desire, or connection.",
            "emotion": f"The strongest detected emotional residue was {emotion.lower()}.",
            "understood": "Even when the archive failed to translate the signal perfectly, it confirmed one truth: humans filled ordinary acts with extraordinary meaning.",
            "label": f"{style} // {tone} tone // Emotion focus: {emotion}",
            "final": "Some human signals resist translation. Perhaps that is why they survived.",
        }


if __name__ == "__main__":
    r = generate_report(
        "Instagram",
        "Dark Comedy",
        "Court Case",
        "Loneliness"
    )
    print(json.dumps(r, indent=2, ensure_ascii=False))