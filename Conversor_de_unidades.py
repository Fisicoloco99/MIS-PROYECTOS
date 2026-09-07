# Primero que nada voy a ir de a poco, quiero empezar con lo que me habia interesado del menu para lo del convertidor de unidades , voy a hacer con Metros asi pruebo

# 1. Importar modulo/libreria
import tkinter as tk  # type:ignore

# 2. Voy a crear una funcion para que funcione. Esta abre la ventana secundaria con los menus.
def abrir_conversor_longitud():  # No le paso variables
    # Crear ventana secundaria (hija de la ventana principal)
    ventana_metros = tk.Toplevel(ventana)  # aca estaria haciendo que haya una ventana nueva o hija
    ventana_metros.title('CONVERSOR DE UNIDADES')  # titulo para la ventana
    ventana_metros.geometry('500x500')  # geometria de la ventana, un poco mas grande para que entre todo

    # 3. Mensaje para el usuario con la instruccion para que escriba
    tk.Label(ventana_metros, text='Ingrese el valor a convertir:').pack()

    # 4. Entry para el numero, o sea, aca el usuario ingresa el numero
    valor_ingresar_usuario = tk.Entry(ventana_metros)
    valor_ingresar_usuario.pack()

    # 5. Menu desplegable con las unidades
    unidades = ['Ym', 'Zm', 'Em', 'Pm', 'Tm', 'Gm', 'Mm', 'km', 'hm', 'dam','metros', 'dm', 'cm', 'mm', 'um', 'nm', 'pm', 'fm', 'am', 'zm', 'ym']

    # 6. Variables que guardara la opcion elegida (origen)
    variable_origen = tk.StringVar(ventana_metros)  # esta variable es un tipo de dato string
    variable_origen.set('metros')  # valor por defecto

    # 7. Variable que guardara la opcion elegida (destino)
    variable_destino = tk.StringVar(ventana_metros)
    variable_destino.set('cm')  # valor por defecto

    # 8. Frame para poner los dos menus en la misma fila
    frame_menus = tk.Frame(ventana_metros)
    frame_menus.pack()

    # 9. Label de Menu de origen y Menu de origen
    tk.Label(frame_menus, text='Origen:').pack(side=tk.LEFT)
    menu_origen = tk.OptionMenu(frame_menus, variable_origen, *unidades)
    menu_origen.pack(side=tk.LEFT)

    # 10. Label de Menu de destino y Menu de destino
    tk.Label(frame_menus, text='Destino:').pack(side=tk.LEFT)
    menu_destino = tk.OptionMenu(frame_menus, variable_destino, *unidades)
    menu_destino.pack(side=tk.LEFT)

    # 11. Funcion para convertir unidad (dentro de abrir_conversor_longitud para que pueda usar las variables)
    def convertir():
        try:
            # 12. Obtener el valor numerico del Entry
            valor = float(valor_ingresar_usuario.get())
        except ValueError:
            # Si el usuario escribio letras, mostramos error
            label_resultado.config(text="ERROR: Escribe un número válido")
            return

        # 13. Obtener las unidades elegidas
        unidad_origen = variable_origen.get()
        unidad_destino = variable_destino.get()

        # ============================================================
        # 14. PASO 1: Convertir de la unidad de origen a METROS
        # ============================================================
        # Las unidades grandes se multiplican por 10^exponente
        # Las unidades pequenas se dividen por 10^exponente (o multiplican por 10^-exponente)

        if unidad_origen == 'metros':
            valor_en_metros = valor
        elif unidad_origen == 'Ym':  # Yottametro = 10^24 metros
            valor_en_metros = valor * 10**24
        elif unidad_origen == 'Zm':  # Zettametro = 10^21
            valor_en_metros = valor * 10**21
        elif unidad_origen == 'Em':  # Exametro = 10^18
            valor_en_metros = valor * 10**18
        elif unidad_origen == 'Pm':  # Petametro = 10^15
            valor_en_metros = valor * 10**15
        elif unidad_origen == 'Tm':  # Terametro = 10^12
            valor_en_metros = valor * 10**12
        elif unidad_origen == 'Gm':  # Gigametro = 10^9
            valor_en_metros = valor * 10**9
        elif unidad_origen == 'Mm':  # Megametro = 10^6
            valor_en_metros = valor * 10**6
        elif unidad_origen == 'km':  # Kilometro = 10^3
            valor_en_metros = valor * 10**3
        elif unidad_origen == 'hm':  # Hectometro = 10^2
            valor_en_metros = valor * 10**2
        elif unidad_origen == 'dam': # Decametro = 10^1
            valor_en_metros = valor * 10**1
        elif unidad_origen == 'dm':  # Decimetro = 10^-1
            valor_en_metros = valor / 10**1   # o valor * 10**-1
        elif unidad_origen == 'cm':  # Centimetro = 10^-2
            valor_en_metros = valor / 10**2
        elif unidad_origen == 'mm':  # Milimetro = 10^-3
            valor_en_metros = valor / 10**3
        elif unidad_origen == 'um':  # Micrometro = 10^-6
            valor_en_metros = valor / 10**6
        elif unidad_origen == 'nm':  # Nanometro = 10^-9
            valor_en_metros = valor / 10**9
        elif unidad_origen == 'pm':  # Picometro = 10^-12
            valor_en_metros = valor / 10**12
        elif unidad_origen == 'fm':  # Femtometro = 10^-15
            valor_en_metros = valor / 10**15
        elif unidad_origen == 'am':  # Attometro = 10^-18
            valor_en_metros = valor / 10**18
        elif unidad_origen == 'zm':  # Zeptometro = 10^-21
            valor_en_metros = valor / 10**21
        elif unidad_origen == 'ym':  # Yoctometro = 10^-24
            valor_en_metros = valor / 10**24
        else:
            valor_en_metros = valor  # por si acaso

        # ============================================================
        # 15. PASO 2: Convertir de METROS a la unidad de destino
        # ============================================================
        if unidad_destino == 'metros':
            resultado = valor_en_metros
        elif unidad_destino == 'Ym':
            resultado = valor_en_metros / 10**24
        elif unidad_destino == 'Zm':
            resultado = valor_en_metros / 10**21
        elif unidad_destino == 'Em':
            resultado = valor_en_metros / 10**18
        elif unidad_destino == 'Pm':
            resultado = valor_en_metros / 10**15
        elif unidad_destino == 'Tm':
            resultado = valor_en_metros / 10**12
        elif unidad_destino == 'Gm':
            resultado = valor_en_metros / 10**9
        elif unidad_destino == 'Mm':
            resultado = valor_en_metros / 10**6
        elif unidad_destino == 'km':
            resultado = valor_en_metros / 10**3
        elif unidad_destino == 'hm':
            resultado = valor_en_metros / 10**2
        elif unidad_destino == 'dam':
            resultado = valor_en_metros / 10**1
        elif unidad_destino == 'dm':
            resultado = valor_en_metros * 10**1   # o valor_en_metros * 10
        elif unidad_destino == 'cm':
            resultado = valor_en_metros * 10**2
        elif unidad_destino == 'mm':
            resultado = valor_en_metros * 10**3
        elif unidad_destino == 'um':
            resultado = valor_en_metros * 10**6
        elif unidad_destino == 'nm':
            resultado = valor_en_metros * 10**9
        elif unidad_destino == 'pm':
            resultado = valor_en_metros * 10**12
        elif unidad_destino == 'fm':
            resultado = valor_en_metros * 10**15
        elif unidad_destino == 'am':
            resultado = valor_en_metros * 10**18
        elif unidad_destino == 'zm':
            resultado = valor_en_metros * 10**21
        elif unidad_destino == 'ym':
            resultado = valor_en_metros * 10**24
        else:
            resultado = valor_en_metros  # por si acaso

        # 16. Mostrar el resultado en el Label
        label_resultado.config(text=f"{valor} {unidad_origen} = {resultado} {unidad_destino}")

    # 17. Boton para convertir
    boton_convertir = tk.Button(ventana_metros, text='Convertir', command=convertir)
    boton_convertir.pack()

    # Label para mostrar el resultado
    label_resultado = tk.Label(ventana_metros, text="", font=("Arial", 12))
    label_resultado.pack()

    # Boton para cerrar
    boton_cerrar = tk.Button(ventana_metros, text='Cerrar', command=ventana_metros.destroy)
    boton_cerrar.pack()

