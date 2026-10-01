import tkinter as tk

usuario_valido = 'BancoGalicia26'
contrasenia_valida = 2026

class CuentaBancaria:
    def __init__(self, saldo, titular):
        # self.saldo: dinero disponible en la cuenta
        self.saldo = saldo
        # self.titular: nombre del dueño de la cuenta
        self.titular = titular

    def loguear_usuario(self):
        #Pide usuario y contraseña por consola.
        #Da 3 intentos. Si falla, bloquea la sesión.
        
        intentos = 0
        while intentos < 3:
            # Pido los datos por consola (input)
            usser = input('Ingrese su usuario: ')
            password = int(input('Ingrese su contraseña numericamente: '))
            
            # Si no escribio nada en alguno de los campos
            if usser == "" or password == "":
                print('No ha ingresado datos')
                intentos += 1
            # Si el usuario y contraseña son correctos
            elif usser == usuario_valido and password == contrasenia_valida:
                print('Datos correctamente ingresados!')
                print(f"Bienvenido, {usser}")
            # Si los datos son incorrectos
            elif usser != usuario_valido or password != contrasenia_valida:
                print('¡Operacion invalida!')
                intentos += 1
                if intentos < 3:
                    print(f"Sesion fallida. Le quedan {3 - intentos} intentos")
                elif intentos == 3:
                    print('Se ha bloqueado la sesion. Espere unos minutos!')

    def depositar(self, deposito):
        try:
            lim_deposito = 500000
            if float(deposito) < lim_deposito:
                if self.saldo == 0:
                    print(f"Su saldo es de ${self.saldo}")
                elif self.saldo > 0:
                    self.saldo += float(deposito)   # Suma al saldo
                    print(f"Su saldo es de ${self.saldo}")
                else:
                    print('Error en la operacion')
            else:
                print('Ha excedido el limite de deposito permitido por dia! Intentelo en 24 hs!')
        except ValueError:
            print('Operacion invalida (debe ingresar un numero)')

    def retirar(self, monto_retirar):
        try:
            lim_retiro = 4000000
            if float(monto_retirar)<=lim_retiro:
                if self.saldo == 0:
                    print(f"Su saldo es de ${self.saldo}")
                elif self.saldo > 0:
                    self.saldo -= float(monto_retirar)   # Resta del saldo
                    print(f"Su saldo es de ${self.saldo}")
                else:
                    print('Error en la operacion')
            else:
                print('Ha excedido al limite de transferencias! Intentelo en 24 hs!')
        except ValueError:
            print('Operacion invalida (debe ingresar un numero)')

    def prestamos(self, monto_prestamo):
        try:
            lim_prestamo = 500000
            if float(monto_prestamo) < lim_prestamo:
                if self.saldo == 0:
                    print(f"Su saldo es de ${self.saldo}")
                elif self.saldo > 0:
                    self.saldo += float(monto_prestamo)
                    print(f"Su saldo es de ${self.saldo}")
                else:
                    print('Error en la operacion')
            else:
                print('Ha excedido al limite del prestamo! Vuelva a intentarlo en 24 hs!')
        except ValueError:
            print('Operacion invalida (debe ingresar un numero)')

# ============================================================
# Creo un objeto de la clase CuentaBancaria
# ============================================================
#Se crea el objeto

Cuenta_Banco = CuentaBancaria()
#Creo la ventana
ventana = tk.Tk()
ventana.title('Banco Galicia')
ventana.geometry('1080x890')
#Aca seria las variables que guarden las opciones
#monto    = float(usuario.get())
#deposito = float(usuario.get())
#retiro   = float(usuario.get())

#Creo la entrada
usuario = tk.Entry(ventana)
usuario.pack()
terminal_eleccion = usuario.get() #aca guardo la opcion que el usuario elige
#Botones
boton_retirar = tk.Button(ventana,text='Retirar dinero',command = Cuenta_Banco.retirar(usuario.get()))
boton_retirar.pack()
boton_depositar = tk.Button(ventana,text='Depositar dinero', command = Cuenta_Banco.depositar(usuario.get()))
boton_depositar.pack()
boton_prestamo = tk.Button(ventana,text = 'Pedir prestamo', commando = Cuenta_Banco.prestamos(usuario.get()))
boton_prestamo.pack()
ventana.mainloop()