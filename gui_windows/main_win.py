import flet as ft
from flet import Colors, Icons, Alignment, FontWeight, MainAxisAlignment, CrossAxisAlignment, ThemeMode, TextAlign, Margin, Padding
import json
import os
from datetime import datetime
import sys

# Añadir el directorio raíz al path para importar calctime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
try:
    from calctime import Tiempo
except ImportError:
    from calctime import Tiempo

class CalcTimeWin:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "CalcTime v3.0.7"
        self.page.window.width = 400
        self.page.window.height = 780
        self.page.window.resizable = False
        
        # Refs para acceso directo
        self.result_ref = ft.Ref[ft.Text]()
        self.expr_ref = ft.Ref[ft.Text]()
        self.history_list_ref = ft.Ref[ft.ListView]()
        
        # Estado
        self.current_value = "0"
        self.expression = ""
        self.last_result = None
        self.operator = None
        self.temp_values = {"años": 0, "meses": 0, "dias": 0, "horas": 0, "minutos": 0}
        self.history = []
        self.settings = {"darkMode": True}
        
        self.load_data()
        self.setup_ui()
        self.page.on_keyboard_event = self.on_keyboard
        self.page.update()

    def load_data(self):
        try:
            if os.path.exists("gui_windows/config.json"):
                with open("gui_windows/config.json", "r") as f: self.settings = json.load(f)
            if os.path.exists("gui_windows/history.txt"):
                with open("gui_windows/history.txt", "r", encoding="utf-8") as f:
                    for line in f:
                        if "]" in line:
                            ts, entry = line.split("]", 1)
                            self.history.append({"timestamp": ts[1:], "entry": entry.strip()})
        except: pass

    def save_data(self):
        try:
            if not os.path.exists("gui_windows"): os.makedirs("gui_windows")
            with open("gui_windows/config.json", "w") as f: json.dump(self.settings, f)
            with open("gui_windows/history.txt", "w", encoding="utf-8") as f:
                for h in self.history: f.write(f"[{h['timestamp']}] {h['entry']}\n")
        except: pass

    def setup_ui(self):
        # Pantalla
        display = ft.Container(
            content=ft.Column([
                ft.Text(ref=self.expr_ref, value="", size=14, color=Colors.BLUE_200, italic=True),
                ft.Text(ref=self.result_ref, value="0", size=24, weight=FontWeight.BOLD),
            ], horizontal_alignment=CrossAxisAlignment.END, spacing=5),
            padding=15, bgcolor=Colors.with_opacity(0.1, Colors.BLUE_GREY_900),
            border_radius=12, margin=Margin.only(bottom=15)
        )

        # Acciones superiores
        top_bar = ft.Row([
            ft.IconButton(Icons.HISTORY_ROUNDED, on_click=self.show_history),
            ft.IconButton(Icons.SETTINGS_ROUNDED, on_click=self.show_settings),
            ft.Button("Copy", icon=Icons.COPY_ALL, on_click=self.copy_result)
        ], alignment=MainAxisAlignment.START)

        # Teclado
        keypad = ft.GridView(expand=True, runs_count=4, max_extent=85, child_aspect_ratio=1.1, spacing=8)
        btns = [
            ("AC", "clear", Colors.PINK_300), ("DEL", "delete", Colors.PINK_300), ("%", "op", Colors.ORANGE_300), ("÷", "op", Colors.ORANGE_300),
            ("7", "digit", None), ("8", "digit", None), ("9", "digit", None), ("×", "op", Colors.ORANGE_300),
            ("4", "digit", None), ("5", "digit", None), ("6", "digit", None), ("-", "op", Colors.ORANGE_300),
            ("1", "digit", None), ("2", "digit", None), ("3", "digit", None), ("+", "op", Colors.ORANGE_300),
            ("0", "digit", None), (".", "digit", None), ("=", "calc", Colors.CYAN_400),
        ]
        for text, tp, col in btns:
            keypad.controls.append(ft.Container(
                content=ft.Text(text, size=18, weight=FontWeight.W_500),
                alignment=Alignment.CENTER, bgcolor=col if col else Colors.with_opacity(0.05, Colors.WHITE),
                border_radius=10, ink=True, on_click=lambda e, t=text, p=tp: self.handle_input(p, t)
            ))

        # Unidades
        units = ft.Row([self.make_unit_btn(u) for u in ["Y", "M", "D", "H", "Min"]], alignment=MainAxisAlignment.CENTER)

        # Drawer de Historial (Pre-init)
        self.page.drawer = ft.NavigationDrawer(controls=[
            ft.Container(content=ft.Column([
                ft.Row([ft.Text("History", size=20, weight="bold"), ft.IconButton(Icons.CLOSE, on_click=self.close_drawer)], alignment="spaceBetween"),
                ft.Divider(),
                ft.ListView(ref=self.history_list_ref, expand=True, height=500),
                ft.Button("Clear All", on_click=self.clear_history)
            ]), padding=15)
        ])

        self.page.add(ft.Column([top_bar, display, keypad, ft.Divider(height=10, color=Colors.TRANSPARENT), units], expand=True))
        
        # Sincronizar overlay para refs
        self.page.overlay.append(self.page.drawer)
        self.page.update()

    def make_unit_btn(self, label):
        return ft.Container(
            content=ft.Text(label, size=11, weight="bold"), padding=Padding.all(8),
            bgcolor=Colors.with_opacity(0.15, Colors.CYAN_700), border_radius=6,
            on_click=lambda e: self.handle_input("unit", label)
        )

    def handle_input(self, tp, val):
        print(f"Input: {tp} {val}")
        if tp == "digit":
            if val == "." and "." in self.current_value: return
            self.current_value = val if self.current_value == "0" else self.current_value + val
        elif tp == "delete": self.current_value = self.current_value[:-1] if len(self.current_value) > 1 else "0"
        elif tp == "clear":
            self.current_value, self.expression, self.last_result, self.operator = "0", "", None, None
            self.temp_values = {u:0 for u in self.temp_values}
        elif tp == "unit":
            num = float(self.current_value)
            self.temp_values[{"Y":"años","M":"meses","D":"dias","H":"horas","Min":"minutos"}[val]] = num
            self.expression += f"{num}{val.lower()} "
            self.current_value = "0"
        elif tp == "op":
            t = Tiempo(**{k:self.temp_values[k] for k in ["años","meses","dias","horas"]})
            t._horas_totales += self.temp_values["minutos"]/60
            if not self.last_result: self.last_result = t
            elif self.operator: self.calculate(t)
            self.operator, self.expression, self.current_value = val, self.expression + f" {val} ", "0"
            self.temp_values = {u:0 for u in self.temp_values}
        elif tp == "calc":
            t = Tiempo(**{k:self.temp_values[k] for k in ["años","meses","dias","horas"]})
            t._horas_totales += self.temp_values["minutos"]/60
            if self.last_result and self.operator:
                prev = str(self.last_result)
                self.calculate(t)
                self.history.insert(0, {"timestamp": datetime.now().strftime("%H:%M"), "entry": f"{prev} {self.operator} {str(t)} = {str(self.last_result)}"})
                self.expression, self.operator, self.current_value = "", None, "0"
                self.temp_values = {u:0 for u in self.temp_values}
                self.save_data()
        self.update_ui()

    def calculate(self, t):
        if self.operator == "+": self.last_result += t
        elif self.operator == "-": self.last_result -= t
        elif self.operator == "×": self.last_result *= float(self.current_value or 1)
        elif self.operator in ["÷", "➗"]:
            div = float(self.current_value or 1)
            if div != 0: self.last_result /= div

    def update_ui(self):
        print(f"UI Update: {self.current_value}")
        self.expr_ref.current.value = self.expression
        if self.last_result and self.current_value == "0":
            años, meses, dias, horas = self.last_result.obtener_componentes()
            disp = f"{años}Y {meses}M {dias}D {horas:.2f}H"
        else: disp = self.current_value
        self.result_ref.current.value = disp[:25]
        self.page.update()

    def on_keyboard(self, e: ft.KeyboardEvent):
        key = e.key
        print(f"Key: {key}")
        
        # Mapeo de Numpad
        if key.startswith("Numpad "):
            num_map = {"0":"0", "1":"1", "2":"2", "3":"3", "4":"4", "5":"5", "6":"6", "7":"7", "8":"8", "9":"9",
                       "Add":"+", "Subtract":"-", "Multiply":"*", "Divide":"/", "Enter":"Enter", "Decimal":"."}
            k_part = key.split(" ", 1)[1]
            if k_part in num_map: key = num_map[k_part]

        if key in "0123456789": self.handle_input("digit", key)
        elif key in [".", ",", "Decimal"]: self.handle_input("digit", ".")
        elif key == "Backspace": self.handle_input("delete", None)
        elif key == "Escape": self.handle_input("clear", None)
        elif key in ["Enter", "="]: self.handle_input("calc", "=")
        elif key == "+": self.handle_input("op", "+")
        elif key == "-": self.handle_input("op", "-")
        elif key.lower() in ["*", "x"]: self.handle_input("op", "×")
        elif key in ["/", ":"]: self.handle_input("op", "÷")
        elif key.upper() in ["Y", "M", "D", "H"]: self.handle_input("unit", key.upper())
        elif key.upper() == "I": self.handle_input("unit", "Min")

    def show_history(self, e):
        print(f"Opening History... Items: {len(self.history)}")
        if self.history_list_ref.current:
            self.history_list_ref.current.controls.clear()
            for h in self.history:
                self.history_list_ref.current.controls.append(ft.Container(
                    content=ft.Column([ft.Text(h["timestamp"], size=10), ft.Text(h["entry"], size=12)]),
                    padding=10, bgcolor=Colors.with_opacity(0.05, Colors.WHITE), border_radius=10
                ))
            if not self.history:
                self.history_list_ref.current.controls.append(ft.Text("Empty history", italic=True))
        
        self.page.drawer.open = True
        self.page.update()

    def close_drawer(self, e): self.page.drawer.open = False; self.page.update()
    def clear_history(self, e): self.history = []; self.save_data(); self.close_drawer(e)
    def copy_result(self, e):
        # Usar set_clipboard() como método, ya que .clipboard no tiene setter
        res = self.result_ref.current.value
        try:
            self.page.set_clipboard(res)
        except:
            # Fallback a propiedad si el método falla en alguna versión
            try: self.page.clipboard = res
            except: pass
        self.page.update()

    def show_settings(self, e):
        print("Opening Settings...")
        def toggle(e): self.page.theme_mode = ThemeMode.DARK if e.control.value else ThemeMode.LIGHT; self.page.update()
        dlg = ft.AlertDialog(title=ft.Text("Settings"), content=ft.Switch(label="Dark Mode", value=True, on_change=toggle))
        self.page.overlay.append(dlg)
        dlg.open = True
        self.page.update()

def main(page: ft.Page): CalcTimeWin(page)
if __name__ == "__main__": ft.run(main)
