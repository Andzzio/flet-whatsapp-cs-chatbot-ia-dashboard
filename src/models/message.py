class Message:
    def __init__(self, user: str, text: str, time: str, is_bot: bool):
        self.user = user
        self.text = text
        self.time = time
        self.is_bot = is_bot
    def to_dict(self):
        return {
            "user": self.user,
            "text": self.text,
            "time": self.time,
            "is_bot": self.is_bot
        }
    @classmethod
    def from_dict(cls, data):
        return cls(
            user=data["user"],
            text=data["text"],
            time=data["time"],
            is_bot=data["is_bot"]
        )