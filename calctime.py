"""
Calculadora de Años, Meses y Días
==================================
Este programa implementa una calculadora que maneja unidades de tiempo
(años, meses, días) con las siguientes conversiones:
- 1 día = 24 horas
- 1 mes = 30 días
- 1 año = 12 meses

Soporta las operaciones: suma, resta, multiplicación y división.
"""


class Tiempo:
    """
    Clase que representa una cantidad de tiempo en años, meses, días y horas.
    
    Internamente almacena el tiempo en horas para facilitar las operaciones
    aritméticas y evitar problemas de precisión.
    """
    
    # Constantes de conversión
    HORAS_POR_DIA = 24
    DIAS_POR_MES = 30
    MESES_POR_AÑO = 12
    
    # Conversiones derivadas
    HORAS_POR_MES = HORAS_POR_DIA * DIAS_POR_MES  # 720 horas
    HORAS_POR_AÑO = HORAS_POR_MES * MESES_POR_AÑO  # 8640 horas
    
    def __init__(self, años=0, meses=0, dias=0, horas=0):
        """
        Inicializa un objeto Tiempo.
        
        Args:
            años (int/float): Cantidad de años
            meses (int/float): Cantidad de meses
            dias (int/float): Cantidad de días
            horas (int/float): Cantidad de horas
        """
        self._horas_totales = self._a_horas(años, meses, dias, horas)
    
    def _a_horas(self, años, meses, dias, horas):
        """
        Convierte años, meses, días y horas a horas totales.
        
        Args:
            años (int/float): Cantidad de años
            meses (int/float): Cantidad de meses
            dias (int/float): Cantidad de días
            horas (int/float): Cantidad de horas
            
        Returns:
            float: Total de horas
        """
        total = 0
        total += años * self.HORAS_POR_AÑO
        total += meses * self.HORAS_POR_MES
        total += dias * self.HORAS_POR_DIA
        total += horas
        return total
    
    def obtener_componentes(self):
        """
        Convierte las horas totales a años, meses, días y horas.
        
        Returns:
            tuple: (años, meses, días, horas)
        """
        horas_restantes = abs(self._horas_totales)
        signo = -1 if self._horas_totales < 0 else 1
        
        # Calcular años
        años = int(horas_restantes // self.HORAS_POR_AÑO)
        horas_restantes %= self.HORAS_POR_AÑO
        
        # Calcular meses
        meses = int(horas_restantes // self.HORAS_POR_MES)
        horas_restantes %= self.HORAS_POR_MES
        
        # Calcular días
        dias = int(horas_restantes // self.HORAS_POR_DIA)
        horas_restantes %= self.HORAS_POR_DIA
        
        # Horas restantes (pueden tener decimales)
        horas = horas_restantes
        
        return (signo * años, signo * meses, signo * dias, signo * horas)
    
    def __str__(self):
        """
        Representación en cadena del objeto Tiempo.
        
        Returns:
            str: Representación legible del tiempo
        """
        años, meses, dias, horas = self.obtener_componentes()
        
        # Construir la representación
        partes = []
        
        if años != 0:
            partes.append(f"{años} año{'s' if abs(años) != 1 else ''}")
        if meses != 0:
            partes.append(f"{meses} mes{'es' if abs(meses) != 1 else ''}")
        if dias != 0:
            partes.append(f"{dias} día{'s' if abs(dias) != 1 else ''}")
        if horas != 0 or len(partes) == 0:
            # Formatear horas con 2 decimales si hay decimales
            if horas % 1 == 0:
                partes.append(f"{int(horas)} hora{'s' if abs(horas) != 1 else ''}")
            else:
                partes.append(f"{horas:.2f} horas")
        
        return ", ".join(partes)
    
    def __repr__(self):
        """Representación técnica del objeto."""
        años, meses, dias, horas = self.obtener_componentes()
        return f"Tiempo(años={años}, meses={meses}, dias={dias}, horas={horas:.2f})"
    
    # Operaciones aritméticas
    
    def __add__(self, otro):
        """
        Suma dos objetos Tiempo.
        
        Args:
            otro (Tiempo): Otro objeto Tiempo
            
        Returns:
            Tiempo: Resultado de la suma
        """
        if not isinstance(otro, Tiempo):
            raise TypeError("Solo se puede sumar con otro objeto Tiempo")
        
        resultado = Tiempo()
        resultado._horas_totales = self._horas_totales + otro._horas_totales
        return resultado
    
    def __sub__(self, otro):
        """
        Resta dos objetos Tiempo.
        
        Args:
            otro (Tiempo): Otro objeto Tiempo
            
        Returns:
            Tiempo: Resultado de la resta
        """
        if not isinstance(otro, Tiempo):
            raise TypeError("Solo se puede restar con otro objeto Tiempo")
        
        resultado = Tiempo()
        resultado._horas_totales = self._horas_totales - otro._horas_totales
        return resultado
    
    def __mul__(self, escalar):
        """
        Multiplica el tiempo por un escalar.
        
        Args:
            escalar (int/float): Número por el cual multiplicar
            
        Returns:
            Tiempo: Resultado de la multiplicación
        """
        if not isinstance(escalar, (int, float)):
            raise TypeError("Solo se puede multiplicar por un número")
        
        resultado = Tiempo()
        resultado._horas_totales = self._horas_totales * escalar
        return resultado
    
    def __rmul__(self, escalar):
        """
        Multiplicación inversa (permite escalar * Tiempo).
        
        Args:
            escalar (int/float): Número por el cual multiplicar
            
        Returns:
            Tiempo: Resultado de la multiplicación
        """
        return self.__mul__(escalar)
    
    def __truediv__(self, escalar):
        """
        Divide el tiempo por un escalar.
        
        Args:
            escalar (int/float): Número por el cual dividir
            
        Returns:
            Tiempo: Resultado de la división
            
        Raises:
            ZeroDivisionError: Si se intenta dividir por cero
        """
        if not isinstance(escalar, (int, float)):
            raise TypeError("Solo se puede dividir por un número")
        
        if escalar == 0:
            raise ZeroDivisionError("No se puede dividir por cero")
        
        resultado = Tiempo()
        resultado._horas_totales = self._horas_totales / escalar
        return resultado
    
    # Métodos de comparación
    
    def __eq__(self, otro):
        """Verifica si dos tiempos son iguales."""
        if not isinstance(otro, Tiempo):
            return False
        return abs(self._horas_totales - otro._horas_totales) < 1e-9
    
    def __lt__(self, otro):
        """Verifica si este tiempo es menor que otro."""
        if not isinstance(otro, Tiempo):
            raise TypeError("Solo se puede comparar con otro objeto Tiempo")
        return self._horas_totales < otro._horas_totales
    
    def __le__(self, otro):
        """Verifica si este tiempo es menor o igual que otro."""
        return self == otro or self < otro
    
    def __gt__(self, otro):
        """Verifica si este tiempo es mayor que otro."""
        if not isinstance(otro, Tiempo):
            raise TypeError("Solo se puede comparar con otro objeto Tiempo")
        return self._horas_totales > otro._horas_totales
    
    def __ge__(self, otro):
        """Verifica si este tiempo es mayor o igual que otro."""
        return self == otro or self > otro


def leer_tiempo(mensaje):
    """
    Lee un objeto Tiempo desde la entrada del usuario.
    
    Args:
        mensaje (str): Mensaje a mostrar al usuario
        
    Returns:
        Tiempo: Objeto Tiempo creado con los valores ingresados
    """
    print(f"\n{mensaje}")
    
    while True:
        try:
            años = float(input("  Años: "))
            meses = float(input("  Meses: "))
            dias = float(input("  Días: "))
            horas = float(input("  Horas: "))
            return Tiempo(años, meses, dias, horas)
        except ValueError:
            print("  ❌ Error: Ingrese valores numéricos válidos")


def leer_escalar(mensaje):
    """
    Lee un número escalar desde la entrada del usuario.
    
    Args:
        mensaje (str): Mensaje a mostrar al usuario
        
    Returns:
        float: Número ingresado
    """
    while True:
        try:
            valor = float(input(f"{mensaje}: "))
            return valor
        except ValueError:
            print("  ❌ Error: Ingrese un valor numérico válido")


def mostrar_menu():
    """Muestra el menú principal de opciones."""
    print("\n" + "="*50)
    print("  CALCULADORA DE AÑOS, MESES Y DÍAS")
    print("="*50)
    print("\n📋 Operaciones disponibles:")
    print("  1. Suma de tiempos")
    print("  2. Resta de tiempos")
    print("  3. Multiplicación por escalar")
    print("  4. División por escalar")
    print("  5. Ejemplos de uso")
    print("  0. Salir")
    print("-"*50)


def mostrar_ejemplos():
    """Muestra ejemplos de uso de la calculadora."""
    print("\n" + "="*50)
    print("  EJEMPLOS DE USO")
    print("="*50)
    
    # Ejemplo 1: Suma
    print("\n📌 Ejemplo 1: Suma")
    t1 = Tiempo(años=2, meses=5, dias=10)
    t2 = Tiempo(años=1, meses=3, dias=15)
    resultado = t1 + t2
    print(f"  {t1}")
    print(f"  + {t2}")
    print(f"  = {resultado}")
    
    # Ejemplo 2: Resta
    print("\n📌 Ejemplo 2: Resta")
    t1 = Tiempo(años=3, meses=8, dias=20)
    t2 = Tiempo(años=1, meses=2, dias=5)
    resultado = t1 - t2
    print(f"  {t1}")
    print(f"  - {t2}")
    print(f"  = {resultado}")
    
    # Ejemplo 3: Multiplicación
    print("\n📌 Ejemplo 3: Multiplicación")
    t1 = Tiempo(años=1, meses=6)
    escalar = 2
    resultado = t1 * escalar
    print(f"  {t1}")
    print(f"  × {escalar}")
    print(f"  = {resultado}")
    
    # Ejemplo 4: División
    print("\n📌 Ejemplo 4: División")
    t1 = Tiempo(años=4, meses=8)
    escalar = 2
    resultado = t1 / escalar
    print(f"  {t1}")
    print(f"  ÷ {escalar}")
    print(f"  = {resultado}")
    
    print("\n" + "="*50)


def operacion_recursiva_suma():
    """Realiza operaciones de suma recursivas."""
    print("\n➕ SUMA DE TIEMPOS (MODO RECURSIVO)")
    resultado = leer_tiempo("Ingrese el primer tiempo:")
    
    while True:
        t2 = leer_tiempo("Ingrese el tiempo a sumar:")
        resultado = resultado + t2
        print(f"\n✅ Resultado actual: {resultado}")
        
        print("\n¿Qué desea hacer?")
        print("  1. Continuar sumando")
        print("  2. Iniciar nueva suma")
        print("  0. Volver al menú principal")
        
        opcion = input("\n➤ Opción: ").strip()
        
        if opcion == "1":
            continue
        elif opcion == "2":
            resultado = leer_tiempo("Ingrese el nuevo primer tiempo:")
        elif opcion == "0":
            break
        else:
            print("\n❌ Opción no válida")


def operacion_recursiva_resta():
    """Realiza operaciones de resta recursivas."""
    print("\n➖ RESTA DE TIEMPOS (MODO RECURSIVO)")
    resultado = leer_tiempo("Ingrese el primer tiempo:")
    
    while True:
        t2 = leer_tiempo("Ingrese el tiempo a restar:")
        resultado = resultado - t2
        print(f"\n✅ Resultado actual: {resultado}")
        
        print("\n¿Qué desea hacer?")
        print("  1. Continuar restando")
        print("  2. Iniciar nueva resta")
        print("  0. Volver al menú principal")
        
        opcion = input("\n➤ Opción: ").strip()
        
        if opcion == "1":
            continue
        elif opcion == "2":
            resultado = leer_tiempo("Ingrese el nuevo primer tiempo:")
        elif opcion == "0":
            break
        else:
            print("\n❌ Opción no válida")


def operacion_recursiva_multiplicacion():
    """Realiza operaciones de multiplicación recursivas."""
    print("\n✖️ MULTIPLICACIÓN POR ESCALAR (MODO RECURSIVO)")
    resultado = leer_tiempo("Ingrese el tiempo inicial:")
    
    while True:
        escalar = leer_escalar("Ingrese el número por el cual multiplicar")
        resultado = resultado * escalar
        print(f"\n✅ Resultado actual: {resultado}")
        
        print("\n¿Qué desea hacer?")
        print("  1. Continuar multiplicando")
        print("  2. Iniciar nueva multiplicación")
        print("  0. Volver al menú principal")
        
        opcion = input("\n➤ Opción: ").strip()
        
        if opcion == "1":
            continue
        elif opcion == "2":
            resultado = leer_tiempo("Ingrese el nuevo tiempo inicial:")
        elif opcion == "0":
            break
        else:
            print("\n❌ Opción no válida")


def operacion_recursiva_division():
    """Realiza operaciones de división recursivas."""
    print("\n➗ DIVISIÓN POR ESCALAR (MODO RECURSIVO)")
    resultado = leer_tiempo("Ingrese el tiempo inicial:")
    
    while True:
        escalar = leer_escalar("Ingrese el número por el cual dividir")
        
        if escalar == 0:
            print("\n❌ Error: No se puede dividir por cero")
            continue
        
        resultado = resultado / escalar
        print(f"\n✅ Resultado actual: {resultado}")
        
        print("\n¿Qué desea hacer?")
        print("  1. Continuar dividiendo")
        print("  2. Iniciar nueva división")
        print("  0. Volver al menú principal")
        
        opcion = input("\n➤ Opción: ").strip()
        
        if opcion == "1":
            continue
        elif opcion == "2":
            resultado = leer_tiempo("Ingrese el nuevo tiempo inicial:")
        elif opcion == "0":
            break
        else:
            print("\n❌ Opción no válida")


def main():
    """Función principal del programa."""
    while True:
        mostrar_menu()
        
        try:
            opcion = input("\n➤ Seleccione una opción: ").strip()
            
            if opcion == "0":
                print("\n👋 ¡Hasta luego!")
                break
            
            elif opcion == "1":
                operacion_recursiva_suma()
            
            elif opcion == "2":
                operacion_recursiva_resta()
            
            elif opcion == "3":
                operacion_recursiva_multiplicacion()
            
            elif opcion == "4":
                operacion_recursiva_division()
            
            elif opcion == "5":
                # Ejemplos
                mostrar_ejemplos()
                input("\nPresione Enter para continuar...")
            
            else:
                print("\n❌ Opción no válida. Intente nuevamente.")
                input("\nPresione Enter para continuar...")
        
        except Exception as e:
            print(f"\n❌ Error: {e}")
            input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()
