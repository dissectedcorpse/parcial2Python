#usted ha sido seleccionado para realizar la interfaz de usuario de los cajeros automaticos de Santander, 
#el programa debe solicitar al usuario: numero de rut el cual debe ser validado con su numero de verificacion, 
# posteriormente a eso el usuario debe ingresar su clave que no debe ser superior a 10 digitos.
print ("Bienvenido al Banco Santander.")
while True: #establece un loop para verificar varios aspectos del RUT
    rut_str = input("Porfavor ingrese su RUT (sin puntos ni guión): ")
    try: #se inicia el try para que la verificación sea más segura. También se podría usar if. (?)
        if not rut_str.isdigit(): #si rut_str no es un número
            print("¡ERROR! El RUT debe contener únicamente números.")
            continue #se piden los datos otra vez
        if not (7 <= len(rut_str) <= 8): #si rut_str no tiene de 7 a 8 números. len significa length, verifica la longitud de un valor
            print("¡ERROR! El RUT debe tener entre 7 y 8 dígitos.")
            continue
        rut = int(rut_str) #si los datos son correctos, se convierten a int
        print("RUT ingresado correctamente.")
        break #se termina el loop
    except ValueError: #tercera verificación
        print("Error inesperado al ingresar el RUT. Intente nuevamente.")
        continue #se procede a pedir el siguiente dato

while True: #loop para verificar el digito verificador
    dv = input("Ingrese el dígito verificador: ").upper()#upper convierte cualquier letra ingresada en mayúscula para no dar errores en la verificación.
    if (dv.isdigit() and len(dv) == 1) or (dv == 'K' and len(dv) == 1):#1.verifica si dv es un número. 2. si solo tiene un carácter de largo. o si tiene una letra y es K
        print("Dígito verificador ingresado correctamente.")
        break
    else:
        print("¡ERROR! El dígito verificador es inválido. Intente nuevamente.")

while True: #loop para verificar la clave
    try:
        clave_str = input("Ingrese su clave. Debe contener de 4 a 10 dígitos: ")
        if not clave_str.isdigit(): #si clave_str no es un número
            print("¡ERROR! La clave debe contener sólo números.")
            continue
        if not (4 <= len(clave_str) <= 10): #si la clave tiene menos de 4 o más de 10 dígitos. Establecí 4 como mínimo, ya que ningún cajero aceptaría un sólo dígito como clave, ya que sería demasiado inseguro.
            print("¡ERROR! La clave debe contener de 4 a 10 dígitos.")
            continue
        clave = int(clave_str) #si los datos son correctos, los convierte a int
        print("Clave ingresada correctamente.")
        break
    except ValueError:
        print("Error inesperado al ingresar la clave. Intente nuevamente.") #tercera verificación
        continue
print("Acceso exitoso. Bienvenido.") #finaliza el programa.
#este programa se puede interpretar como un registro. Si fuera un login con un rut, dv y clave ya predefinidos, sólo habría que modificar
#los if not a los valores que se requieren para dicho login. 