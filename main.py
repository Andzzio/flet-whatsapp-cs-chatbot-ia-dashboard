import flet as ft

def main(page: ft.Page):
    page.title = "Boty - DASHBOARD"
    page.window.width = 1440
    page.window.height = 900
    page.padding = 0
    current_contact = "RONALD S. V"
    
    chat_history = {
        "RONALD S. V": [
            {
                "msg": "Hola Ronald, bienvenido.",
                "user": "BOTY",
                "time": "9:00",
                "isBot": True,
            },
            {
                "msg": "Gracias, necesito tu ayuda.",
                "user": "RONALD S. V",
                "time": "9:05",
                "isBot": False,
            }
        ],
        "JUAN P. H": [
            {
                "msg": "Juan tu pedido está listo.",
                "user": "BOTY",
                "time": "10:00",
                "isBot": True,
            }
        ],
        "MARIA L. G": [
            
        ],
        "ANDRE S. J": [
            {
                "msg": "Hola en que podemos ayudarte.",
                "user": "BOTY",
                "time": "9:30",
                "isBot": True,
            }
        ]
    }
    
    def create_contact(name):
        contact = ft.ElevatedButton(
            content=ft.Row([
                ft.Icon(ft.Icons.PERSON, color=ft.Colors.WHITE),
                ft.Text(name, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD, size=18),
            ]),
            style=ft.ButtonStyle(
                bgcolor="#6cb9f3",
                padding=20,
            ),
            on_click= lambda e: load_chat_for_contact(name)
        )
        finale_result = ft.Container(
            content=contact,
            margin=ft.margin.only(10, 0, 20, 15),
        )
        
        return finale_result
    
    def create_message(message, user, time, isBot = True):
        data = ft.Row([
                            ft.Text(user, color="#6cb9f3", weight=ft.FontWeight.BOLD, size=18),
                            ft.Text(time, color="#6cb9f3", weight=ft.FontWeight.BOLD, size=18)
                            ])
        if len(message)>50:
            message_complete = ft.Container(
                ft.Column([
                        data,
                        ft.Text(value=message, color="#6cb9f3", weight=ft.FontWeight.BOLD, size=18, width=500),
                    ]),
                padding=ft.padding.only(left=40, top=15, right=40, bottom=15),
            )
        else:
            message_complete = ft.Container(
                ft.Column([
                        data,
                        ft.Text(value=message, color="#6cb9f3", weight=ft.FontWeight.BOLD, size=18),
                    ]),
                padding=ft.padding.only(left=40, top=15, right=40, bottom=15),
                )
        if isBot:
            return ft.Container(
                ft.Row([
                    message_complete
                ], alignment=ft.MainAxisAlignment.END)
            )
        else:
            return ft.Container(
                ft.Row([
                    message_complete
                ], alignment=ft.MainAxisAlignment.START)
            )
    
    def send_message(e):
        if entry.value and entry.value.strip():
            entry_value = entry.value
            entry.value = ""
            new_message_data = {
                "msg": entry_value,
                "user": "BOTY",
                "time": "AHORA",
                "isBot": True,
            }
            if current_contact not in chat_history:
                chat_history[current_contact] = []
            chat_history[current_contact].append(new_message_data)
            new_message = create_message(entry_value, "BOTY", "AHORA")
            message_column.controls.insert(0, new_message)
            page.update()
    def load_chat_for_contact(contact_name):
        nonlocal current_contact
        current_contact = contact_name
        
        message_column.controls.clear()
        
        if contact_name in chat_history:
            history = chat_history[contact_name]
            for msg_data in history:
                msg_widget = create_message(
                    msg_data['msg'],
                    msg_data['user'],
                    msg_data['time'],
                    msg_data['isBot'],
                )
                message_column.controls.insert(0, msg_widget)
        page.update()
    
    message_column = ft.ListView([
            
        ],
        reverse=True,
        expand=True
    )
    entry = ft.TextField(
                hint_text="Escribe un mensaje",
                bgcolor="#d7ffff",
                filled=True,
                border_color="transparent",
                content_padding=ft.padding.all(22),
                on_submit=send_message
                )   
    
    sidebar_main = ft.Container(
        ft.Column([
            ft.Container(
                    ft.Column([
                            ft.Row([
                                ft.Text("BOTY - MANAGER", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                            ]),
                            create_contact("RONALD S. V"),
                            create_contact("JUAN P. H"),
                            create_contact("MARIA L. G"),
                            create_contact("ANDRE S. J"),
                        ],scroll=ft.ScrollMode.AUTO),
                    bgcolor="#a2dcf9",
                    expand=True,
                    alignment=ft.alignment.top_left,
                    padding=ft.padding.only(left=15, top=15),
                ),
            ft.Container(
                    ft.Row([
                        ft.Container(
                            ft.Row([
                                ft.IconButton(ft.Icons.SETTINGS),
                                ft.Switch(value=True),
                            ]),
                            padding=ft.padding.only(left=20),
                            ),
                        ft.Container(
                            ft.Row([
                                ft.IconButton(ft.Icons.SHOP),
                            ], alignment=ft.MainAxisAlignment.END),
                            expand=True,
                            padding=ft.padding.only(right=20),
                        ),
                        ]),
                    bgcolor="#6cb9f3",
                    height=60,
                ),

        ], spacing=0),
        expand=1,
    )
    chat_main = ft.Container(
        ft.Column([
            ft.Container(
                message_column,
                expand=True,
                ),
            entry
        ]),
        bgcolor="#bceefc",
        expand=3,
    )
    
    main_page = ft.Row([
        sidebar_main, chat_main
    ], expand=True, spacing=0)
    
    page.add(main_page)
    page.update()
    
ft.app(main)