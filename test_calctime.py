"""
Script de pruebas para la Calculadora de Años, Meses y Días
============================================================
Este script verifica que todas las operaciones y conversiones
funcionen correctamente.
"""

from unittest.mock import patch
from calctime import Tiempo, obtener_entrada_numerica, seleccionar_opcion


def test_conversiones():
    """Prueba las conversiones entre unidades."""
    print("\n" + "="*60)
    print("TEST 1: CONVERSIONES ENTRE UNIDADES")
    print("="*60)
    
    # 1 año = 12 meses = 360 días = 8640 horas
    t1 = Tiempo(años=1)
    assert t1._horas_totales == 8640, "Error: 1 año debe ser 8640 horas"
    print("✅ 1 año = 8640 horas")
    
    # 1 mes = 30 días = 720 horas
    t2 = Tiempo(meses=1)
    assert t2._horas_totales == 720, "Error: 1 mes debe ser 720 horas"
    print("✅ 1 mes = 720 horas")
    
    # 1 día = 24 horas
    t3 = Tiempo(dias=1)
    assert t3._horas_totales == 24, "Error: 1 día debe ser 24 horas"
    print("✅ 1 día = 24 horas")
    
    # Conversión mixta
    t4 = Tiempo(años=1, meses=6, dias=15)
    esperado = 8640 + 4320 + 360  # 1 año + 6 meses + 15 días
    assert t4._horas_totales == esperado, f"Error: esperado {esperado}, obtenido {t4._horas_totales}"
    print(f"✅ 1 año, 6 meses, 15 días = {esperado} horas")
    
    print("\n✅ Todas las conversiones pasaron correctamente")


def test_suma():
    """Prueba la operación de suma."""
    print("\n" + "="*60)
    print("TEST 2: OPERACIÓN DE SUMA")
    print("="*60)
    
    # Suma simple
    t1 = Tiempo(meses=6)
    t2 = Tiempo(meses=8)
    t3 = t1 + t2
    años, meses, dias, horas = t3.obtener_componentes()
    assert años == 1 and meses == 2, f"Error: esperado 1 año 2 meses, obtenido {años} años {meses} meses"
    print(f"✅ 6 meses + 8 meses = {t3}")
    
    # Suma con días
    t4 = Tiempo(dias=20)
    t5 = Tiempo(dias=15)
    t6 = t4 + t5
    años, meses, dias, horas = t6.obtener_componentes()
    assert meses == 1 and dias == 5, f"Error: esperado 1 mes 5 días, obtenido {meses} meses {dias} días"
    print(f"✅ 20 días + 15 días = {t6}")
    
    # Suma mixta
    t7 = Tiempo(años=2, meses=5, dias=10)
    t8 = Tiempo(años=1, meses=3, dias=15)
    t9 = t7 + t8
    años, meses, dias, horas = t9.obtener_componentes()
    assert años == 3 and meses == 8 and dias == 25, f"Error en suma mixta"
    print(f"✅ (2 años, 5 meses, 10 días) + (1 año, 3 meses, 15 días) = {t9}")
    
    print("\n✅ Todas las sumas pasaron correctamente")


def test_resta():
    """Prueba la operación de resta."""
    print("\n" + "="*60)
    print("TEST 3: OPERACIÓN DE RESTA")
    print("="*60)
    
    # Resta simple
    t1 = Tiempo(años=2)
    t2 = Tiempo(meses=6)
    t3 = t1 - t2
    años, meses, dias, horas = t3.obtener_componentes()
    assert años == 1 and meses == 6, f"Error: esperado 1 año 6 meses, obtenido {años} años {meses} meses"
    print(f"✅ 2 años - 6 meses = {t3}")
    
    # Resta con resultado negativo
    t4 = Tiempo(meses=3)
    t5 = Tiempo(meses=8)
    t6 = t4 - t5
    años, meses, dias, horas = t6.obtener_componentes()
    assert meses == -5, f"Error: esperado -5 meses, obtenido {meses} meses"
    print(f"✅ 3 meses - 8 meses = {t6}")
    
    # Resta mixta
    t7 = Tiempo(años=3, meses=8, dias=20)
    t8 = Tiempo(años=1, meses=2, dias=5)
    t9 = t7 - t8
    años, meses, dias, horas = t9.obtener_componentes()
    assert años == 2 and meses == 6 and dias == 15, f"Error en resta mixta"
    print(f"✅ (3 años, 8 meses, 20 días) - (1 año, 2 meses, 5 días) = {t9}")
    
    print("\n✅ Todas las restas pasaron correctamente")


