intentos = 5
while intentos > 0:
    print("Bienvenido a la banca en línea")
    nombre = input("Ingrese su nombre:")
    usuario = input("Ingrese el RUT:")
    clave = input("Ingrese la clave internet:")
    if clave == ("stein10"):
        print("Ingreso correcto. Bienvenido,", nombre,".")
        break
    else: intentos = intentos - 1 
    print("Clave incorrecta. Le quedan", intentos, "intentos.")
if intentos == 0:
    print("Porfavor comuníquese con nuestro call center.")
        
    