from src.models.message import Message

class Contact:
    def __init__(self, name):
        self.name = name
        self.messages = []
    def add_message(self, message):
        self.messages.append(message)
    def to_dict(self):
        return {
            "name": self.name,
            "history": [msg.to_dict() for msg in self.messages]
        }
    @classmethod
    def from_dict(cls, data):
        contact = cls(data["name"])
        if "history" in data:
            for msg_data in data["history"]:
                contact.add_message(Message.from_dict(msg_data))
        return contact