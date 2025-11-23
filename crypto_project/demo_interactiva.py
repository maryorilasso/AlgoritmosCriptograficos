# ========================
# DEMOSTRACIÓN INTERACTIVA
# Script para demostrar cada funcionalidad del proyecto
# ========================

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from aescipher import generate_aes_key, encrypt_file_gcm, decrypt_file_gcm
from rsautils import generate_rsa_keypair, sign_message, verify_signature, load_private_key, load_public_key
from hashutils import calculate_file_hash, register_file, verify_file_integrity
from hybrid import encrypt_file_hybrid, decrypt_file_hybrid
import os

def separador(titulo):
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)

def pausa():
    input("\nPresiona ENTER para continuar...")

# ========================
# MENÚ PRINCIPAL
# ========================
def menu_principal():
    while True:
        separador("PROYECTO DE CRIPTOGRAFÍA - DEMOSTRACIÓN INTERACTIVA")
        print("""
1. Cifrado Simétrico (AES)
2. Cifrado Asimétrico (RSA)
3. Firma Digital
4. Verificación de Integridad (SHA-256)
5. Esquema Híbrido (AES + RSA)
6. Ejecutar todas las demos
0. Salir
        """)
        
        opcion = input("Selecciona una opción: ").strip()
        
        if opcion == "1":
            demo_aes()
        elif opcion == "2":
            demo_rsa()
        elif opcion == "3":
            demo_firma()
        elif opcion == "4":
            demo_integridad()
        elif opcion == "5":
            demo_hibrido()
        elif opcion == "6":
            ejecutar_todas()
        elif opcion == "0":
            print("\n¡Hasta luego!")
            break
        else:
            print("\n❌ Opción inválida")

# ========================
# DEMO 1: AES
# ========================
def demo_aes():
    separador("DEMOSTRACIÓN: CIFRADO SIMÉTRICO AES")
    
    print("\n📝 Escribe un mensaje para cifrar:")
    mensaje = input("> ").encode()
    
    if not mensaje:
        mensaje = b"Mensaje de prueba predeterminado"
    
    # Guardar mensaje
    with open("tests/mensaje_aes.txt", "wb") as f:
        f.write(mensaje)
    
    print("\n🔐 Generando clave AES-256...")
    key = generate_aes_key(256)
    print(f"✓ Clave generada: {key.hex()[:64]}...")
    
    # Guardar clave
    with open("tests/aes_key.bin", "wb") as f:
        f.write(key)
    
    print("\n🔒 Cifrando mensaje...")
    nonce, tag = encrypt_file_gcm("tests/mensaje_aes.txt", "tests/mensaje_cifrado.enc", key)
    print(f"✓ Mensaje cifrado guardado en: tests/mensaje_cifrado.enc")
    print(f"✓ Tamaño original: {len(mensaje)} bytes")
    print(f"✓ Tamaño cifrado: {os.path.getsize('tests/mensaje_cifrado.enc')} bytes")
    
    print("\n🔓 Descifrando mensaje...")
    decrypt_file_gcm("tests/mensaje_cifrado.enc", "tests/mensaje_descifrado.txt", key)
    
    with open("tests/mensaje_descifrado.txt", "rb") as f:
        recuperado = f.read()
    
    print(f"✓ Mensaje descifrado: '{recuperado.decode()}'")
    print(f"✓ Verificación: {mensaje == recuperado}")
    
    pausa()

# ========================
# DEMO 2: RSA
# ========================
def demo_rsa():
    separador("DEMOSTRACIÓN: CIFRADO ASIMÉTRICO RSA")
    
    print("\n🔐 Generando par de claves RSA-2048...")
    priv, pub = generate_rsa_keypair(2048)
    
    with open("tests/demo_private.pem", "wb") as f:
        f.write(priv)
    with open("tests/demo_public.pem", "wb") as f:
        f.write(pub)
    
    print("✓ Claves generadas:")
    print("  - Clave privada: tests/demo_private.pem")
    print("  - Clave pública: tests/demo_public.pem")
    
    print("\n📝 Las claves RSA se usan principalmente para:")
    print("  1. Intercambio seguro de claves")
    print("  2. Firma digital")
    print("  3. Autenticación")
    
    print("\n💡 Nota: Para cifrar archivos grandes, usar esquema híbrido (opción 5)")
    
    pausa()

