# Informe Detallado del Proyecto: CalcTime ⏰

## 1. Introducción
Este proyecto consiste en una calculadora especializada en la gestión de unidades de tiempo (años, meses, días y horas). Su objetivo principal es facilitar el cálculo de tiempos de experiencia laboral, específicamente diseñado para el formato de hoja de vida de la función pública en Colombia, utilizando conversiones estándar (1 mes = 30 días, 1 año = 12 meses).

## 2. Plan Ejecutado y Mejoras Implementadas

### Fase 1: Validación Robusta de Datos
Se implementó un sistema de validación avanzada para prevenir errores comunes:
- **Prevención de caracteres no numéricos**: El programa bloquea entradas con letras o símbolos donde se esperan números.
- **Validación por campo**: Cada unidad (años, meses, etc.) se valida individualmente antes de pasar a la siguiente.
- **Manejo de estados vacíos**: Se evita que el programa falle si el usuario presiona "Enter" sin digitar un valor.

### Fase 2: Mejora de la Interfaz de Usuario (UX)
Se optimizó la presentación en consola:
- **Limpieza de Pantalla Dinámica**: Implementación de comandos `cls` (Windows) y `clear` (Unix) para mantener la consola despejada.
- **Visualización Acumulada**: En el modo recursivo, se mantiene el resultado anterior visible mientras se solicitan los nuevos datos.
- **Emojis e Indicadores**: Uso de iconos visuales para mejorar la legibilidad de las operaciones.

### Fase 4: Ecosistema Multi-Interfaz (Web & Desktop)
Se expandió CalcTime para ser accesible desde cualquier entorno:
- **GUI Web Premium**: Interfaz HTML/JS con diseño *Glassmorphism*.
- **GUI Desktop Nativa (v3.3.2)**: Aplicación construida con **Flet**, con arquitectura de capas (Stack UI) para estabilidad total, soporte universal de portapapeles (PowerShell) y localización internacional.
- **Lógica Unificada**: Reutilización de la clase `Tiempo` en Python para todas las versiones.

---

## 3. Manual de Usuario: Ejecución con Python

Para ejecutar el programa directamente desde la terminal, siga estos pasos:

1. **Abrir la terminal**: 
   - En Windows: Presione `Win + R`, escriba `cmd` o `powershell` y presione Enter.
   - Navegue hasta la carpeta del proyecto: `cd c:\Users\aldin\Desktop\CalcTime`

2. **Verificar Python**: 
   Asegúrese de tener Python 3.7 o superior instalado:
   ```bash
   python --version
   ```

3. **Ejecutar el programa**:
   Escriba el comando y presione Enter:
   ```bash
   python calctime.py
   ```

4. **Navegación**:
   - Use los números del **0 al 5** para seleccionar operaciones.
   - Siga las instrucciones en pantalla para ingresar los valores de tiempo.

---

---

## 5. Manual de Interfaz Gráfica (Web & Desktop)

### 5.1 Ejecución de la Versión Desktop (Nativa Windows)
1.  **Instalar Flet**: Es el motor gráfico necesario.
    ```bash
    pip install flet
    ```
2.  **Lanzar la aplicación**:
    ```bash
    python gui_windows/main_win.py
    ```
#### Novedades v3.3.2 (Desktop):
- **Stack UI Overlays**: Capas de interfaz manuales (no dependientes de Drawers) para transparencia y control total.
- **PowerShell Clipboard**: Copiado garantizado mediante comandos nativos de Windows.
- **Script-Relative Paths**: Datos persistentes vinculados localmente a la ubicación del ejecutable.
1.  Navegue a la carpeta `gui/`.
2.  Abra el archivo `index.html` en su navegador preferido (Chrome, Edge).

---

## 6. Conclusión
El proyecto CalcTime ha evolucionado de un script básico a un ecosistema multiplataforma robusto. Con tres interfaces independientes (CLI, Web, Desktop), ofrece flexibilidad total para el usuario final, manteniendo siempre la precisión matemática en la gestión de tiempos.
