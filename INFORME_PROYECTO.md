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

### Fase 3: Suite de Pruebas y Calidad
Se expandió la suite de pruebas automatizadas:
- **Mocks de Entrada**: Simulación de interacciones de usuario para probar la resistencia del código.
- **Pruebas de Interfaz**: Verificación de las llamadas al sistema para la limpieza de pantalla.
- **Cobertura Lógica**: Mantenimiento de las pruebas aritméticas originales.

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

## 4. Manual Técnico: Generación del Archivo Ejecutable (.exe)

Si desea volver a generar el ejecutable o actualizarlo tras cambios en el código, siga este procedimiento:

1. **Instalar PyInstaller**:
   Es necesario tener la herramienta PyInstaller instalada en su entorno de Python:
   ```bash
   pip install pyinstaller
   ```

2. **Comando de Compilación**:
   Ejecute el siguiente comando desde la raíz del proyecto para generar un archivo único:
   ```bash
   pyinstaller --onefile --name "CalcTime" calctime.py
   ```

3. **Explicación de los parámetros**:
   - `--onefile`: Crea un solo archivo `.exe` en lugar de una carpeta con muchos archivos.
   - `--name "CalcTime"`: Define el nombre del archivo final.
   - `calctime.py`: El script fuente que se va a compilar.

4. **Localización del Resultado**:
   Una vez finalizado el proceso (donde dirá "Build complete!"), encontrará el archivo en la carpeta:
   `\dist\CalcTime.exe`

---

## 5. Conclusión
El proyecto CalcTime ha evolucionado de un script básico a una herramienta robusta y fácil de usar, con estándares de validación modernos y capacidad de distribución independiente para usuarios de Windows.
