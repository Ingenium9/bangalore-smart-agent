def detect_persona(query):
    query = query.lower()
    if any(word in query for word in ["just visiting", "weekend", "trip", "vacation", "sightseeing"]):
        return "tourist"
    elif any(word in query for word in ["moving", "relocating", "job", "shifting", "work", "staying"]):
        return "resident"
    return "unknown"
