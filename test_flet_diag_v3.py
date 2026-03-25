import flet as ft
from flet import Colors, Icons, Alignment, FontWeight, MainAxisAlignment, CrossAxisAlignment, ThemeMode, TextAlign

def check_obj(obj, name):
    try:
        attrs = [a for a in dir(obj) if not a.startswith('_')]
        print(f"\n--- {name} Attributes ---")
        print(attrs[:30])
    except Exception as e:
        print(f"Error checking {name}: {e}")

check_obj(TextAlign, "TextAlign")
check_obj(ft.Page, "ft.Page methods")
# Ver si hay snack_bar o SnackBar
print(f"\nft.SnackBar exists: {'SnackBar' in dir(ft)}")
print(f"page.show_snack_bar exists: {'show_snack_bar' in dir(ft.Page)}")
