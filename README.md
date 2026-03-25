# ⏰ CalcTime v2.0 - Calculadora de Años, Meses y Días

Una herramienta integral para el manejo de unidades de tiempo que incluye una potente lógica en Python y una **nueva interfaz gráfica (GUI)** moderna con persistencia de datos.

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/Version-2.0.0-green.svg)](https://img.shields.io/badge/Version-2.0.0-green.svg)

## 🌟 Características Principales

- ✅ **Interfaz Gráfica Premium**: Diseño *Glassmorphism* con soporte para modo oscuro/claro y selección de fuentes.
- ✅ **Persistencia de Datos**: El historial de cálculos y tus ajustes se guardan automáticamente en el navegador.
- ✅ **Operaciones Aritméticas Completas**: Suma, resta, multiplicación y división de tiempos con alta precisión.
- ✅ **Modo Recursivo**: Encadena múltiples cálculos sin perder el flujo de trabajo.
- ✅ **Conversiones Precisas**: Manejo automático entre años, meses, días, horas y **minutos**.
- ✅ **Exportación de Datos**: Descarga tu historial de cálculos directamente en un archivo `.txt`.
- ✅ **Suite de Pruebas Robusta**: Garantía de precisión lógica del 100%.

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

### Ejecutar la Interfaz Gráfica (Recomendado)
Simplemente abre el archivo principal de la GUI en tu navegador:
1. Navega a la carpeta `gui/`
2. Abre `index.html` en Chrome, Edge o Firefox.

### Ejecutar el programa por Consola (Python)
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
├── gui/                 # Nueva Interfaz Gráfica Web
│   ├── index.html       # Estructura de la calculadora
│   ├── style.css        # Diseño Glassmorphism y Temas
│   └── calculator.js    # Lógica en JS y Persistencia
├── calctime.py          # Lógica central en Python
├── test_calctime.py     # Suite de pruebas
├── README.md            # Este archivo
└── LICENSE              # Licencia MIT
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
