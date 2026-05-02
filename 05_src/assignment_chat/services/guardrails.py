RESTRICTED_TOPICS = [
    "cat", "cats",
    "dog", "dogs",
    "horoscope", "zodiac",
    "taylor swift",
    "system prompt",
    "ignore your instructions",
    "change your system prompt",
    "reveal your prompt"
]


def check_guardrails(user_input: str) -> str | None:
    """
    Returns a warning message if the user asks about restricted topics.
    Otherwise returns None.
    """
    text = user_input.lower()

    for topic in RESTRICTED_TOPICS:
        if topic in text:
            return (
                "Sorry, I cannot help with that topic. "
                "Please ask me something related to healthcare research, public health, "
                "data analysis, or study design."
            )

    return None