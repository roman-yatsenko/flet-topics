import flet as ft


@ft.control
class CalcButton(ft.Button):

    def init(self):
        if not self.expand:
            self.expand = 1


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


@ft.control
class CalculatorApp(ft.Container):

    def init(self):
        self.reset()
        self.width = 350
        self.bgcolor = ft.Colors.BLACK
        self.border_radius = ft.BorderRadius.all(20)
        self.padding = 20
        self.result = ft.Text(value="0", color=ft.Colors.WHITE, size=20)

        self.content = ft.Column(
            controls=[
                ft.Row(controls=[self.result], alignment=ft.MainAxisAlignment.END),
                ft.Row(
                    controls=[
                        ExtraActionButton("AC", on_click=self.button_clicked),
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
                        DigitButton("1", on_click=self.button_clicked),
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
        )

    def button_clicked(self, event):
        data = event.control.content
        if data == "AC":
            self.result.value = "0"
        elif data == "1":
            self.result.value = "1"

    def reset(self):
        self.operator = "+"
        self.operand1 = 0
        self.new_operand = True


def main(page: ft.Page):
    page.title = "Калькулятор"
    calc = CalculatorApp()
    page.add(calc)


if __name__ == "__main__":
    ft.run(main)
