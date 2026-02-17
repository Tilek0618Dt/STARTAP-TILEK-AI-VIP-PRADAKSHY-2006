def apply_style(user, ai_text):

    styles = [
        f"😎 Досум… {ai_text} 😂🔥",
        f"😈 Эхе… {ai_text} API деле чарчап калды 😭",
        f"🧠 {ai_text}\n\nСен чын эле ойлонуп жатасыңбы?"
    ]

    index = user.style_counter % 3
    styled = styles[index]

    user.style_counter += 1

    return styled
