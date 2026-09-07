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
#Adivine el numero
#Este miniporyecto consta de adivinar el numero del 1 al 20 , cinco intentos y se bloquea al quinto intento errado
#1.Importo las librerias que necesito
import tkinter as tk #type:ignore
import random
#2.Creo la ventana
ventana = tk.Tk()
ventana.title('Adivine el numero')
ventana.geometry('600x400')
#3.Creo el label para darle intrucciones al jugador
tk.Label(text='Escriba un numero y haga click en el boton para empezar el juego').pack()
#4.Creo el label que voy a usar para resultados
resultado = tk.Label(text="",font = ['Comic Sans',20])
resultado.pack()
#5.Creo la variable que va a ser para el numero random
numero_random = random.randint(1,20)
#6.Creo el contador,el contador maximo y un booleno para crear botones para cuando termine el juego
cont = 0
cont_max =5
juego_terminado = False
#7.Creo las funciones
def reiniciar():
    global cont,numero_random,juego_terminado
    cont = 0
    numero_random = random.randint(1,20)
    juego_terminado = False
    mensaje.config(text='Nuevo juego!', font = ['Comic Sans',14])
    boton_adivinar.config(state='normal') #aca habilito de nuevo el boton
    numero_elegido.delete(0,tk.END) #aca elimino el numero que se haya elegido, por las dudas
    numero_elegido.focus()

def adivinar_numero():
#8.Hago global a cont
    global cont,cont_max,numero_random,juego_terminado
    numero_adivinado = int(numero_elegido.get())

    if numero_adivinado == "" and cont <cont_max:
        mensaje.config(text=f"No escribiste nada!Te quedan {cont_max-cont} intentos",font=['Comic Sans',17])
        cont +=1
    elif numero_adivinado == numero_random:
        mensaje.config(text='Acertaste!',font=['Comic Sans',17])
    elif numero_adivinado < numero_random and cont <cont_max:
        mensaje.config(text=f"Muy bajo!.Te quedan {cont_max-cont} intentos",font=['Comic Sans',17])
        cont +=1
    elif numero_adivinado>numero_random and cont <cont_max:
        mensaje.config(text=f"Muy alto!.Te quedan {cont_max-cont} intentos",font=['Comic Sans',17])
        cont +=1
    else:
        mensaje.config(text=f"Fallaste!.Te quedan {cont_max-cont} intentos",font=['Comic Sans',17])
        cont +=1
        if cont >= cont_max:
            mensaje.config(text='¡Game Over!',font=['Comic Sans',17])
            boton_adivinar.config(state="disabled")  # Desactivar boton
            juego_terminado = True
                   
            
#9.Hago los labels 
mensaje = tk.Label(ventana,text="", font=['Comic Sans',17])
mensaje.pack()
#10.Hago la entrada
numero_elegido = tk.Entry(ventana)
numero_elegido.pack()
#11.Boton para adivinar y reiniciar partida
boton_adivinar = tk.Button(ventana,text="Adivinar numero",command=adivinar_numero)
boton_adivinar.pack()
boton_reinicio = tk.Button(ventana,text="Reiniciar partida",command=reiniciar)
boton_reinicio.pack()
#12 Bucle principal que mantiene la ventana abierta y escucha eventos.
ventana.mainloop()
