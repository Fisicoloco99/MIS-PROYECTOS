import time

class Tarea:
    def __init__(self,descripcion):
        self.descripcion = descripcion
        self.completado = False

    def mostrar_tarea(self):
        print(f"Tu tarea es: {self.descripcion}")

    def completar_tarea(self):
        if not self.completado:
            print('Tarea completado')

class Lista_tareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self,tarea):
        for i in range(1):
            self.tareas.append(tarea)
            print('Tarea agregada!')
            print('¿Desea agregar mas tareas?')
            print('1.SI')
            print('2.NO')
            subop = int(input('Escriba su opcion de forma numerica'))
            if subop == 1:
                for i in range(1):
                    self.tareas.append(tarea)
                    print('Tarea agregada!')

            elif subop == 2:
                print('Tarea agregada!')

            else:
                print('Operacion invalida!')

    def mostrar_tareas(self):
        for i in self.tareas:
            i.mostrar_tarea()


#tkinker ver si puedo hacerlo en casa y chequear!

#tareas1 = Tarea('Comprar pan!')
#tareas1.mostrar_tarea()
#tareas2 = Tarea('Comprar un kilo de queso San Bernardo!')
#tareas2.mostrar_tarea()

tareas = Lista_tareas()

while True:
    print('1.Agregar tareas')
    print('2.Ver lista de tareas')
    print('3.Salir')
    op = int(input('Escriba la operacion que desea hacer en forma numerica'))
    if op == 1:
        print('Ha seleccionado la opcion 1')
        texto = input('Escriba la tarea que desea almacenar!')
        tarea_prueba = Tarea(texto)
        tareas.agregar_tarea(tarea_prueba)
        #tareas3.agregar_tarea(tareas1)
        #tareas3.agregar_tarea(tareas2)
    elif op == 2:
        print('Ha seleccionado la opcion 2')
        total = 50
        for i in range(total + 1):
            porcentaje = int((i / total) * 100)
            barra = "█" * i + "░" * (total - i)
            print(f"\r[{barra}] {porcentaje}%", end="", flush=True)
            time.sleep(0.05)
        print()  # salto de línea final
        tareas.mostrar_tareas()
    elif op == 3:
        print('Ha seleccionado la opcion 3')
        print('Adios! Vuelva pronto!')
        break
    else:
        print('Escriba el numero de la operacion correcta!')
