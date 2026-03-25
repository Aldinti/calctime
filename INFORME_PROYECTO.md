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

### Walkthrough: CalcTime v3.0.9 - El Sistema Multi-Interfaz Definitivo
(Web & Desktop)
Se expandió CalcTime para ser accesible desde cualquier entorno:
- **GUI Web Premium**: Interfaz HTML/JS con diseño *Glassmorphism*.
- **GUI Desktop Nativa (v3.0.9)**: Aplicación construida con **Flet**, con arquitectura reactiva (`ft.Ref`), soporte completo para teclado (Numpad) y localización internacional de resultados.
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
#### Novedades v3.0.9 (Desktop):
-4.  **Soporte de Teclado (v3.0.9)**: Control nativo mediante NumPad, Enter y teclas de unidad.
5.  **Internacionalización (v3.0.9)**: Resultados en formato internacional (Y, M, D, H).
6.  **Arquitectura Reactiva**: Implementación con `ft.Ref` para una respuesta instantánea.
7.  **Lógica Compartida**: Código core unificado en Python para CLI, Web y Desktop.
1.  Navegue a la carpeta `gui/`.
2.  Abra el archivo `index.html` en su navegador preferido (Chrome, Edge).

---

## 6. Conclusión
El proyecto CalcTime ha evolucionado de un script básico a un ecosistema multiplataforma robusto. Con tres interfaces independientes (CLI, Web, Desktop), ofrece flexibilidad total para el usuario final, manteniendo siempre la precisión matemática en la gestión de tiempos.
