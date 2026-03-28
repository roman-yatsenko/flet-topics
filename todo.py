import flet as ft


def main(page: ft.Page):
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        page.update()

    new_task = ft.TextField(hint_text="Що потрібно зробити?")

    page.add(new_task, ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_clicked))


ft.run(main)
