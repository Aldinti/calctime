# Walkthrough: CalcTime v3.0.9 - El Sistema Multi-Interfaz Definitivo
---
*CalcTime v3.0.9 - "Reactive Perfection" (2026)*
de Cálculo de Tiempo

Una solución completa y multi-interfaz para el manejo de unidades de tiempo. Incluye lógica robusta en Python con tres formas de interacción independientes.

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/Version-3.0.0-purple.svg)](https://img.shields.io/badge/Version-3.0.0-purple.svg)

## 🌟 3 Interfaces Independientes

1.  **💻 Desktop Native (Windows)**: Aplicación de escritorio moderna construida con Flet.
2.  **🌐 Web Premium (HTML/JS)**: Interfaz responsiva con diseño *Glassmorphism*.
3.  **🐚 Terminal (CLI)**: Versión clásica de consola para operaciones rápidas.

## ✨ Características Principales v3.0

- ✅ **Persistencia Multi-Capa**: LocalStorage para web y archivos JSON/TXT para desktop.
-   **Multi-Interfaz**: Incluye una versión Web moderna y una aplicación de escritorio nativa para Windows.

#### Novedades v3.0.9 (Desktop):
- **Arquitectura Reactiva**: Uso de `ft.Ref` para una sincronización instantánea entre lógica y UI.
- **Soporte de Teclado**: Control completo mediante el bloque numérico (Numpad) y atajos de unidad.
- **Internacionalización**: Resultados con iniciales en inglés (Y, M, D, H) para compatibilidad universal.
- **Estabilidad de Paneles**: Gestión robusta de Historial y Ajustes mediante el sistema de superposiciones de Flet.

- ✅ **Personalización Avanzada**: Temas Oscuro/Claro y selección de fuentes en ambas GUIs.
- ✅ **Exportación de Historial**: Generación de reportes en `.txt` de tus cálculos.
- ✅ **Lógica Unificada**: Los 518,400 minutos de un año calculados con precisión matemática.

## 📋 Especificaciones

### Conversiones

- **1 hora** = 60 minutos
- **1 día** = 24 horas = 1,440 minutos
- **1 mes** = 30 días = 720 horas = 43,200 minutos
- **1 año** = 12 meses = 360 días = 8,640 horas = 518,400 minutos

### Operaciones Soportadas

- Suma de tiempos
- Resta de tiempos (permite resultados negativos)
- Multiplicación por escalar
- División por escalar (con manejo de división por cero)

## 🚀 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/calctime.git
cd calctime

# No requiere dependencias externas - solo Python 3.7+
```

## 💻 Uso

### 1. Ejecutar la Aplicación de Escritorio (Windows Native)
Requiere tener instalado `flet` (`pip install flet`).
```bash
python gui_windows/main_win.py
```

### 2. Ejecutar la Interfaz Web (Browser)
Simplemente abre el archivo en tu navegador:
- Navega a `gui/index.html` y ábrelo con Chrome/Edge.

### 3. Ejecutar el programa por Consola (CLI)
```bash
python calctime.py
```

### Ejecutar como Aplicación Portable (.exe)
Si estás en Windows, puedes usar la versión compilada:
1. Dirígete a la carpeta `dist/`
2. Ejecuta `CalcTime.exe`

### Ejecutar las pruebas
```bash
python test_calctime.py
```

## 📖 Ejemplos

### Ejemplo 1: Suma Simple

```python
from calctime import Tiempo

t1 = Tiempo(años=2, meses=5, dias=10)
t2 = Tiempo(años=1, meses=3, dias=15)
resultado = t1 + t2
print(resultado)  # 3 años, 8 meses, 25 días
```

### Ejemplo 2: Operaciones Recursivas

El modo recursivo permite encadenar múltiples operaciones:

1. Selecciona una operación (ej: Suma)
2. Ingresa el primer tiempo: `1 año, 2 meses, 3 días, 4 horas`
3. Ingresa el tiempo a sumar: `0 años, 5 meses, 10 días, 0 horas`
4. **Resultado**: `1 año, 7 meses, 13 días, 4 horas`
5. Opciones:
   - **Continuar sumando** → Suma otro tiempo al resultado
   - **Iniciar nueva suma** → Comienza desde cero
   - **Volver al menú** → Regresa al menú principal

### Ejemplo 3: Multiplicación

```python
t1 = Tiempo(años=1, meses=6)
resultado = t1 * 2
print(resultado)  # 3 años
```

### Ejemplo 4: División

```python
t1 = Tiempo(años=4, meses=8)
resultado = t1 / 2
print(resultado)  # 2 años, 4 meses
```

## 🏗️ Arquitectura

### Clase `Tiempo`

La clase principal utiliza **horas** como unidad base de almacenamiento interno para:

- Simplificar operaciones aritméticas
- Mantener precisión en cálculos con decimales
- Realizar conversiones automáticas entre unidades

**Métodos principales:**

- `__add__`, `__sub__`, `__mul__`, `__truediv__`: Operaciones aritméticas
- `__eq__`, `__lt__`, `__le__`, `__gt__`, `__ge__`: Comparaciones
- `obtener_componentes()`: Convierte horas a años, meses, días, horas
- `__str__()`: Representación legible del tiempo

## 🧪 Pruebas

La suite de pruebas incluye 7 categorías:

8. **Validación de entradas y datos** (entradas vacías, caracteres alfanuméricos)
9. **Funcionalidad de limpieza de pantalla**

**Resultado**: ✅ 100% de pruebas pasadas (Lógica + Interfaz)

## 📁 Estructura del Proyecto

```
calctime/
├── gui_windows/        # Interfaz Nativa Desktop (Nuevo v3.0)
│   ├── main_win.py     # Aplicación Flet
│   └── config.json     # Configuración local
├── gui/                # Interfaz Web (Glassmorphism)
│   ├── index.html
│   └── calculator.js
├── calctime.py         # Lógica core y CLI
├── test_calctime.py    # Pruebas
└── README.md
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 👤 Autor

**Ing. Aldo B. Patiño F.**
- GitHub: [@Aldinti](https://github.com/tu-usuario)

## 📚 Documentación Adicional

- [Informe Detallado del Proyecto](INFORME_PROYECTO.md): Contiene el plan ejecutado, manual técnico de compilación y manual de usuario detallado.

## 🙏 Agradecimientos

- Proyecto personal desarrollado como iniciativa para facilitar los cálculos de tiempos exigidos en el formato de hoja de vida de la función pública en Colombia.
- Universidad: Universidad Cooperativa de Colombia - UCC

---

⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub!
