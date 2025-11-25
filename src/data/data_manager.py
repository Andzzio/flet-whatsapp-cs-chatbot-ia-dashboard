import json
import os
from src.models.contact import Contact
import requests
import os
import json

class DataManager:
    def __init__(self):
        self.file_path = "storage/data/data.json"
        self.api_token = None
        self.contacts = {}
        self.URL = "https://django-whatsapp-cs-chatbot-ia-backend.onrender.com"
        self.load_data()
    def sync_from_server(self):
        if self.api_token == None:
            print("No hay token configurado")
            return
        try:
            headers = {
                "Authorization": self.api_token
            }
            response = requests.get(f"{self.URL}/api/sync/", headers=headers)
            if response.status_code == 200:
                data = response.json()
                server_contacts = data.get("contacts", [])
                self.contacts = {}
                for cont in server_contacts:
                    contact = Contact.from_dict(cont)
                    self.contacts[contact.name] = contact
                self.save_data()
                print("Sincronización exitosa")
        except Exception as e:
            print(e)
    def load_data(self):
        if not os.path.exists(self.file_path):
            self._create_initial_data()
            return
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.api_token = data.get("api_token")
                contact_list = data.get("contacts", [])
                for contact_data in contact_list:
                    contact = Contact.from_dict(contact_data)
                    self.contacts[contact.name] = contact
        except Exception as e:
                print(f"Error al cargar datos: {e}")
                self._create_initial_data()
    def save_data(self):
        data_to_save = {
            "api_token": self.api_token,
            "contacts": [contact.to_dict() for contact in self.contacts.values()]
        }
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data_to_save, file, indent=4, ensure_ascii=False)
    def _create_initial_data(self):
        self.contacts = {}
        ronald = Contact("Ronald S. V")
        ronald.add_message(Contact.from_dict({
            "name": "Ronald S. V",
            "history": [
                {
                    "user": "BOTY",
                    "text": "Hola Ronald, como estás.",
                    "time": "9:51",
                    "is_bot": True,
                },
            ]
            }).messages[0])
        ronald.add_message(Contact.from_dict({
            "name": "Ronald S. V",
            "history": [
                {
                    "user": "Ronald S. V",
                    "text": "Gracias necesito tu ayuda.",
                    "time": "10:00",
                    "is_bot": False,
                },
            ]
            }).messages[0])
        juan = Contact("Juan P. V")
        juan.add_message(Contact.from_dict({
            "name": "Juan P. V",
            "history": [
                {
                    "user": "BOTY",
                    "text": "Hola Juan, como estás.",
                    "time": "10:01",
                    "is_bot": True,
                },
            ]
            }).messages[0])
        juan.add_message(Contact.from_dict({
            "name": "Juan P. V",
            "history": [
                {
                    "user": "Juan P. V",
                    "text": "Gracias necesito tu ayuda.",
                    "time": "10:02",
                    "is_bot": False,
                },
            ]
            }).messages[0])
        self.contacts["MARIA L. G"] = Contact("Maria L. G")
        
        andre = Contact("ANDRE S. J")
        andre.add_message(Contact.from_dict({
            "name": "ANDRE S. J",
            "history": [
                {
                    "user": "BOTY",
                    "text": "Hola Andre, como estás.",
                    "time": "10:03",
                    "is_bot": True,
                },
            ]
        }).messages[0])
        andre.add_message(Contact.from_dict({
            "name": "ANDRE S. J",
            "history": [
                {
                    "user": "ANDRE S. J",
                    "text": "Gracias necesito tu ayuda.",
                    "time": "10:04",
                    "is_bot": False,
                },
            ]
        }).messages[0])
        self.contacts["ANDRE S. J"] = andre
        self.contacts["Ronald S. V"] = ronald
        self.contacts["Juan P. V"] = juan
        
        self.save_data()
    def get_contacts(self):
        return list(self.contacts.values())
    def get_contact(self, name):
        return self.contacts.get(name)
        