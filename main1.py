# 2. CARACTERÍSTICAS EXTRA (Ejecutadas después)
# ==========================================
print("\n--- Menú de Características Extra ---")


print("\nElige una opción:")
print("1. Restar el segundo al primero")
print("2. Multiplicar dos números")
print("3. Dividir el primero entre el segundo")
print("4. Operación módulo")
print("5. Operaciones con 3 números o mezclar operaciones (ej. 2 + 4 - 3)")
    
opcion = input("Ingresa el número de tu opción (1-5): ")
    
if opcion == "1":
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    print("Resultado (Resta):", a - b)
        
elif opcion == "2":
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    print("Resultado (Multiplicación):", a * b)
        
elif opcion == "3":
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    if b != 0:
        print("Resultado (División):", a / b)
    else:
        print("Error: No se puede dividir entre cero.")
            
elif opcion == "4":
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    print("Resultado (Módulo):", a % b)
        
elif opcion == "5":
    print("\nPuedes escribir operaciones combinadas o con 3+ números.")
    print("Ejemplo: 2 + 4 - 3 o 4 * 5 + 1 / 3")
    expresion = input("Escribe tu operación: ")
        
    # eval() permite procesar operaciones matemáticas mixtas en texto de forma directa
    try:
        resultado_mixto = eval(expresion)
        print("Resultado de la operación:", resultado_mixto)
    except Exception as error:
        print("Ocurrió un error en la expresión:", error)
            
else:
    print("Opción no válida.")

print("\n¡Programa finalizado!")