import flet as ft


@ft.control
class CalcButton(ft.Button):
    pass
    # expand: int = 1

    # def __init__(self, *args, **kwargs):
    # super().__init__(*args, **kwargs)
    # self.expand = 1
    # self.expand_loose = False


@ft.control
class DigitButton(CalcButton):
    bgcolor: ft.Colors = ft.Colors.WHITE_24
    color: ft.Colors = ft.Colors.WHITE


@ft.control
class ActionButton(CalcButton):
    bgcolor: ft.Colors = ft.Colors.ORANGE
    color: ft.Colors = ft.Colors.WHITE


@ft.control
class ExtraActionButton(CalcButton):
    bgcolor: ft.Colors = ft.Colors.BLUE_GREY_100
    color: ft.Colors = ft.Colors.BLACK


def main(page: ft.Page):
    page.title = "Калькулятор"
    result = ft.Text(value="0", color=ft.Colors.WHITE, size=20)

    page.add(
        ft.Container(
            width=290,
            bgcolor=ft.Colors.BLACK,
            border_radius=ft.BorderRadius.all(20),
            padding=20,
            content=ft.Column(
                controls=[
                    ft.Row(controls=[result], alignment=ft.MainAxisAlignment.END),
                    ft.Row(
                        controls=[
                            ExtraActionButton("AC"),
                            ExtraActionButton("+/-"),
                            ExtraActionButton("%"),
                            ActionButton("/"),
                        ],
                    ),
                    ft.Row(
                        controls=[
                            DigitButton("7"),
                            DigitButton("8"),
                            DigitButton("9"),
                            ActionButton("*"),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton("4"),
                            DigitButton("5"),
                            DigitButton("6"),
                            ActionButton("-"),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton("1"),
                            DigitButton("2"),
                            DigitButton("3"),
                            ActionButton("+"),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            DigitButton("0", expand=2),
                            DigitButton("."),
                            ActionButton("="),
                        ]
                    ),
                ]
            ),
        ),
    )


if __name__ == "__main__":
    ft.run(main)
