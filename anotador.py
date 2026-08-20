import os #type :ignore
import pyfiglet #type :ignore
from datetime import datetime #type :ignore
from colorama import Style,Fore  #type :ignore

ARCHIVO_NOTAS = "mis_notas.txt" #Lo hare en formato .txt

def mostrar_notas(notas):
    if not notas:
        print('No hay notas')
        print('...Escriba una...')
        return

    print('\n - - - MIS NOTAS - - -')
    for i,nota in enumerate(notas,start = 1):
        print(f"[{i}]{nota['fecha']}")
        print(f"{nota['texto']}")
        print("="*40)

def cargar_notas():
    notas_cargadas = [] #aca se guardaran las notas como diccionarios
    if not os.path.exists(ARCHIVO_NOTAS):
        print('No existe!')
        print('...Escriba algo!...')
        return notas_cargadas #da una lista vacia

    with open(ARCHIVO_NOTAS,"r",encoding="utf-8") as archivo:
        contenido = archivo.read().strip() #aca lee el archivo que uno escribio

    if not contenido:
        return notas_cargadas

    bloques = contenido.split("==NOTAS==")

    for bloque in bloques:
        bloque = bloque.strip()
        if not bloque:
            continue
        lineas = bloque.split("\n")
        fecha = " "
        texto = " "
        for linea in lineas:
            if linea.startswith("Fecha"," ").strip():
                fecha = linea.replace("Fecha:", "").strip()
            elif linea.startswith("Texto"," ").strip():
                texto = linea.replace("Texto:", "").strip()
        if texto:
            notas_cargadas.append({"texto":texto,"fecha":fecha})
    return notas_cargadas

def guardar_notas(notas):
    with open(ARCHIVO_NOTAS,"w",encoding="utf-8") as archivo:
        for nota in notas:
            archivo.write("==NOTAS==\n")
            archivo.write(f"Fecha:{nota['fecha']}\n")
            archivo.write(f"Texto:{nota['texto']}\n\n")

def nueva_nota(notas):
    texto = input('Escriba su nota:')
    if not texto.strip():
        print('No se pudo agregar la nota vacia')
        return
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
    notas.append({"texto":texto,"fecha":fecha})
    guardar_notas(notas)

def editar_nota(notas):
    if not notas:
        print('No hay notas!')
        return
    mostrar_notas(notas)
    indice = int(input('Escriba el numero de su nota:')) - 1
    if 0 <= indice <len(notas):
        nueva_nota_generada = input('Escriba su nueva nota aqui:')
        if not nueva_nota_generada.strip():
            print('Su nueva nota nota NO puede estar vacia, escriba algo!')
            return

        notas[indice]['texto'] = nueva_nota_generada
        notas[indice]['fecha'] = datetime.now().strftime("%d/%m/%Y %H:%M") + " editado"
        guardar_notas(notas)
        print('Nota correctamente guardada')
    else:
        print('Numero invalido!')
        print('Escriba otro numero!')

def borrar_nota(notas):
    if not notas:
        print("No hay notas para borrar.")
        return
    mostrar_notas(notas)
    indice = int(input("Escriba el numero de su nota que desea borrar:")) - 1
    if 0 <= indice < len(notas):
        notas.pop(indice)
        guardar_notas(notas)
        print("Nota correctamente borrada")

    else:
        print('Numero invalido!')
        print('Escriba otro numero!')

def main():
    notas = cargar_notas()
    while True:
        os.system('cls')
        print(Fore.CYAN + pyfiglet.figlet_format("GESTOR DE NOTAS",font="doom"))
        print(Fore.GREEN + "\n1.Ver notas."+Style.RESET_ALL )
        print(Fore.LIGHTCYAN_EX + "\n2.Editar notas." + Style.RESET_ALL )
        print(Fore.BLUE + "\n3.Escribir notas nuevas." + Style.RESET_ALL)
        print(Fore.RED + "\n4.Borrar notas." + Style.RESET_ALL)
        print(Fore.BLACK + "\n5.Guardar notas."+Style.RESET_ALL) 
        print(Fore.WHITE + "\n6.Salir." +Style.RESET_ALL)
        print(Fore.LIGHTWHITE_EX +'Gestor de Notas - Version 1.3  Autor Nahuel Zanini Fecha Fecha actual Licencia Uso personal y educativo. No se permite la redistribución comercial sin autorización expresa.' + Style.RESET_ALL)

        opcion  = int(input('Escriba la operacion que desear hacer de forma numerica:'))

        if opcion == 1:
            mostrar_notas(notas)
        elif opcion == 2:
            editar_nota(notas)
        elif opcion == 3:
            nueva_nota(notas)
        elif opcion == 4:
            borrar_nota(notas)
        elif opcion == 5:
            guardar_notas(notas)
        elif opcion ==6:
            print("Notas guardadas.¡Hasta luego!")
            break
        else:
            print("Opcion no valida.")
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()

