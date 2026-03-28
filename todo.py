import flet as ft


def main(page: ft.Page):
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        page.update()

    new_task = ft.TextField(hint_text="Що потрібно зробити?", expand=True)
    tasks_view = ft.Column()
    container = ft.Column(
        width=600,
        controls=[
            ft.Row(
                controls=[
                    new_task,
                    ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_clicked),
                ]
            ),
            tasks_view,
        ],
    )

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(container)
    page.window.width = 650
    page.update()


ft.run(main)
