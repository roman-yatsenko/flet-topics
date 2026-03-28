import flet as ft


@ft.control
class ToDoApp(ft.Column):

    def init(self):
        self.new_task = ft.TextField(hint_text="Що потрібно зробити?", expand=True)
        self.tasks_view = ft.Column()
        self.width = 600
        self.controls = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        self.new_task,
                        ft.FloatingActionButton(
                            icon=ft.Icons.ADD, on_click=self.add_clicked
                        ),
                    ]
                ),
                self.tasks_view,
            ],
        )

    def add_clicked(self, e):
        self.tasks_view.controls.append(ft.Checkbox(label=self.new_task.value))
        self.new_task.value = ""
        self.update()


def main(page: ft.Page):
    page.title = "To-Do App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.width = 650
    page.update()

    todo = ToDoApp()
    page.add(todo)


ft.run(main)
