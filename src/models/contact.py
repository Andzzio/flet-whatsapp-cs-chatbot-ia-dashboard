from src.models.message import Message

class Contact:
    def __init__(self, name, phone="", is_bot_active=True):
        self.name = name
        self.phone = phone
        self.is_bot_active = is_bot_active
        self.messages = []
    def add_message(self, message):
        self.messages.append(message)
    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "is_bot_active": self.is_bot_active,
            "history": [msg.to_dict() for msg in self.messages]
        }
    @classmethod
    def from_dict(cls, data):
        contact = cls(
            name=data["name"],
            phone=data.get("phone", ""),
            is_bot_active=data.get("is_bot_active", True)
            )
        if "history" in data:
            for msg_data in data["history"]:
                contact.add_message(Message.from_dict(msg_data))
        return contact