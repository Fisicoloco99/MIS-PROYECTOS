# ============================================================
# AUTOR: Nahuel Zanini
# DERECHOS DE AUTOR (C) 2026 Nahuel Zanini
# TODOS LOS DERECHOS RESERVADOS.
#
# Este software es propiedad de Nahuel Zanini.
# No está permitido copiar, distribuir, modificar, vender,
# ni utilizar este código total o parcialmente sin
# autorización expresa por escrito del autor.
# ============================================================
#Este miniporyecto de hacer una aplicacion de To Do list
#El plan o estructura a seguir es :
#1. Importar módulos
#2. Crear variables globales (listas, contadores)
#3. Definir funciones (agregar, eliminar, ver, etc.)
#4. Crear la ventana principal
#5. Crear los widgets (Labels, Entry, Botones, Listbox)
#6. Ejecutar ventana.mainloop()

# 1. Importar modulo/libreria
import tkinter as tk  # type:ignore
import random
#2.Variables a tener en cuenta
tarea_hecha = True #esto es un bool para que cuando se complete la tarea aparezca como True
tareas_hechas = []
tareas_no_hechas = [] #aca van a estar todas las tareas
tareas_azar = [] # aca estarian las tareas random...la idea seria que le de al usuario una tarea cualquiera y despues se elimine
contador = 0#este seria mi variable de contador para que se sume o se reste las tareas agregadas o eliminadas
#2.Creo la ventana
ventana = tk.Tk()
ventana.title('To-Do List Aplicacion')
ventana.geometry('600x400')
#Ahora bien quiero las entradas para el usuario
#2.Voy a hacer el label para los mensajes
mensaje = tk.Label(ventana,text="",font=['Comic Sans',14])
mensaje.pack()
#Ahora voy a hacer el menu para que el usuario lo vea.
def menu():
    tk.Label(ventana,text=f"Cantidad de tareas hechas:{len(tareas_hechas)}").pack() # <---- Aca estaria el mensaje que muestra la cantidad de tareas hechas
    tk.Label(ventana,text=f"Cantidad de tareas pendientes:{len(tareas_no_hechas)}").pack()# <---- Aca estaria el mensaje que muestra la cantidad de tareas NO hechas
    tk.Label(ventana,text=f"Cantidad de tareas azar:{len(tareas_azar)}").pack()# <---- Aca estaria el mensaje que muestra la cantidad de tareas azar
    tk.Label(ventana,text='---MENU---',font=['Comic sans',20]).pack()
    tk.Label(ventana,text='1.Ver lista de tareas',font=['Comic sans',14]).pack()
    tk.Label(ventana,text='2.Añadir tareas',font=['Comic sans',14]).pack()
    tk.Label(ventana,text='3.Eliminar tareas',font=['Comic sans',14]).pack()
    tk.Label(ventana,text='4.Crear una tarea al azar',font=['Comic sans',14]).pack()
    tk.Label(ventana,text='5.Chequear estado de las tareas',font=['Comic sans',14]).pack()
    tk.Label(ventana,text='6.Salir',font=['Comic sans',14]).pack()
    tk.Label(ventana,text='Escriba una opcion numerica',font=['Comic sans',14]).pack()
#2.Ahora la idea seria hacer la entrada para que el usuario ingrese una opcion de forma numerica
entrada = tk.Entry(ventana)
entrada.pack()
#2.Aca guardo la variable que el usuario elija
usuario_eleccion = entrada.get()
#2.Aca guardo la variable para que la computadora elija en su lista
eleccion_azar = random.choice(tareas_azar)
#3.Voy a hacer las funciones para que tenga sentido
#Por ejemplo para la opcion 1 es motrar la lista de tareas
def ver_tareas():
    global tareas_hechas,tareas_no_hechas,tareas_azar






#Creo la lista
lista_aplicacion = tk.Listbox(ventana)
lista_aplicacion.pack()

#Creo el bucle para que se mantenga abierto
ventana.mainloop() # <--- ESTO TIENE QUE IR A LO ULTIMO PORQUE SINO NO SE CREA LO DEMAS!