def test_multiplicacion():
    """Prueba la operación de multiplicación."""
    print("\n" + "="*60)
    print("TEST 4: OPERACIÓN DE MULTIPLICACIÓN")
    print("="*60)
    
    # Multiplicación simple
    t1 = Tiempo(meses=3)
    t2 = t1 * 4
    años, meses, dias, horas = t2.obtener_componentes()
    assert años == 1, f"Error: esperado 1 año, obtenido {años} años"
    print(f"✅ 3 meses × 4 = {t2}")
    
    # Multiplicación inversa
    t3 = Tiempo(dias=10)
    t4 = 3 * t3
    años, meses, dias, horas = t4.obtener_componentes()
    assert dias == 30 or meses == 1, f"Error en multiplicación inversa"
    print(f"✅ 3 × 10 días = {t4}")
    
    # Multiplicación con decimal
    t5 = Tiempo(años=2)
    t6 = t5 * 1.5
    años, meses, dias, horas = t6.obtener_componentes()
    assert años == 3, f"Error: esperado 3 años, obtenido {años} años"
    print(f"✅ 2 años × 1.5 = {t6}")
    
    # Multiplicación mixta
    t7 = Tiempo(años=1, meses=6)
    t8 = t7 * 2
    años, meses, dias, horas = t8.obtener_componentes()
    assert años == 3, f"Error: esperado 3 años, obtenido {años} años"
    print(f"✅ (1 año, 6 meses) × 2 = {t8}")
    
    print("\n✅ Todas las multiplicaciones pasaron correctamente")


def test_division():
    """Prueba la operación de división."""
    print("\n" + "="*60)
    print("TEST 5: OPERACIÓN DE DIVISIÓN")
    print("="*60)
    
    # División simple
    t1 = Tiempo(años=2)
    t2 = t1 / 2
    años, meses, dias, horas = t2.obtener_componentes()
    assert años == 1, f"Error: esperado 1 año, obtenido {años} años"
    print(f"✅ 2 años ÷ 2 = {t2}")
    
    # División con resultado decimal
    t3 = Tiempo(meses=5)
    t4 = t3 / 2
    años, meses, dias, horas = t4.obtener_componentes()
    assert meses == 2 and dias == 15, f"Error en división decimal"
    print(f"✅ 5 meses ÷ 2 = {t4}")
    
    # División mixta
    t5 = Tiempo(años=4, meses=8)
    t6 = t5 / 2
    años, meses, dias, horas = t6.obtener_componentes()
    assert años == 2 and meses == 4, f"Error en división mixta"
    print(f"✅ (4 años, 8 meses) ÷ 2 = {t6}")
    
    # Prueba de división por cero
    try:
        t7 = Tiempo(años=1)
        t8 = t7 / 0
        assert False, "Error: debería lanzar ZeroDivisionError"
    except ZeroDivisionError:
        print("✅ División por cero lanza ZeroDivisionError correctamente")
    
    print("\n✅ Todas las divisiones pasaron correctamente")


def test_comparaciones():
    """Prueba las operaciones de comparación."""
    print("\n" + "="*60)
    print("TEST 6: OPERACIONES DE COMPARACIÓN")
    print("="*60)
    
    t1 = Tiempo(años=2)
    t2 = Tiempo(meses=24)
    t3 = Tiempo(años=1)
    
    # Igualdad
    assert t1 == t2, "Error: 2 años debería ser igual a 24 meses"
    print("✅ 2 años == 24 meses")
    
    # Mayor que
    assert t1 > t3, "Error: 2 años debería ser mayor que 1 año"
    print("✅ 2 años > 1 año")
    
    # Menor que
    assert t3 < t1, "Error: 1 año debería ser menor que 2 años"
    print("✅ 1 año < 2 años")
    
    # Mayor o igual
    assert t1 >= t2, "Error: 2 años debería ser >= 24 meses"
    print("✅ 2 años >= 24 meses")
    
    # Menor o igual
    assert t3 <= t1, "Error: 1 año debería ser <= 2 años"
    print("✅ 1 año <= 2 años")
    
    print("\n✅ Todas las comparaciones pasaron correctamente")


