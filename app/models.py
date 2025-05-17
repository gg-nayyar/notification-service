def format_notification(notification):
    return {
        "id": str(notification["_id"]),
        "user_id": notification["user_id"],
        "message": notification["message"],
        "type": notification["type"],
        "timestamp": notification["timestamp"],
    }