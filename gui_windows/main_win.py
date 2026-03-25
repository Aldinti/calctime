import flet as ft
import json
import os
from datetime import datetime
import sys

# Añadir el directorio raíz al path para importar calctime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
try:
    from calctime import Tiempo
except ImportError:
    # Fallback si se ejecuta directamente desde la raíz
    from calctime import Tiempo

class CalcTimeWin:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "CalcTime v3.0 - Desktop"
        self.page.window_width = 400
        self.page.window_height = 750
        self.page.window_resizable = False
        
        # Estado de la calculadora
        self.current_value = "0"
        self.expression = ""
        self.last_result = None
        self.operator = None
        self.temp_values = {"años": 0, "meses": 0, "dias": 0, "horas": 0, "minutos": 0}
        self.history = []
        self.settings = {"darkMode": True, "font": "Inter"}
        
        self.load_data()
        self.setup_ui()
        self.apply_settings()

    def load_data(self):
        # Cargar ajustes
        if os.path.exists("gui_windows/config.json"):
            with open("gui_windows/config.json", "r") as f:
                self.settings = json.load(f)
        
        # Cargar historial
        if os.path.exists("gui_windows/history.txt"):
            with open("gui_windows/history.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    if "]" in line:
                        ts, entry = line.split("]", 1)
                        self.history.append({"timestamp": ts[1:], "entry": entry.strip()})

    def save_data(self):
        # Guardar ajustes
        with open("gui_windows/config.json", "w") as f:
            json.dump(self.settings, f)
        
        # Guardar historial
        with open("gui_windows/history.txt", "w", encoding="utf-8") as f:
            for h in self.history:
                f.write(f"[{h['timestamp']}] {h['entry']}\n")

    def setup_ui(self):
        # Pantalla
        self.expr_text = ft.Text(value="", size=14, color=ft.colors.BLUE_200, italic=True)
        self.result_text = ft.Text(value="0", size=48, weight=ft.FontWeight.BOLD)
        
        display_container = ft.Container(
            content=ft.Column(
                [self.expr_text, self.result_text],
                horizontal_alignment=ft.CrossAxisAlignment.END,
                spacing=0
            ),
            padding=20,
            bgcolor=ft.colors.with_opacity(0.1, ft.colors.BLUE_GREY_900),
            border_radius=15,
            margin=ft.margin.only(bottom=20)
        )

        # Botones Superiores (H, S, Copiar)
        top_actions = ft.Row(
            [
                ft.IconButton(ft.icons.HISTORY_ROUNDED, on_click=self.show_history, tooltip="Historial"),
                ft.IconButton(ft.icons.SETTINGS_ROUNDED, on_click=self.show_settings, tooltip="Ajustes"),
                ft.VerticalDivider(width=10, color=ft.colors.TRANSPARENT),
                ft.ElevatedButton("Copiar", icon=ft.icons.COPY_ALL, on_click=self.copy_result, 
                                 style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)))
            ],
            alignment=ft.MainAxisAlignment.START
        )

        # Teclado (Flet GridView para los botones)
        buttons = [
            ("AC", "clear", ft.colors.PINK_300), ("DEL", "delete", ft.colors.PINK_300), ("%", "op", ft.colors.ORANGE_300), ("÷", "op", ft.colors.ORANGE_300),
            ("7", "digit", None), ("8", "digit", None), ("9", "digit", None), ("×", "op", ft.colors.ORANGE_300),
            ("4", "digit", None), ("5", "digit", None), ("6", "digit", None), ("-", "op", ft.colors.ORANGE_300),
            ("1", "digit", None), ("2", "digit", None), ("3", "digit", None), ("+", "op", ft.colors.ORANGE_300),
            ("0", "digit", None), (".", "digit", None), ("=", "calc", ft.colors.CYAN_400),
        ]

        keypad = ft.GridView(
            expand=True,
            runs_count=4,
            max_extent=90,
            child_aspect_ratio=1.2,
            spacing=10,
            run_spacing=10,
        )

        for text, type, color in buttons:
            btn = ft.Container(
                content=ft.Text(text, size=20, weight=ft.FontWeight.W_500),
                alignment=ft.alignment.center,
                on_click=lambda e, t=text, tp=type: self.handle_input(tp, t),
                bgcolor=color if color else ft.colors.with_opacity(0.05, ft.colors.WHITE),
                border_radius=12,
                ink=True
            )
            keypad.controls.append(btn)

        # Botones de Unidades (A, M, D, H, Min)
        unit_buttons = ft.Row(
            [
                self.make_unit_btn("Años"), self.make_unit_btn("Meses"), 
                self.make_unit_btn("Días"), self.make_unit_btn("Horas"), 
                self.make_unit_btn("Minutos")
            ],
            wrap=True,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=5
        )

        # Layout Principal
        self.page.add(
            ft.Column(
                [
                    top_actions,
                    display_container,
                    keypad,
                    ft.Divider(height=20, color=ft.colors.TRANSPARENT),
                    unit_buttons
                ],
                expand=True
            )
        )

    def make_unit_btn(self, label):
        return ft.Container(
            content=ft.Text(label, size=12),
            padding=10,
            bgcolor=ft.colors.with_opacity(0.1, ft.colors.BLUE_400),
            border_radius=8,
            on_click=lambda e: self.handle_input("unit", label)
        )

    def apply_settings(self):
        self.page.theme_mode = ft.ThemeMode.DARK if self.settings["darkMode"] else ft.ThemeMode.LIGHT
        # Fuentes se aplican vía style properties si se cargan fuentes personalizadas
        self.page.update()

    def handle_input(self, type, val):
        if type == "digit":
            if val == "." and "." in self.current_value: return
            if self.current_value == "0": self.current_value = val
            else: self.current_value += val
            
        elif type == "delete":
            self.current_value = self.current_value[:-1] if len(self.current_value) > 1 else "0"
            
        elif type == "clear":
            self.current_value = "0"
            self.expression = ""
            self.reset_state()
            
        elif type == "unit":
            num = float(self.current_value)
            unit_map = {"Años": "años", "Meses": "meses", "Días": "dias", "Horas": "horas", "Minutos": "minutos"}
            self.temp_values[unit_map[val]] = num
            
            unit_display = {"Años": "a", "Meses": "m", "Días": "d", "Horas": "h", "Minutos": "min"}[val]
            self.expression += f"{num}{unit_display} "
            self.current_value = "0"
            
        elif type == "op":
            # Crear objeto Tiempo con valores actuales
            t = Tiempo(años=self.temp_values["años"], meses=self.temp_values["meses"], 
                       dias=self.temp_values["dias"], horas=self.temp_values["horas"])
            # Nota: calctime.py original no tiene minutos, pero la GUI web los portó.
            # Aquí, si minutos > 0, los sumamos proporcionalmente asumiendo precisión en horas
            t._horas_totales += self.temp_values["minutos"] / 60
            
            if not self.last_result:
                self.last_result = t
            elif self.operator:
                self.calculate_intermediate(t)
            
            self.operator = val
            self.expression += f" {val} "
            self.temp_values = {"años": 0, "meses": 0, "dias": 0, "horas": 0, "minutos": 0}
            self.current_value = "0"

        elif type == "calc":
            final_t = Tiempo(años=self.temp_values["años"], meses=self.temp_values["meses"], 
                            dias=self.temp_values["dias"], horas=self.temp_values["horas"])
            final_t._horas_totales += self.temp_values["minutos"] / 60
            
            if self.last_result and self.operator:
                prev_str = str(self.last_result)
                self.calculate_intermediate(final_t)
                result_str = str(self.last_result)
                
                self.add_to_history(f"{prev_str} {self.operator} {str(final_t)} = {result_str}")
                self.expression = ""
                self.operator = None
                self.current_value = "0"
                self.temp_values = {"años": 0, "meses": 0, "dias": 0, "horas": 0, "minutos": 0}

        self.update_display()

    def calculate_intermediate(self, t):
        if self.operator == "+": self.last_result = self.last_result + t
        elif self.operator == "-": self.last_result = self.last_result - t
        elif self.operator == "×": 
            fac = float(self.current_value) if self.current_value != "0" else 1
            self.last_result = self.last_result * fac
        elif self.operator == "÷":
            div = float(self.current_value) if self.current_value != "0" else 1
            if div != 0: self.last_result = self.last_result / div

    def reset_state(self):
        self.last_result = None
        self.operator = None
        self.temp_values = {"años": 0, "meses": 0, "dias": 0, "horas": 0, "minutos": 0}

    def update_display(self):
        self.expr_text.value = self.expression
        # Mostrar el valor actual o el último resultado si la expresión está vacía
        display_val = self.current_value if self.current_value != "0" or not self.last_result else str(self.last_result)
        self.result_text.value = display_val[:10] # Limitar longitud
        self.page.update()

    def copy_result(self, e):
        text = str(self.last_result) if self.last_result else self.current_value
        self.page.set_clipboard(text)
        self.page.show_snack_bar(ft.SnackBar(ft.Text("¡Copiado al portapapeles!")))

    def add_to_history(self, entry):
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.insert(0, {"timestamp": ts, "entry": entry})
        if len(self.history) > 50: self.history.pop()
        self.save_data()

    def show_history(self, e):
        lv = ft.ListView(expand=True, spacing=10, padding=20)
        if not self.history:
            lv.controls.append(ft.Text("No hay historial aún.", italic=True, opacity=0.5))
        for item in self.history:
            lv.controls.append(
                ft.Container(
                    content=ft.Column([
                        ft.Text(item["timestamp"], size=10, color=ft.colors.BLUE_200),
                        ft.Text(item["entry"], size=14)
                    ]),
                    padding=10, bgcolor=ft.colors.with_opacity(0.05, ft.colors.WHITE), border_radius=10
                )
            )
        
        self.page.drawer = ft.NavigationDrawer(
            controls=[
                ft.Container(
                    content=ft.Column([
                        ft.Row([ft.Text("Historial", size=24, weight="bold"), ft.IconButton(ft.icons.CLOSE, on_click=lambda _: self.page.drawer.open_close())], alignment="spaceBetween"),
                        ft.Divider(),
                        lv,
                        ft.ElevatedButton("Limpiar Todo", icon=ft.icons.DELETE_FOREVER, on_click=self.clear_history)
                    ]),
                    padding=20
                )
            ]
        )
        self.page.drawer.open = True
        self.page.update()

    def clear_history(self, e):
        self.history = []
        self.save_data()
        self.page.drawer.open = False
        self.page.update()

    def show_settings(self, e):
        def toggle_theme(e):
            self.settings["darkMode"] = e.control.value
            self.apply_settings()
            self.save_data()

        dlg = ft.AlertDialog(
            title=ft.Text("Ajustes de la Interfaz"),
            content=ft.Column([
                ft.Switch(label="Modo Oscuro", value=self.settings["darkMode"], on_change=toggle_theme),
                ft.Text("Fuente actual: System Default (Inter)", size=12, opacity=0.6)
            ], tight=True),
            actions=[ft.TextButton("Cerrar", on_click=lambda _: self.close_dlg(dlg))]
        )
        self.page.dialog = dlg
        dlg.open = True
        self.page.update()

    def close_dlg(self, dlg):
        dlg.open = False
        self.page.update()

def main(page: ft.Page):
    CalcTimeWin(page)

if __name__ == "__main__":
    ft.app(target=main)
