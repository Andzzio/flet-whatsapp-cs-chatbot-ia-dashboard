import flet as ft
from src.views.dashboard_view import DashboardView

def main(page: ft.Page):
    page.title = "Boty - DASHBOARD"
    page.window.width = 1440
    page.window.height = 900
    page.padding = 0
    
    dashboard = DashboardView(page)
    
    page.add(dashboard)
    
ft.app(target=main)