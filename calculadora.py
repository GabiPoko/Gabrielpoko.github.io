while True:
    # entrada de numeros
 numero_1 = float(input("ingrese el primer numero: "))
 numero_2 = float(input("ingrese el segundo numero: "))
    # seleccion de opciones
 print(" >>> MENU <<< ")
   print(" >>> 1. SUMA ")
    print(" >>> 2. RESTA ")
    print(" >>> 3. MULTIPLICACION ")
    print(" >>> 4. DIVISION ")
    opcion = input(" Ingrese una opcion: \n")
    # calculo
    # suma
    if opcion == "1":
        resultado = numero_1 + numero_2
        signo = "+"
    # resta
    elif opcion == "2":
        resultado = numero_1 - numero_2
        signo = "-"
    # multiplicacion4
    elif opcion == "3":
        resultado = numero_1 * numero_2
        signo = "*"
    # division
    elif opcion == "4":
        if numero_2 == 0:
            print("El numero no puede dividirse por 0")
            continue
        else:
            resultado = numero_1 / numero_2
            signo = "/"

    print(f" {numero_1} {signo} {numero_2} = {resultado}")

    salir = input(" Para salir ingrese 0 \n Para continuar presione enter \n")
    if salir == "0":
        break
print("Gracias, calculadora finalizada")