# ================================================================
# VISUALIZADOR DE CONTRASEÑAS WiFi
# ================================================================
# Este programa muestra todas las redes WiFi guardadas en tu PC
# y te permite ver la contraseña de cualquiera de ellas.
# 
# SOLO FUNCIONA EN WINDOWS
# NECESITA EJECUTARSE COMO ADMINISTRADOR para ver las claves
# ================================================================

import subprocess
import re
import os
import sys

# ================================================================
# FUNCIÓN: Obtener lista de perfiles WiFi
# ================================================================

def obtener_perfiles():
    """
    Ejecuta el comando 'netsh wlan show profiles' y extrae
    los nombres de todas las redes WiFi guardadas en el sistema.
    
    Retorna:
        Una lista con los nombres de los perfiles WiFi.
        Si no hay perfiles o hay error, retorna una lista vacía.
    """
    try:
        # Ejecutar el comando y capturar la salida
        resultado = subprocess.run(
            ["netsh", "wlan", "show", "profiles"],
            capture_output=True,
            text=True,
            encoding="utf-8"
        )
        
        # Verificar si hubo error
        if resultado.returncode != 0:
            print("❌ Error al ejecutar el comando.")
            print(f"   {resultado.stderr}")
            return []
        
        # Procesar la salida línea por línea
        perfiles = []
        for linea in resultado.stdout.split("\n"):
            # Buscar líneas que contienen "All User Profile"
            if "Todos los perfiles de usuario" in linea or "All User Profile" in linea:
                # Extraer el nombre del perfil (lo que está después de ":")
                # Ejemplo: "    Todos los perfiles de usuario : WiFi_Red"
                partes = linea.split(":")
                if len(partes) >= 2:
                    nombre = partes[1].strip()
                    if nombre:  # Si no está vacío
                        perfiles.append(nombre)
        
        return perfiles
    
    except FileNotFoundError:
        print("❌ Comando 'netsh' no encontrado. ¿Estás en Windows?")
        return []
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return []

# ================================================================
# FUNCIÓN: Obtener contraseña de un perfil WiFi
# ================================================================

def obtener_contraseña(nombre_perfil):
    """
    Ejecuta el comando 'netsh wlan show profile name="..." key=clear'
    y extrae la contraseña (Key Content) del perfil especificado.
    
    Parámetros:
        nombre_perfil: El nombre de la red WiFi.
    
    Retorna:
        La contraseña de la red, o None si no se pudo obtener.
    """
    try:
        # Ejecutar el comando con key=clear para mostrar la clave
        resultado = subprocess.run(
            ["netsh", "wlan", "show", "profile", f"name={nombre_perfil}", "key=clear"],
            capture_output=True,
            text=True,
            encoding="utf-8"
        )
        
        if resultado.returncode != 0:
            print(f"❌ Error al obtener información de '{nombre_perfil}'")
            return None
        
        # Buscar la línea que contiene "Contenido de la clave" o "Key Content"
        for linea in resultado.stdout.split("\n"):
            if "Contenido de la clave" in linea or "Key Content" in linea:
                partes = linea.split(":")
                if len(partes) >= 2:
                    clave = partes[1].strip()
                    if clave:
                        return clave
        
        # Si no se encontró la clave, puede ser que el perfil no tenga contraseña
        # o que no se ejecutó como administrador
        return None
    
    except Exception as e:
        print(f"❌ Error al obtener contraseña: {e}")
        return None

# ================================================================
# FUNCIÓN: Verificar si se ejecuta como administrador
# ================================================================

def es_administrador():
    """
    Verifica si el programa se está ejecutando con permisos de administrador.
    Solo en Windows.
    """
    if sys.platform == "win32":
        try:
            import ctypes
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        except:
            return False
    return False

# ================================================================
# PROGRAMA PRINCIPAL
# ================================================================

def main():
    print("=" * 50)
    print("   📶 VISUALIZADOR DE CONTRASEÑAS WiFi")
    print("=" * 50)
    
    # Verificar que estamos en Windows
    if sys.platform != "win32":
        print("❌ Este programa solo funciona en Windows.")
        return
    
    # Verificar permisos de administrador
    if not es_administrador():
        print("\n⚠️ ADVERTENCIA: No estás ejecutando como administrador.")
        print("   Es posible que no puedas ver las contraseñas.")
        print("   Ejecutá el programa como Administrador para ver todas las claves.\n")
    
    # Obtener lista de perfiles
    print("\n🔍 Escaneando redes WiFi guardadas...")
    perfiles = obtener_perfiles()
    
    if not perfiles:
        print("❌ No se encontraron perfiles WiFi guardados.")
        print("   Asegurate de tener redes guardadas en tu sistema.")
        return
    
    # Mostrar perfiles numerados
    print(f"\n✅ Se encontraron {len(perfiles)} redes:\n")
    for i, nombre in enumerate(perfiles, 1):
        print(f"   {i}. {nombre}")
    
    # Pedir al usuario que elija una red
    print("\n" + "-" * 50)
    while True:
        try:
            opcion = input("👉 Elegí el número de la red (o 0 para salir): ")
            
            if opcion == "0":
                print("\n👋 ¡Hasta luego!")
                return
            
            indice = int(opcion)
            
            if 1 <= indice <= len(perfiles):
                break
            else:
                print(f"❌ Número inválido. Elegí un número del 1 al {len(perfiles)}.")
        except ValueError:
            print("❌ Ingresá un número válido.")
    
    # Obtener el nombre del perfil seleccionado
    nombre_elegido = perfiles[indice - 1]
    print(f"\n🔍 Obteniendo información de: {nombre_elegido}")
    print("-" * 50)
    
    # Obtener la contraseña
    clave = obtener_contraseña(nombre_elegido)
    
    # Mostrar resultados
    print(f"\n📶 Red: {nombre_elegido}")
    
    if clave is not None:
        print(f"🔑 Contraseña: {clave}")
    else:
        print("🔑 Contraseña: No disponible")
        print("   (Probá ejecutando como Administrador)")
    
    # Mostrar información adicional si se ejecutó como admin
    if es_administrador():
        print("\n✅ Ejecutado como Administrador. Todas las claves son visibles.")
    
    print("\n" + "=" * 50)

# ================================================================
# EJECUCIÓN
# ================================================================

if __name__ == "__main__":
    main()

# ================================================================
# NOTA: Para ejecutar este programa, guardalo como .py y corré:
#       python wifi_viewer.py
# 
#       Para ver las contraseñas, necesitás ejecutarlo como administrador:
#       - En Windows: click derecho sobre el terminal → "Ejecutar como administrador"
# ================================================================