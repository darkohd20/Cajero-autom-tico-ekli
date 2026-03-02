usuario_autenticacion = "david" 
intentos = 3
while intentos > 0:
    usaurio = input ("ingrese usuario: ")
    
    if usaurio == usuario_autenticacion: 
        print ("USUARIO CORRECTO.")
        print ("=======================")
        print ("=TechBank Riwi digital=")
        print ("====Bienvenido David===")
        print ("=======================")
        break
    else: 
        intentos-=1
        print (f"usuario no encontrado.")
    
if intentos==0:
    print ("USUARIO BLOQUEADO LLAME A LINEA DE ATENCION: 3214567890")
    
