import random
import time
import sys

# ================================================================
# CONFIGURACIÓN
# ================================================================
PASSWORD = "SMARTPYTHON123"  # La contraseña a adivinar
CARACTERES = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"  # Caracteres posibles
MAX_INTENTOS = 1000000  # Límite para evitar que se ejecute para siempre

# ================================================================
# SIMULADOR DE HACKING (FUERZA BRUTA)
# ================================================================
print("🔒 Iniciando hackeo de contraseña...")
time.sleep(1)

# Variables
intentos = 0
encontrada = False

# Bucle principal
for i in range(1, len(PASSWORD) + 1):
    # Intentar adivinar con la longitud actual
    intentos_longitud = 0
    
    while intentos_longitud < MAX_INTENTOS:
        intentos += 1
        intentos_longitud += 1
        
        # Generar una combinación aleatoria de la longitud actual
        guess = "".join(random.choice(CARACTERES) for _ in range(i))
        
        # Mostrar progreso en la misma línea
        print(f"\r🔑 Intentando: {guess} (Longitud: {i})", end="", flush=True)
        time.sleep(0.001)  # Simular tiempo de procesamiento
        
        # Verificar si encontramos la contraseña
        if guess == PASSWORD[:i]:
            # Si adivinamos un prefijo, mostramos avance
            print(f"\r✅ ¡Avance! {i}/{len(PASSWORD)} caracteres coinciden: {guess}")
            
            # Si es la contraseña completa, terminamos
            if i == len(PASSWORD):
                encontrada = True
                print(f"\n🎉 ¡CONTRASEÑA ENCONTRADA! - {PASSWORD}")
                print(f"📊 Intentos totales: {intentos}")
                break
    
    if encontrada:
        break
    
    # Si no se encontró después de muchos intentos, pausa para no saturar
    if not encontrada and intentos_longitud >= MAX_INTENTOS:
        print(f"\n⚠️ Límite de intentos alcanzado para longitud {i}")

if not encontrada:
    print("\n❌ No se pudo encontrar la contraseña. Demasiados intentos.")

# ================================================================
# VERSIÓN MEJORADA CON BARRA DE PROGRESO
# ================================================================
print("\n" + "=" * 50)
print("🔄 VERSIÓN MEJORADA CON PROGRESO")
print("=" * 50)

def simular_hackeo():
    """Versión mejorada con barra de progreso y estadísticas."""
    
    print("\n🚀 Iniciando ataque de fuerza bruta...")
    time.sleep(1)
    
    total_caracteres = len(PASSWORD)
    intentos = 0
    
    for i in range(total_caracteres + 1):
        # Mostrar barra de progreso
        progreso = int((i / total_caracteres) * 100)
        barra = "█" * i + "░" * (total_caracteres - i)
        print(f"\r[{barra}] {progreso}% - Descifrando...", end="", flush=True)
        time.sleep(0.3)
        
        # Simular que probamos combinaciones
        for j in range(100):  # Intentos por cada carácter
            intentos += 1
            guess = "".join(random.choice(CARACTERES) for _ in range(i))
            
            if i > 0 and guess == PASSWORD[:i]:
                # Simular que encontramos un carácter
                print(f"\n✅ Carácter {i}/{total_caracteres} descifrado")
                break
    
    print(f"\n🎉 ¡Hackeo completado! Contraseña: {PASSWORD}")
    print(f"📊 Intentos totales: {intentos}")

simular_hackeo()

# ================================================================
# VERSIÓN CON ESTADÍSTICAS EN TIEMPO REAL
# ================================================================
print("\n" + "=" * 50)
print("📊 VERSIÓN CON ESTADÍSTICAS")
print("=" * 50)

def hackeo_con_estadisticas():
    """Versión que muestra estadísticas en tiempo real."""
    
    intentos = 0
    inicio = time.time()
    
    print("\n🔍 Analizando sistema...")
    time.sleep(1)
    
    for i in range(1, len(PASSWORD) + 1):
        for j in range(1000):  # Intentos por carácter
            intentos += 1
            guess = "".join(random.choice(CARACTERES) for _ in range(i))
            
            # Calcular velocidad
            velocidad = intentos / (time.time() - inicio) if time.time() - inicio > 0 else 0
            
            # Mostrar estadísticas
            print(f"\r🔑 Intentos: {intentos} | Velocidad: {velocidad:.0f} comb/seg | Probando: {guess}", end="", flush=True)
            time.sleep(0.0005)
            
            if guess == PASSWORD[:i]:
                if i == len(PASSWORD):
                    print(f"\n🎉 ¡CONTRASEÑA ENCONTRADA! - {PASSWORD}")
                    print(f"📊 Intentos totales: {intentos}")
                    print(f"⏱️ Tiempo: {time.time() - inicio:.2f} segundos")
                    return

hackeo_con_estadisticas()

# ================================================================
# VERSIÓN "PELÍCULA" (para impresionar)
# ================================================================
print("\n" + "=" * 50)
print("🎬 VERSIÓN PELÍCULA DE HACKEO")
print("=" * 50)

def hackeo_pelicula():
    """Versión con efectos visuales tipo película."""
    
    # Lista de frases para efectos
    frases = [
        "Conectando a servidor...",
        "Bypass firewall en progreso...",
        "Escaneando vulnerabilidades...",
        "Explotando fallo de seguridad...",
        "Acceso concedido",
        "Descifrando contraseña..."
    ]
    
    for frase in frases:
        print(f"\r🖥️ {frase}", end="", flush=True)
        time.sleep(random.uniform(0.5, 1.5))
    
    # Simular el hackeo con efecto de "código cayendo"
    print("\n")
    for i in range(len(PASSWORD)):
        for j in range(5):  # Efecto de "búsqueda"
            char = random.choice(CARACTERES)
            print(f"\r🔓 Encontrando carácter {i+1}: {char}", end="", flush=True)
            time.sleep(0.05)
        print(f"\r✅ Carácter {i+1} encontrado: {PASSWORD[i]}")
        time.sleep(0.3)
    
    print(f"\n🎬 ¡HACKEO COMPLETADO! Contraseña: {PASSWORD}")
    print("🕵️ Acceso garantizado...")

hackeo_pelicula()

# ================================================================
# FIN DEL PROGRAMA
# ================================================================
print("\n" + "=" * 50)
print("   🚀 SIMULACIÓN FINALIZADA")
print("=" * 50)