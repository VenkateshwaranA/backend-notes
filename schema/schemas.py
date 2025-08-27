def invidual_serial(note) -> dict:
    return{
        "id": str(note["_id"]),
        "title": note["title"],
        "content": note["content"]
    }


def list_serial(notes) -> list:
    return [invidual_serial(note) for note in notes]