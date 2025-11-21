import flet as ft

class ContactCard(ft.Container):
    def __init__(self, name, on_click):
        super().__init__()
        self.name = name
        self.on_click = on_click
        self.content = ft.ElevatedButton(
            content=ft.Row([
                ft.Icon(ft.Icons.PERSON, color=ft.Colors.WHITE),
                ft.Text(self.name, color=ft.Colors.WHITE)
            ]),
            style=ft.ButtonStyle(
                bgcolor="#6cb9f3",
                padding=20,
            ),
            on_click=lambda e: self.on_click(self.name)
        )
        self.margin = ft.margin.only(10, 0, 20, 15)