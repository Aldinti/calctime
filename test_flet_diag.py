import flet as ft
print("--- Flet Attributes ---")
all_attrs = dir(ft)
print(f"Total attributes: {len(all_attrs)}")

# Buscar colores
print("\nColors found:")
print([a for a in all_attrs if "color" in a.lower()])

# Buscar iconos
print("\nIcons found:")
print([a for a in all_attrs if "icon" in a.lower()])

# Probar acceso directo
try:
    print(f"\nft.Icons: {'Icons' in all_attrs}")
    print(f"ft.icons: {'icons' in all_attrs}")
    print(f"ft.Colors: {'Colors' in all_attrs}")
except Exception as e:
    print(f"Error checking attributes: {e}")

# Ver si Icons es un submódulo
try:
    import flet.icons as icons
    print("\nflet.icons found via import")
except ImportError:
    print("\nflet.icons NOT found via import")

try:
    from flet import Icons
    print("flet.Icons found via from-import")
except ImportError:
    print("flet.Icons NOT found via from-import")