def test_casos_especiales():
    """Prueba casos especiales y edge cases."""
    print("\n" + "="*60)
    print("TEST 7: CASOS ESPECIALES")
    print("="*60)
    
    # Tiempo cero
    t1 = Tiempo()
    assert t1._horas_totales == 0, "Error: Tiempo vacío debería ser 0 horas"
    print(f"✅ Tiempo vacío: {t1}")
    
    # Suma con cero
    t2 = Tiempo(años=1)
    t3 = Tiempo()
    t4 = t2 + t3
    assert t4 == t2, "Error: sumar cero no debería cambiar el tiempo"
    print("✅ 1 año + 0 = 1 año")
    
    # Multiplicación por cero
    t5 = Tiempo(años=5)
    t6 = t5 * 0
    assert t6._horas_totales == 0, "Error: multiplicar por 0 debería dar 0"
    print("✅ 5 años × 0 = 0")
    
    # Valores decimales en entrada
    t7 = Tiempo(años=1.5, meses=2.5)
    años, meses, dias, horas = t7.obtener_componentes()
    print(f"✅ 1.5 años + 2.5 meses = {t7}")
    
    # Tiempo negativo
    t8 = Tiempo(años=-1)
    años, meses, dias, horas = t8.obtener_componentes()
    assert años == -1, "Error: debería soportar valores negativos"
    print(f"✅ Tiempo negativo: {t8}")
    
    print("\n✅ Todos los casos especiales pasaron correctamente")


def test_validacion_y_entrada():
    """Prueba las funciones de validación de entrada."""
    print("\n" + "="*60)
    print("TEST 8: VALIDACIÓN DE DATOS Y ENTRADAS")
    print("="*60)
    
    # Prueba obtener_entrada_numerica con entrada válida
    with patch('builtins.input', side_effect=['10']):
        valor = obtener_entrada_numerica("Test: ")
        assert valor == 10.0, f"Error: esperado 10.0, obtenido {valor}"
        print("✅ obtener_entrada_numerica acepta valores válidos")
    
    # Prueba obtener_entrada_numerica con entrada vacía seguida de válida
    with patch('builtins.input', side_effect=['', '25']):
        # Capturamos print para no ensuciar la salida del test
        with patch('builtins.print'):
            valor = obtener_entrada_numerica("Test: ")
            assert valor == 25.0, "Error: debería manejar entradas vacías"
            print("✅ obtener_entrada_numerica maneja entradas vacías")
            
    # Prueba obtener_entrada_numerica con letra seguida de válida
    with patch('builtins.input', side_effect=['abc', '50']):
        with patch('builtins.print'):
            valor = obtener_entrada_numerica("Test: ")
            assert valor == 50.0, "Error: debería manejar entradas no numéricas"
            print("✅ obtener_entrada_numerica maneja entradas no numéricas (letras)")
            
    # Prueba obtener_entrada_numerica con negativo cuando está prohibido
    with patch('builtins.input', side_effect=['-5', '10']):
        with patch('builtins.print'):
            valor = obtener_entrada_numerica("Test: ", permitir_negativos=False)
            assert valor == 10.0, "Error: debería prohibir negativos"
            print("✅ obtener_entrada_numerica prohíbe negativos cuando se solicita")

    # Prueba seleccionar_opcion
    with patch('builtins.input', side_effect=['invalid', '2']):
        with patch('builtins.print'):
            opcion = seleccionar_opcion("Test: ", ["1", "2", "3"])
            assert opcion == "2", f"Error: esperado '2', obtenido '{opcion}'"
            print("✅ seleccionar_opcion valida opciones correctas")
            
    print("\n✅ Todas las pruebas de validación pasaron correctamente")


def test_interfaz_limpieza():
    """Prueba la función de limpieza de pantalla."""
    print("\n" + "="*60)
    print("TEST 9: LIMPIEZA DE PANTALLA")
    print("="*60)
    
    from calctime import limpiar_pantalla
    import os
    
    with patch('os.system') as mock_system:
        limpiar_pantalla()
        mock_system.assert_called_once()
        comando = 'cls' if os.name == 'nt' else 'clear'
        mock_system.assert_called_with(comando)
        print(f"✅ limpiar_pantalla llamó a os.system('{comando}')")
        
    print("\n✅ La prueba de limpieza de pantalla pasó correctamente")


def ejecutar_todas_las_pruebas():
    """Ejecuta todas las pruebas."""
    print("\n" + "="*60)
    print("  SUITE DE PRUEBAS - CALCULADORA DE TIEMPO")
    print("="*60)
    
    try:
        test_conversiones()
        test_suma()
        test_resta()
        test_multiplicacion()
        test_division()
        test_comparaciones()
        test_casos_especiales()
        test_validacion_y_entrada()
        test_interfaz_limpieza()
        
        print("\n" + "="*60)
        print("  ✅ TODAS LAS PRUEBAS PASARON EXITOSAMENTE")
        print("="*60)
        
    except AssertionError as e:
        print(f"\n❌ PRUEBA FALLIDA: {e}")
        return False
    except Exception as e:
        print(f"\n❌ ERROR INESPERADO: {e}")
        return False
    
    return True


if __name__ == "__main__":
    ejecutar_todas_las_pruebas()
