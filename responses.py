def handle_response(message) -> str:
    p_message = message.lower()

    if p_message in ("hi", "hello", "嗨", "哈嘍"):
        return 'Hi!!'
    elif "煙火" in p_message or "firework" in p_message.lower():
        return '"Boom! 🎆🎇"'
