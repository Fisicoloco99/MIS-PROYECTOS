import tkinter as tk # type:ignore
import math #type : ignore

def sumar():   
    try:
        numero1 = float(num1.get())
        numero2 = float(num2.get())
        resultado.config(text = f"Resultado:{numero1 + numero2}") # resultado que es una variable se configuro, es como un return , el texto que tiene adentro lo puedo cambiar como quiera
    except ValueError:
        resultado.config('Escriba un numero!')
def restar():
    try:
        numero1 = float(num1.get())
        numero2 = float(num2.get())
        resultado.config(text = f"Resultado:{numero1 - numero2}") # resultado que es una variable se configuro, es como un return , el texto que tiene adentro lo puedo cambiar como quiera
    except ValueError:
            resultado.config('Escriba un numero!')
def multiplicar():
    try:
        numero1 = float(num1.get())
        numero2 = float(num2.get())
        resultado.config(text = f"Resultado:{numero1*numero2}") # resultado que es una variable se configuro, es como un return , el texto que tiene adentro lo puedo cambiar como quiera
    except ValueError:
            resultado.config('Escriba un numero!')
def dividir():
    try:
        numero1 = float(num1.get())
        numero2 = float(num2.get())
        if numero2 != 0:
            resultado.config(text = f"Resultado:{numero1 / numero2}") # resultado que es una variable se configuro, es como un return , el texto que tiene adentro lo puedo cambiar como quiera
    except ZeroDivisionError:
            resultado.config('Escriba un numero!')
def potencia():
    try:
        numero1 = float(num1.get())
        numero2 = float(num2.get())
        resultado.config(text = f"Resultado:{numero1**numero2}") # resultado que es una variable se configuro, es como un return , el texto que tiene adentro lo puedo cambiar como quiera
    except ValueError:
        resultado.config('Escriba un numero!')
def cuadratica():
    try:
        a = float(terminoa.get())
        b = float(terminob.get())
        c = float(terminoc.get())
        discriminante = b**2 - 4*a*c
        if discriminante < 0:
            resultado1.config(text="No tiene soluciones reales")
        else:
            raiz = math.sqrt(discriminante)
            x1 = (-b + raiz) / (2*a)
            x2 = (-b - raiz) / (2*a)
        resultado1.config(text = f"Las soluciones de tu cuadratica son : solucion 1:{x1} y solucion 2:{x2}")
    except ValueError:
        resultado1.config(text="Error: ingresa numeros validos")
    except ZeroDivisionError:
        resultado1.config(text="Error: 'a' no puede ser 0")

def raiz_cuadrada():
    try:
        numero1 = float(num1.get())
        resultado.config(text = f"Resultado:{math.sqrt(numero1)}") # resultado que es una variable se configuro, es como un return , el texto que tiene adentro lo puedo cambiar como quiera
    except ValueError:
            print("Error en obtener la raiz cuadrada")

#def raiz_general():
#        try:
#            if num3 != 0:
#                resultado = (num1) ** num2 / num3
#                self.resultado_actual = resultado
#                return resultado
#        except ZeroDivisionError:
#            print("Error!Intentelo de nuevo!")
#=====================================================================================================
#Ventana 
ventana = tk.Tk()#funciona como un objeto
ventana.title("Calculadora")
ventana.geometry("1890x980") # el tamaño de la ventana
# ===================================================================================================
#Ventana para cuadratica
ventana1 = tk.Tk()
ventana1.title("Cuadratica")
ventana1.geometry("1890x970")
#====================================================================================================
num1     = tk.Entry(ventana)
num2     = tk.Entry(ventana)             
num1.pack()
num2.pack()
#========================================================================================================
terminoa = tk.Entry(ventana1)
terminob = tk.Entry(ventana1)
terminoc = tk.Entry(ventana1)
terminoa.pack()
terminob.pack()
terminoc.pack()
#=========================================================================================================
#Boton para ventana
boton_sumar = tk.Button(ventana, text ="Sumar",command = sumar) # este es el boton , se le asigna la ventana, el texto, el command para llamar la funcion, podria tener un objeto 
boton_sumar.pack()

boton_restar = tk.Button(ventana, text="Restar", command=restar)
boton_restar.pack()

boton_multiplicar = tk.Button(ventana, text="Multiplicar", command=multiplicar)
boton_multiplicar.pack()

boton_dividir = tk.Button(ventana, text="Dividir", command=dividir)
boton_dividir.pack()

boton_potencia = tk.Button(ventana, text="Potencia", command=potencia)
boton_potencia.pack()

boton_raiz = tk.Button(ventana, text="Raiz Cuadrada", command=raiz_cuadrada)
boton_raiz.pack()

resultado = tk.Label(ventana, text="Resultado:")
resultado.pack()
#========================================================================================================
#Boton para ventana1
boton_1 = tk.Button(ventana1, text="Resolver", command=cuadratica)
boton_1.pack()
boton_1.pack()
resultado1 = tk.Label(ventana1,text="Resultado")
resultado1.pack()
#=========================================================================================================
lista1 = tk.Listbox(ventana1)
lista1.pack()
ventana1.mainloop()
#==========================================================================================================
#resultado.grid(row = 3, column = 0)
#Lista
lista = tk.Listbox(ventana) # esto es para la lista, indico que ventana va a hacer 
lista.pack() #espacio para el texto
ventana.mainloop() # para que se mantenga abierto 
