def menu ():
    print ("Ejercicio 1, Hola Mundo")
    print ("Ejercicio 2, Suma dos números")
    print ("Ejercicio 3, Calcular edad")
    print ("Ejercicio 4, Calcular IMC")
    print ("Ejercicio 5, Hallar número par e impar")
    print ("Ejercicio 6, Hallar el área de un cuadraro")
    print ("Ejercicio 7, Calcular el area de un triangulo")

print("Ingresa un número del menú: ")
menu()
opcion = input ("Opcion: ")

match opcion:
    case "1":
        nota_uno = input ("Ejercicio 1, Hola Mundo: ")
    case "2":
        nota_dos = input ("Ejercicio 2, Suma dos números: ")
    case "3":
        nota_tres = input("Ejercicio 3, Calcular edad: ")
    case "4":
        nota_cuatro = input("Ejercicio 4, Calcular IMC: ")
    case "5":
        nota_cinco = input("Ejercicio 5, Hallar número par e impar: ")
    case "6":
        nota_seis = input("Ejercicio 6, Hallar el área de un cuadraro: ")
    case "7":
        nota_siete = input("Ejercicio 7, Hallar el área de un triángulo: ")
    case _:
        print("Opción incorrecta")
