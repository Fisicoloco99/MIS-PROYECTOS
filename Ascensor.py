import tkinter as tk# Importo la libreria para interfaces graficas
ventana = tk.Tk()# Creo la ventana principal
ventana.title('Ascensor')
ventana.geometry('600x400')
mensaje = tk.Label(ventana, text='')# Creo el label donde voy a mostrar los mensajes
mensaje.grid(row=0, column=0, columnspan=3, pady=10)  # Ocupa 3 columnas
class Ascensor:# Creo una clase ascensor
    def __init__(self,puerta,piso):
        self.puerta = puerta
        self.piso = piso
    def verificar_puerta(self):
        if self.puerta == True:
            mensaje.config(text='La puerta esta cerrada.Se puede usar el ascensor correctamente') #despues que salga este
            return True
        else:
            ventana.config(state="disabled")# Desactivar boton
            return False
    def subir_piso(self,piso):
        lista_de_pisos = [-3,-2,-1,0,1,2,3,4,5,6,7,8]
        menor = min(lista_de_pisos)
        mayor = max(lista_de_pisos)
        if self.piso>=menor and self.piso<=mayor:
            mensaje.config(text=f"Esta subiendo al piso {self.piso}")#La idea es que salga este mensaje
            self.piso = piso
        else:
            mensaje.config(text='Operacion invalida')
    def bajar_al_piso(self,piso):
        lista_de_pisos = [-3,-2,-1,0,1,2,3,4,5,6,7,8]
        menor = min(lista_de_pisos)
        mayor = max(lista_de_pisos)
        if self.piso >= menor and self.piso <= mayor:
            mensaje.config(text=f"Esta bajando al piso {self.piso}")
            self.piso = piso             
        else:
            mensaje.config(text='Operacion invalida')
    def botones_especiales(self,boton_especiales):
        especiales = ['><','<>','EMERGENCIA']
        if boton_especiales in especiales:
            if boton_especiales == '><':
                mensaje.config(text='Ha cerrado la puerta')
                self.puerta = True
            elif boton_especiales == '<>':
                mensaje.config(text='Ha abierto la puerta')
                self.puerta = False
            elif boton_especiales == 'EMERGENCIA':
                mensaje.config(text='No entre el panico.Los bomberos y emergencia vendran lo mas rapido!')
        else:
            mensaje.config(text='Presione una tecla valida')
    def botones(self,boton):
        botones= [-3,-2,-1,0,1,2,3,4,5,6,7,8]
        if boton in botones:
            mensaje.config(text=f"Esta en el piso {boton}")
        else:
            mensaje.config(text='Presione una tecla valida')
# Quiero ver si se puede actualizar
    def actualizar(self, piso_destino):
        self.piso = piso_destino
        mensaje.config(text=f"Ha llegado al piso {self.piso}")
    #Creo el objeto
elevador = Ascensor(False,0)
#Botones# Fila 1: botones 1, 2, 3

tk.Button(ventana, text="0",command=lambda: elevador.botones(0), width=5, height=2).grid(row=1, column=0, padx=5, pady=5)
tk.Button(ventana, text="1",command=lambda: elevador.botones(1), width=5, height=2).grid(row=1, column=1, padx=5, pady=5)
tk.Button(ventana, text="2",command=lambda: elevador.botones(2), width=5, height=2).grid(row=1, column=2, padx=5, pady=5)
#Botones Fila 2:
tk.Button(ventana, text="3",command=lambda: elevador.botones(3), width=5, height=2).grid(row=2, column=0, padx=5, pady=5)
tk.Button(ventana, text="4",command=lambda: elevador.botones(4), width=5, height=2).grid(row=2, column=1, padx=5, pady=5)
tk.Button(ventana, text="5",command=lambda: elevador.botones(5), width=5, height=2).grid(row=2, column=2, padx=5, pady=5)
#Botones Fila 3:
tk.Button(ventana, text="6",command=lambda: elevador.botones(6), width=5, height=2).grid(row=3, column=0, padx=5, pady=5)
tk.Button(ventana, text="7",command=lambda: elevador.botones(7), width=5, height=2).grid(row=3, column=1, padx=5, pady=5)
tk.Button(ventana, text="8",command=lambda: elevador.botones(8), width=5, height=2).grid(row=3, column=2, padx=5, pady=5)
#Botones Fila 4:
tk.Button(ventana, text="-1",command=lambda: elevador.botones(-1), width=5, height=2).grid(row=4, column=0, padx=5, pady=5)
tk.Button(ventana, text="-2",command=lambda: elevador.botones(-2), width=5, height=2).grid(row=4, column=1, padx=5, pady=5)
tk.Button(ventana, text="-3",command=lambda: elevador.botones(-3), width=5, height=2).grid(row=4, column=2, padx=5, pady=5)
#Botones Fila 5:
tk.Button(ventana, text="><",command=lambda: elevador.botones_especiales('><'), width=5, height=2).grid(row=5, column=0, padx=5, pady=5)
tk.Button(ventana, text="<>",command=lambda: elevador.botones_especiales('<>'), width=5, height=2).grid(row=5, column=1, padx=5, pady=5)
tk.Button(ventana, text="EMERGENCIA",command=lambda: elevador.botones_especiales('EMERGENCIA'), width=5, height=2).grid(row=5, column=2, padx=5, pady=5)


ventana.mainloop()# Bucle principal que mantiene la ventana abierta