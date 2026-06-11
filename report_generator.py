import random

def generate_report(topic, tone, style, emotion):

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