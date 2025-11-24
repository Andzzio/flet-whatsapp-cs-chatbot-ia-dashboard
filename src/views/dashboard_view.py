import flet as ft
import threading
import time
from src.data.data_manager import DataManager
from src.models.message import Message
from src.components.contact_card import ContactCard
from src.components.chat_message import ChatMessage

class DashboardView(ft.Row):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.expand = True
        self.spacing = 0
        self.is_settings_open = False
        
        self.data_manager = DataManager()
        self.current_contact = None
        
        self.message_column = ft.ListView(expand=True, reverse=True)
        self.settings_column = ft.Column([
            ft.Row([ft.Text("Token de Autenticación", size=20, weight=ft.FontWeight.BOLD, color="#6cb9f3"),
                    ft.TextField(value=self.data_manager.api_token ,hint_text="TOKEN", bgcolor=ft.Colors.WHITE, on_submit=self.save_token)],
                   alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
            ], expand=True,)
        self.entry = ft.TextField(
            hint_text="Escribe un mensaje",
            bgcolor="#d7ffff",
            filled=True,
            border_color="transparent",
            content_padding=ft.padding.all(22),
            on_submit=self.send_message
        )
        self._build_sidebar()
        self._build_chat_area()
        
        contacts = self.data_manager.get_contacts()
        if contacts:
            self.load_chat(contacts[0].name)
        self._start_background_sync()
    def _sync_loop(self):
        while True:
            self.data_manager.sync_from_server()
            if not self.is_settings_open:
                if self.current_contact:
                    self.load_chat(self.current_contact.name)
                self.update_view()
            time.sleep(5)
    def _start_background_sync(self):
        thread = threading.Thread(target=self._sync_loop, daemon=True)
        thread.start()
    def save_token(self, e):
        token = e.control.value
        self.data_manager.api_token = token
        self.data_manager.save_data()
    def toggle_settings(self, e):
        if self.is_settings_open == False:
            self.is_settings_open = True
        else:
            self.is_settings_open = False
        print(f"Settings: {self.is_settings_open}")
        self.update_view()
    def update_view(self):
        self.controls.clear()
        if self.is_settings_open:
            self._build_sidebar_settings()
            self._build_settings_area()
        else:
            self._build_sidebar()
            self._build_chat_area()
        self.update()
    def _build_sidebar_settings(self):
        self.sidebar = ft.Container(
            content=ft.Column([
                ft.Container(
                    content=ft.Column([
                        ft.Text("BOTY - CONFIGURATION", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                    ]),
                    bgcolor="#a2dcf9",
                    expand=True,
                    padding=ft.padding.only(left=15, top=15),
                ),
                ft.Container(
                    content=ft.Row([
                        ft.Container(
                            content=ft.Row([
                                ft.IconButton(ft.Icons.SETTINGS, icon_color=ft.Colors.WHITE, on_click=self.toggle_settings),
                                ft.Switch(value=False, active_color="white", active_track_color="green"),
                            ]),
                            padding=ft.padding.only(left=20),
                            
                        ),
                        ft.Container(
                            content=ft.Row([
                                ft.IconButton(ft.Icons.SHOP, icon_color=ft.Colors.WHITE),
                                
                            ], alignment=ft.MainAxisAlignment.END),
                            expand=True,
                            padding=ft.padding.only(right=20)
                        ),
                    ]),
                    bgcolor="#6cb9f3",
                    height=60,
                ),
            ], spacing=0),
            expand=1
        )
        self.controls.append(self.sidebar)
    def _build_settings_area(self):
        self.settings_area = ft.Container(
            content=ft.Column([
                ft.Container(
                    self.settings_column,
                    expand=True,
                    padding=ft.padding.only(left=20, top=20, right=20)
                    ),
            ]),
            bgcolor="#bceefc",
            expand=3,
        )
        self.controls.append(self.settings_area)
    def _build_sidebar(self):
        contact_list = []
        for contact in self.data_manager.get_contacts():
            contact_list.append(ContactCard(contact.name, self.load_chat))
        self.sidebar = ft.Container(
            content=ft.Column([
                ft.Container(
                    content=ft.Column([
                        ft.Text("BOTY - MANAGER", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                        ft.Column(contact_list, scroll=ft.ScrollMode.AUTO)
                    ]),
                    bgcolor="#a2dcf9",
                    expand=True,
                    padding=ft.padding.only(left=15, top=15),
                ),
                ft.Container(
                    content=ft.Row([
                        ft.Container(
                            content=ft.Row([
                                ft.IconButton(ft.Icons.SETTINGS, icon_color=ft.Colors.WHITE, on_click=self.toggle_settings),
                                ft.Switch(value=False, active_color="white", active_track_color="green"),
                            ]),
                            padding=ft.padding.only(left=20),
                            
                        ),
                        ft.Container(
                            content=ft.Row([
                                ft.IconButton(ft.Icons.SHOP, icon_color=ft.Colors.WHITE),
                                
                            ], alignment=ft.MainAxisAlignment.END),
                            expand=True,
                            padding=ft.padding.only(right=20)
                        ),
                    ]),
                    bgcolor="#6cb9f3",
                    height=60,
                ),
            ], spacing=0, expand=True, horizontal_alignment=ft.CrossAxisAlignment.STRETCH),
            expand=1,
        )
        self.controls.append(self.sidebar)
    
    def _build_chat_area(self):
        self.chat_area = ft.Container(
            content=ft.Column([
                ft.Container(self.message_column, expand=True),
                self.entry
            ]),
            bgcolor="#bceefc",
            expand=3,
        )
        self.controls.append(self.chat_area)
        
    def load_chat(self, contact_name):
        self.current_contact = self.data_manager.get_contact(contact_name)
        self.message_column.controls.clear()
        if self.current_contact:
            for msg in self.current_contact.messages:
                self.message_column.controls.insert(0, ChatMessage(msg))
        self.page.update()
        
    def send_message(self, e):
        if not self.entry.value or not self.current_contact:
            return
        if self.entry.value == "" or self.entry.value.strip() == "":
            return
        text = self.entry.value
        self.entry.value = ""
        
        user_msg = Message(user="BOTY", text=text, time="AHORA", is_bot=True)
        self.current_contact.add_message(user_msg)
        self.message_column.controls.insert(0, ChatMessage(user_msg))
        
        self.data_manager.save_data()
        self.page.update()