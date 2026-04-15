'''duoc ha contratado sus servicios para realizar un login en python, el login debe validar el usuario y la clave'''
usuario = input("Porfavor ingrese su usuario:")
if usuario == ("alumno"):
    clave = input("Bienvenido. Porfavor ingrese la clave:")
    if clave == ("1123"):
        print("Ha ingresado correctamente.")
    else: print("Contraseña incorrecta, intente nuevamente.")
else: print("Usuario no autorizado, intente nuevamente.")