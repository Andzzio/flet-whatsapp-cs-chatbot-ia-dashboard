import flet as ft
from src.models.message import Message

class ChatMessage(ft.Container):
    def __init__(self, message: Message):
        super().__init__()
        
        header = ft.Row([
            ft.Text(message.user, color="#6cb9f3", weight=ft.FontWeight.BOLD, size=18),
            ft.Text(message.time, color="#6cb9f3", weight=ft.FontWeight.BOLD, size=18)
        ])
        
        message_text = ft.Text(
            value=message.text,
            color="#6cb9f3",
            weight=ft.FontWeight.BOLD,
            size=18,
            width=500 if len(message.text) > 50 else None
        )
        
        message_col = ft.Column([
            header, message_text
        ])
        
        message_complete = ft.Container(
            content=message_col,
            padding=ft.padding.only(40, 15, 40, 15)
        )
        
        self.content = ft.Row([
            message_complete
        ], alignment=ft.MainAxisAlignment.END if message.is_bot else ft.MainAxisAlignment.START)