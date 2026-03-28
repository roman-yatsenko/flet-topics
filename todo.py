from dataclasses import field
from typing import Callable

import flet as ft


@ft.control
class Task(ft.Column):
    task_name: str = ""
    on_task_delete: Callable[["Task"], None] = field(default=lambda task: None)

    def init(self):
        self.display_task = ft.Checkbox(value=False, label=self.task_name, expand=True)
        self.edit_name = ft.TextField(expand=1)

        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_task,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.CREATE_OUTLINED,
                            tooltip="Змінити",
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(
                            icon=ft.Icons.DELETE_OUTLINE,
                            tooltip="Видалити",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                ft.IconButton(
                    icon=ft.Icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.Colors.GREEN,
                    tooltip="Зберегти",
                    on_click=self.save_clicked,
                ),
            ],
        )
        self.controls = [self.display_view, self.edit_view]

    def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def delete_clicked(self, e):
        self.on_task_delete(self)


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
        task = Task(task_name=self.new_task.value, on_task_delete=self.task_delete)
        self.tasks_view.controls.append(task)
        self.new_task.value = ""
        self.update()

    def task_delete(self, task):
        self.tasks_view.controls.remove(task)
        self.update()


def main(page: ft.Page):
    page.title = "To-Do App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.width = 650
    page.update()

    todo = ToDoApp()
    page.add(todo)


ft.run(main)