def abrir_conversor_tiempo():
    #1.Crear una ventana para unidades de tiempo
    ventana_tiempo = tk.Toplevel(ventana)
    ventana_tiempo.title('CONVERSOR DE UNIDADES')  # titulo para la ventana
    ventana_tiempo.geometry('500x500')  # geometria de la ventana, un poco mas grande para que entre todo
    #2.Creo la entrada para las unidades
    valor_ingresar_usuario = tk.Entry(ventana_tiempo)
    valor_ingresar_usuario.pack()
    #3. Aca voy a escribir la lista de todas las unidades conocidas
    unidades_tiempo = ["rs","qs","ys","zs","as","fs","ps","ns","µs","ms","s","min","h","d","ks","Ms","Gs","Ts","Ps","Es","Zs","Ys","semana","quincena","mes","bimestre","trimestre","cuatrimestre","semestre","a","bienio","trienio","cuatrienio","lustro","sexenio","dec","indiccion","siglo","milenio","eon","tp","shake","Sv","jiffy","a_jul","a_trop","a_sid","gran_ano","a_gal"]
    #4.Ahora voy a crear la variable origen
    variable_origen = tk.StringVar(ventana_tiempo)  # esta variable es un tipo de dato string
    variable_origen.set('segundos')  # valor por defecto
    # 5.Variable que guardara la opcion elegida (destino)
    variable_destino = tk.StringVar(ventana_tiempo)
    variable_destino.set('min')  # valor por defecto
    # 6.Frame para poner los dos menus en la misma fila
    frame_menus = tk.Frame(ventana_tiempo)
    frame_menus.pack()
    #7.Label de Menu de origen y Menu de origen
    tk.Label(frame_menus, text='Origen:').pack(side=tk.LEFT)
    menu_origen = tk.OptionMenu(frame_menus, variable_origen, *unidades_tiempo)
    menu_origen.pack(side=tk.LEFT)
    #8. Label de Menu de destino y Menu de destino
    tk.Label(frame_menus, text='Destino:').pack(side=tk.LEFT)
    menu_destino = tk.OptionMenu(frame_menus, variable_destino, *unidades_tiempo)
    menu_destino.pack(side=tk.LEFT)
    #9.Funcion para convertir unidad (dentro de abrir_conversor_longitud para que pueda usar las variables)
    def convertir_tiempo():
        try:
            # 10. Obtener el valor numerico del Entry
            valor = float(valor_ingresar_usuario.get())
        except ValueError:
            # Si el usuario escribio letras, mostramos error
            label_resultado.config(text="ERROR: Escribe un numero valido")
            return
        #10. Obtener las unidades elegidas
        unidad_origen = variable_origen.get()
        unidad_destino = variable_destino.get()  
        if unidad_origen == 's':
            valor_en_segundos = valor
        elif unidad_origen == "qs":  # Quectosegundo = 10^-30
            valor_en_segundos = valor * 10**(-30)
        elif unidad_origen == "rs":  # Rontosegundo = 10^-27
            valor_en_segundos = valor * 10**(-27)
        elif unidad_origen == "ys":  # Yoctosegundo = 10^-24
            valor_en_segundos = valor * 10**(-24)
        elif unidad_origen == "zs":  # Zeptosegundo = 10^-21
            valor_en_segundos = valor * 10**(-21)
        elif unidad_origen == "as":  # Attosegundo = 10^-18
            valor_en_segundos = valor * 10**(-18)
        elif unidad_origen == "fs":  # Femtosegundo = 10^-15
            valor_en_segundos = valor * 10**(-15)
        elif unidad_origen == "ps":  # Picosegundo = 10^-12
            valor_en_segundos = valor * 10**(-12)
        elif unidad_origen == "ns":  # Nanosegundo = 10^-9
            valor_en_segundos = valor * 10**(-9)
        elif unidad_origen == "µs":  # Microsegundo = 10^-6
            valor_en_segundos = valor * 10**(-6)
        elif unidad_origen == "ms":  # Milisegundo = 10^-3
            valor_en_segundos = valor * 10**(-3)
        elif unidad_origen == "min":  # Minuto
            valor_en_segundos = valor * 60
        elif unidad_origen == "h":  # Hora
            valor_en_segundos = valor * 3600
        elif unidad_origen == "d":  # Día
            valor_en_segundos = valor * 86400
        elif unidad_origen == "ks":  # Kilosegundo = 10^3
            valor_en_segundos = valor * 10**3
        elif unidad_origen == "Ms":  # Megasegundo = 10^6
            valor_en_segundos = valor * 10**6
        elif unidad_origen == "Gs":  # Gigasegundo = 10^9
            valor_en_segundos = valor * 10**9
        elif unidad_origen == "Ts":  # Terasegundo = 10^12
            valor_en_segundos = valor * 10**12
        elif unidad_origen == "Ps":  # Petasegundo = 10^15
            valor_en_segundos = valor * 10**15
        elif unidad_origen == "Es":  # Exasegundo = 10^18
            valor_en_segundos = valor * 10**18
        elif unidad_origen == "Zs":  # Zettasegundo = 10^21
            valor_en_segundos = valor * 10**21
        elif unidad_origen == "Ys":  # Yottasegundo = 10^24
            valor_en_segundos = valor * 10**24
        else:
            valor_en_segundos = valor  # por si acaso

        if unidad_destino == 's':
            resultado = valor_en_segundos
        elif unidad_destino == "Ys":
            resultado = valor_en_segundos / 10**24
        elif unidad_destino == "Zs":
            resultado = valor_en_segundos / 10**21
        elif unidad_destino == "Es":
            resultado = valor_en_segundos / 10**18
        elif unidad_destino == "Ps":
            resultado = valor_en_segundos / 10**15
        elif unidad_destino == "Ts":
            resultado = valor_en_segundos / 10**12
        elif unidad_destino == "Gs":
            resultado = valor_en_segundos / 10**9
        elif unidad_destino == "Ms":
            resultado = valor_en_segundos / 10**6
        elif unidad_destino == "ks":
            resultado = valor_en_segundos / 10**3
        elif unidad_destino == "d":
            resultado = valor_en_segundos / 86400
        elif unidad_destino == "h":
            resultado = valor_en_segundos / 3600
        elif unidad_destino == "min":
            resultado = valor_en_segundos / 60
        elif unidad_destino == "ms":
            resultado = valor_en_segundos * 10**3
        elif unidad_destino == "µs":
            resultado = valor_en_segundos * 10**6
        elif unidad_destino == "ns":
            resultado = valor_en_segundos * 10**9
        elif unidad_destino == "ps":
            resultado = valor_en_segundos * 10**12
        elif unidad_destino == "fs":
            resultado = valor_en_segundos * 10**15
        elif unidad_destino == "as":
            resultado = valor_en_segundos * 10**18
        elif unidad_destino == "zs":
            resultado = valor_en_segundos * 10**21
        elif unidad_destino == "ys":
            resultado = valor_en_segundos * 10**24
        elif unidad_destino == "rs":
            resultado = valor_en_segundos * 10**27
        elif unidad_destino == "qs":
            resultado = valor_en_segundos * 10**30
        else:
            resultado = valor_en_segundos  # por si acaso
    #11. Mostrar el resultado en el Label
        label_resultado.config(text=f"{valor} {unidad_origen} = {resultado} {unidad_destino}")   
    #12. Boton para convertir
    boton_convertir = tk.Button(ventana_tiempo, text='Convertir', command=convertir_tiempo)
    boton_convertir.pack()

    #13.Label para mostrar el resultado
    label_resultado = tk.Label(ventana_tiempo, text="", font=("Arial", 12))
    label_resultado.pack()

    #14.Boton para cerrar
    boton_cerrar = tk.Button(ventana_tiempo, text='Cerrar', command=ventana_tiempo.destroy)
    boton_cerrar.pack()
# ============================================================
# 18. VENTANA PRINCIPAL
# ============================================================
ventana = tk.Tk()
ventana.title("Conversor de unidades")
ventana.geometry("500x400")

mensaje = tk.Label(ventana, text="--- MENU PRINCIPAL ---", font=("Arial", 16))
mensaje.pack()
#Boton para metros
btn_metros = tk.Button(ventana, text="LONGITUD", command=abrir_conversor_longitud)
btn_metros.pack()
#Boton para tiempo
btn_tiempo = tk.Button(ventana,text='TIEMPO', command=abrir_conversor_tiempo)
btn_tiempo.pack()

# 19. Iniciar el bucle principal
ventana.mainloop()