# ========================
# DEMO 3: FIRMA DIGITAL
# ========================
def demo_firma():
    separador("DEMOSTRACIÓN: FIRMA DIGITAL")
    
    print("\n📝 Escribe un documento para firmar:")
    documento = input("> ").encode()
    
    if not documento:
        documento = b"Este es un documento oficial importante"
    
    print("\n🔐 Generando claves para firma...")
    priv, pub = generate_rsa_keypair(2048)
    
    priv_key = load_private_key(priv)
    pub_key = load_public_key(pub)
    
    print("\n✍️  Firmando documento...")
    firma = sign_message(documento, priv_key)
    print(f"✓ Firma generada ({len(firma)} bytes)")
    print(f"  {firma.hex()[:64]}...")
    
    print("\n✅ Verificando firma...")
    valida = verify_signature(documento, firma, pub_key)
    print(f"✓ Firma válida: {valida}")
    
    print("\n⚠️  Simulando modificación del documento...")
    documento_falso = documento + b" [MODIFICADO]"
    valida_falso = verify_signature(documento_falso, firma, pub_key)
    print(f"✓ Firma válida con documento modificado: {valida_falso}")
    print("✓ La firma digital detectó la modificación correctamente!")
    
    pausa()

# ========================
# DEMO 4: INTEGRIDAD
# ========================
def demo_integridad():
    separador("DEMOSTRACIÓN: VERIFICACIÓN DE INTEGRIDAD")
    
    # Crear archivo de prueba
    print("\n📄 Creando archivo de prueba...")
    contenido = b"Documento importante que debe mantener su integridad\n"
    contenido += b"Fecha: 2025-11-23\n"
    contenido += b"Contenido sensible..."
    
    with open("tests/documento_importante.txt", "wb") as f:
        f.write(contenido)
    
    print("✓ Archivo creado: tests/documento_importante.txt")
    
    print("\n🔍 Calculando hash SHA-256...")
    hash_original = calculate_file_hash("tests/documento_importante.txt")
    print(f"✓ Hash: {hash_original}")
    
    print("\n📝 Registrando en base de datos de integridad...")
    register_file("tests/documento_importante.txt", "tests/demo_integrity.json")
    print("✓ Archivo registrado")
    
    print("\n✅ Verificando integridad (sin modificaciones)...")
    result = verify_file_integrity("tests/documento_importante.txt", "tests/demo_integrity.json")
    print(f"✓ {result['message']}")
    
    print("\n⚠️  Simulando modificación maliciosa...")
    input("Presiona ENTER para modificar el archivo...")
    
    with open("tests/documento_importante.txt", "ab") as f:
        f.write(b"\n[DATOS AGREGADOS POR ATACANTE]")
    
    print("✓ Archivo modificado")
    
    print("\n🔍 Verificando integridad nuevamente...")
    result2 = verify_file_integrity("tests/documento_importante.txt", "tests/demo_integrity.json")
    print(f"✓ {result2['message']}")
    print(f"  Hash original: {result2['original_hash']}")
    print(f"  Hash actual:   {result2['current_hash']}")
    print("\n✓ ¡El sistema detectó la modificación!")
    
    # Restaurar
    with open("tests/documento_importante.txt", "wb") as f:
        f.write(contenido)
    
    pausa()

# ========================
# DEMO 5: HÍBRIDO
# ========================
def demo_hibrido():
    separador("DEMOSTRACIÓN: ESQUEMA HÍBRIDO AES + RSA")
    
    print("\n💡 El esquema híbrido combina:")
    print("   - AES: Rápido para cifrar archivos grandes")
    print("   - RSA: Seguro para intercambiar la clave AES")
    
    print("\n📝 Escribe un mensaje para cifrar:")
    mensaje = input("> ").encode()
    
    if not mensaje:
        mensaje = b"Este es un archivo grande que se cifrara de forma hibrida" * 100
    
    print("\n👤 Generando claves para el receptor...")
    priv, pub = generate_rsa_keypair(2048)
    
    print("\n🔐 Cifrando con esquema híbrido...")
    print("   1. Generando clave AES aleatoria...")
    print("   2. Cifrando contenido con AES-GCM...")
    print("   3. Cifrando clave AES con RSA (clave pública)...")
    
    enc_key, nonce, tag, ciphertext = encrypt_file_hybrid(mensaje, pub)
    
    print(f"✓ Cifrado completado")
    print(f"  - Tamaño original: {len(mensaje)} bytes")
    print(f"  - Clave AES cifrada: {len(enc_key)} bytes")
    print(f"  - Contenido cifrado: {len(ciphertext)} bytes")
    
    print("\n🔓 Descifrando con esquema híbrido...")
    print("   1. Descifrando clave AES con RSA (clave privada)...")
    print("   2. Descifrando contenido con AES-GCM...")
    
    recuperado = decrypt_file_hybrid(enc_key, nonce, tag, ciphertext, priv)
    
    print(f"✓ Descifrado exitoso")
    print(f"✓ Contenido recuperado correctamente: {mensaje == recuperado}")
    
    pausa()

# ========================
# EJECUTAR TODAS
# ========================
def ejecutar_todas():
    print("\n🚀 Ejecutando todas las demostraciones...\n")
    demo_aes()
    demo_rsa()
    demo_firma()
    demo_integridad()
    demo_hibrido()
    print("\n✅ ¡Todas las demostraciones completadas!")
    pausa()

if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrumpido por el usuario")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
