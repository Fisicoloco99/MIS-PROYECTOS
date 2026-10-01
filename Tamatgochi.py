import tkinter as tk
# Variables globales para los atributos de la mascota
hambre = 50     # Nivel de hambre (0 = sin hambre, valores altos = mucha hambre)
energia = 100   # Nivel de energia
cariño = 100
clicks = 0
nivel = 0

# Funcion para actualizar la interfaz (muestra valores y mensajes)
def actualizar():
    global hambre
    global energia
    global cariño
    global clicks
    # Actualiza la etiqueta de estado con los numeros actuales
    estado.config(text=f"Hambre:{hambre},Energia:{energia}. Cariño:{cariño}")
    if clicks>=100:
        mensaje.config(text="Subis de nivel")
        clicks = 0
    elif clicks >=0:
        clicks+=1   
    elif clicks<0:
        clicks = 0
    # Mensajes segun el nivel de energia (rangos)
    if energia in range(1,51):
        mensaje.config(text="No tengo energia")
    elif energia in range(51,101):
        mensaje.config(text="Tengo energia")
    elif energia in range(101,151):   
        mensaje.config(text="Tengo mucha energia")
    
    # Mensajes segun el nivel de hambre (rangos)
    if hambre in range(1,51):
        mensaje.config(text="No tengo hambre")
    elif hambre in range(51,101):
        mensaje.config(text="Tengo hambre")
    elif hambre in range(51,151):   # Tambien se solapa (deberia ser 101-150)
        mensaje.config(text="Tengo mucha hambre")

def alimentar():
    global hambre
    global energia
    hambre -= 10                     # Al comer, el hambre disminuye
    energia += 10                    # Y la energia aumenta
    actualizar()                     # Refresca la interfaz
    if hambre <= 0:
        hambre = 0                   # Evita que el hambre sea negativa
    else:
        hambre =0

def jugar():
    global hambre
    global energia
    hambre += 10                     # Jugar aumenta el hambre
    energia -= 10                    # Y disminuye la energia
    actualizar()
    if hambre == 150:                # Si el hambre llega a 150, se reinicia a 0
        hambre = 0                   # Reinicio

def subir_nivel():
    global clicks
    if clicks == "":
        mensaje.config(text="Hace CLICK!")
    elif clicks == 100:
        mensaje.config(text="Subis de nivel!")
        clicks = 0
    elif clicks <100:
        clicks +=1
    else:
        mensaje.config(text="Hace CLICK!")


# Ventana principal
ventana = tk.Tk()
ventana.title("Tamagotchi ")
ventana.geometry("1080x900")

# Carga una imagen (asegurate de que la ruta sea correcta)
Kuchipatchi = tk.PhotoImage(file = 'Kuchipatchi.png')
Kuchipatchi.pack()
# Etiqueta con el titulo
titulo = tk.Label(ventana,text = "Tamagotchi  Life", font = ['Comic Sans',20])
titulo.pack()

# Botones para interactuar
boton_alimentar = tk.Button(ventana, text="Le diste de comer", command=alimentar)
boton_alimentar.pack()
boton_jugar = tk.Button(ventana, text="Esta jugando", command=jugar)
boton_jugar.pack()

# Etiquetas para mostrar mensajes y estado
mensaje = tk.Label(ventana,text='Estado de hambre:')
mensaje.pack()
estado = tk.Label(ventana,text='Estado de hambre')
estado.pack()

# Muestra la imagen de la mascota
mascota = tk.Label(ventana,image=Kuchipatchi)
mascota.pack()

ventana.mainloop()