from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import math


class FinalCalcLayout(BoxLayout):
    history = []

    def clear_display(self):
        self.ids.display.text = ""

    def calculate(self):
        try:
            expr = self.ids.display.text
            result = str(eval(expr))
            self.ids.display.text = result
            FinalCalcLayout.history.append(f"{expr} = {result}")
            if len(FinalCalcLayout.history) > 5:
                FinalCalcLayout.history.pop(0)
        except Exception:
            self.ids.display.text = "Ошибка"

    def power(self):
        try:
            expr = self.ids.display.text
            result = str(eval(expr + "**2"))
            self.ids.display.text = result
            FinalCalcLayout.history.append(f"{expr}² = {result}")
        except:
            self.ids.display.text = "Ошибка"

    def sqrt(self):
        try:
            expr = float(self.ids.display.text)
            result = str(math.sqrt(expr))
            self.ids.display.text = result
            FinalCalcLayout.history.append(f"√{expr} = {result}")
        except:
            self.ids.display.text = "Ошибка"

    def percent(self):
        try:
            expr = float(self.ids.display.text)
            result = str(expr / 100)
            self.ids.display.text = result
            FinalCalcLayout.history.append(f"{expr}% = {result}")
        except:
            self.ids.display.text = "Ошибка"

    def show_history(self):
        if FinalCalcLayout.history:
            content = "\n".join(FinalCalcLayout.history[-5:])
        else:
            content = "История пуста"
        popup = Popup(
            title="История",
            content=Label(text=content),
            size_hint=(0.7, 0.5)
        )
        popup.open()


class FinalCalcApp(App):
    def build(self):
        return FinalCalcLayout()



if __name__ == "__main__":
    FinalCalcApp().run()

