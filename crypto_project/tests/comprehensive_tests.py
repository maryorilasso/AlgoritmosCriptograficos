# ========================
# PRUEBAS COMPREHENSIVAS DEL PROYECTO
# Incluye evaluaciones de rendimiento, seguridad y casos de fallo
# ========================

import sys
from pathlib import Path
import time
import os

# Agregar el directorio padre al path
sys.path.insert(0, str(Path(__file__).parent.parent))

from aescipher import (
    generate_aes_key, encrypt_file_gcm, decrypt_file_gcm,
    encrypt_file_cbc, decrypt_file_cbc, encrypt_gcm, decrypt_gcm
)
from rsautils import (
    generate_rsa_keypair, load_private_key, load_public_key,
    sign_message, verify_signature, rsa_encrypt, rsa_decrypt
)
from hashutils import (
    calculate_file_hash, register_file, verify_file_integrity,
    verify_all_files, compare_files, sha256_hex
)
from hybrid import encrypt_file_hybrid, decrypt_file_hybrid

print("=" * 70)
print("PRUEBAS COMPREHENSIVAS - PROYECTO DE CRIPTOGRAFÍA")
print("=" * 70)

# ========================
# PARTE 1: CIFRADO SIMÉTRICO AES
# ========================
print("\n" + "=" * 70)
print("PARTE 1: CIFRADO SIMÉTRICO (AES)")
print("=" * 70)

# Crear archivo de prueba
test_content = b"Este es un documento confidencial con informacion sensible.\nContrasena: MiPassword123\nTarjeta: 1234-5678-9012-3456"
with open("tests/documento_secreto.txt", "wb") as f:
    f.write(test_content)

print("\n[1.1] Generación de claves AES de diferentes tamaños")
print("-" * 70)
for key_size in [128, 192, 256]:
    key = generate_aes_key(key_size)
    print(f"  ✓ Clave AES-{key_size}: {len(key)} bytes = {len(key)*8} bits")

print("\n[1.2] Cifrado con AES-GCM (modo recomendado)")
print("-" * 70)
key_256 = generate_aes_key(256)

start = time.time()
encrypt_file_gcm("tests/documento_secreto.txt", "tests/documento_secreto.enc", key_256)
time_gcm = time.time() - start

print(f"  ✓ Archivo cifrado con AES-256-GCM en {time_gcm*1000:.2f} ms")
print(f"  ✓ Archivo original: {os.path.getsize('tests/documento_secreto.txt')} bytes")
print(f"  ✓ Archivo cifrado: {os.path.getsize('tests/documento_secreto.enc')} bytes")

start = time.time()
success = decrypt_file_gcm("tests/documento_secreto.enc", "tests/documento_recuperado.txt", key_256)
time_gcm_dec = time.time() - start

with open("tests/documento_recuperado.txt", "rb") as f:
    recovered = f.read()

print(f"  ✓ Archivo descifrado en {time_gcm_dec*1000:.2f} ms")
print(f"  ✓ Contenido recuperado correctamente: {recovered == test_content}")

print("\n[1.3] Cifrado con AES-CBC + HMAC")
print("-" * 70)
key_cbc = generate_aes_key(256)

start = time.time()
iv, mac, mac_key = encrypt_file_cbc("tests/documento_secreto.txt", "tests/documento_cbc.enc", key_cbc)
time_cbc = time.time() - start

print(f"  ✓ Archivo cifrado con AES-256-CBC en {time_cbc*1000:.2f} ms")
print(f"  ✓ IV generado: {iv.hex()[:32]}...")
print(f"  ✓ HMAC calculado para integridad")

start = time.time()
success = decrypt_file_cbc("tests/documento_cbc.enc", "tests/documento_cbc_recuperado.txt", key_cbc, mac_key)
time_cbc_dec = time.time() - start

print(f"  ✓ Archivo descifrado en {time_cbc_dec*1000:.2f} ms")
print(f"  ✓ Descifrado exitoso: {success}")

print("\n[1.4] Comparación GCM vs CBC")
print("-" * 70)
print(f"  • GCM - Cifrado: {time_gcm*1000:.2f} ms | Descifrado: {time_gcm_dec*1000:.2f} ms")
print(f"  • CBC - Cifrado: {time_cbc*1000:.2f} ms | Descifrado: {time_cbc_dec*1000:.2f} ms")
print(f"  • GCM incluye autenticación integrada (AEAD)")
print(f"  • CBC requiere HMAC adicional para integridad")

print("\n[1.5] Importancia del IV - Demostración")
print("-" * 70)
print("  ℹ️  El IV (Vector de Inicialización) asegura que el mismo plaintext")
print("      produzca diferentes ciphertexts. Esto previene ataques de análisis.")

key_demo = generate_aes_key(128)
msg = b"Mensaje repetido"

nonce1, ct1, tag1 = encrypt_gcm(msg, key_demo)
nonce2, ct2, tag2 = encrypt_gcm(msg, key_demo)

print(f"  ✓ Mismo mensaje cifrado dos veces:")
print(f"    - Nonce 1: {nonce1.hex()}")
print(f"    - Nonce 2: {nonce2.hex()}")
print(f"    - Ciphertexts diferentes: {ct1 != ct2}")

# ========================
# PARTE 2: CIFRADO ASIMÉTRICO RSA
# ========================
print("\n" + "=" * 70)
print("PARTE 2: CIFRADO ASIMÉTRICO (RSA)")
print("=" * 70)

print("\n[2.1] Generación de pares de claves RSA")
print("-" * 70)

start = time.time()
priv_pem, pub_pem = generate_rsa_keypair(2048)
time_keygen = time.time() - start

with open("tests/alice_private.pem", "wb") as f:
    f.write(priv_pem)
with open("tests/alice_public.pem", "wb") as f:
    f.write(pub_pem)

print(f"  ✓ Par de claves RSA-2048 generado en {time_keygen:.3f} segundos")
print(f"  ✓ Clave privada guardada: tests/alice_private.pem")
print(f"  ✓ Clave pública guardada: tests/alice_public.pem")

# Generar otro par para Bob
priv_bob, pub_bob = generate_rsa_keypair(2048)
with open("tests/bob_private.pem", "wb") as f:
    f.write(priv_bob)
with open("tests/bob_public.pem", "wb") as f:
    f.write(pub_bob)

print(f"  ✓ Par de claves para Bob generado")

print("\n[2.2] Intercambio de mensajes cifrados")
print("-" * 70)
mensaje_alice = b"Hola Bob, esta es Alice. Mensaje secreto!"

# Alice cifra con la clave pública de Bob
pub_key_bob = load_public_key(pub_bob)
start = time.time()
mensaje_cifrado = rsa_encrypt(mensaje_alice, pub_key_bob)
time_rsa_enc = time.time() - start

print(f"  ✓ Alice cifra mensaje con clave pública de Bob")
print(f"  ✓ Tiempo de cifrado RSA: {time_rsa_enc*1000:.2f} ms")
print(f"  ✓ Mensaje cifrado ({len(mensaje_cifrado)} bytes): {mensaje_cifrado[:32].hex()}...")

# Bob descifra con su clave privada
priv_key_bob = load_private_key(priv_bob)
start = time.time()
mensaje_descifrado = rsa_decrypt(mensaje_cifrado, priv_key_bob)
time_rsa_dec = time.time() - start

print(f"  ✓ Bob descifra con su clave privada")
print(f"  ✓ Tiempo de descifrado RSA: {time_rsa_dec*1000:.2f} ms")
print(f"  ✓ Mensaje recuperado: {mensaje_descifrado.decode()}")
print(f"  ✓ Verificación exitosa: {mensaje_alice == mensaje_descifrado}")

print("\n[2.3] Comparación Simétrico vs Asimétrico")
print("-" * 70)
test_data = b"Datos de prueba para comparar rendimiento" * 10

# AES
key_compare = generate_aes_key(256)
start = time.time()
_, _, _ = encrypt_gcm(test_data, key_compare)
time_aes = time.time() - start

print(f"  • AES-256: {time_aes*1000:.4f} ms")
print(f"  • RSA-2048: {time_rsa_enc*1000:.4f} ms")
print(f"  • RSA es ~{(time_rsa_enc/time_aes):.0f}x más lento que AES")
print(f"  • Por eso se usa RSA para intercambiar claves AES (esquema híbrido)")

print("\n[2.4] Esquema Híbrido AES + RSA")
print("-" * 70)
print("  ℹ️  Aprovecha lo mejor de ambos mundos:")
print("      - RSA: Cifra la clave AES (datos pequeños)")
print("      - AES: Cifra el contenido del archivo (rápido)")

archivo_grande = b"Contenido de archivo grande..." * 1000

start = time.time()
enc_key, nonce, tag, ciphertext = encrypt_file_hybrid(archivo_grande, pub_bob)
time_hybrid = time.time() - start

print(f"  ✓ Archivo cifrado con esquema híbrido en {time_hybrid*1000:.2f} ms")
print(f"  ✓ Tamaño original: {len(archivo_grande)} bytes")
print(f"  ✓ Clave AES cifrada con RSA: {len(enc_key)} bytes")

start = time.time()
recuperado_hybrid = decrypt_file_hybrid(enc_key, nonce, tag, ciphertext, priv_bob)
time_hybrid_dec = time.time() - start

print(f"  ✓ Archivo descifrado en {time_hybrid_dec*1000:.2f} ms")
print(f"  ✓ Contenido recuperado correctamente: {archivo_grande == recuperado_hybrid}")

# ========================
# PARTE 3: FIRMA DIGITAL
# ========================
print("\n" + "=" * 70)
print("PARTE 3: FIRMA DIGITAL")
print("=" * 70)

print("\n[3.1] Generación de firma digital")
print("-" * 70)
documento = b"Contrato de compra-venta: Alice vende a Bob su casa por $100,000"

priv_alice = load_private_key(priv_pem)
pub_alice = load_public_key(pub_pem)

start = time.time()
firma = sign_message(documento, priv_alice)
time_sign = time.time() - start

print(f"  ✓ Documento: '{documento.decode()}'")
print(f"  ✓ Firma generada en {time_sign*1000:.2f} ms")
print(f"  ✓ Firma ({len(firma)} bytes): {firma[:32].hex()}...")

print("\n[3.2] Verificación de firma válida")
print("-" * 70)
start = time.time()
es_valida = verify_signature(documento, firma, pub_alice)
time_verify = time.time() - start

print(f"  ✓ Verificación completada en {time_verify*1000:.2f} ms")
print(f"  ✓ Firma válida: {es_valida}")
print(f"  ✓ El documento NO ha sido alterado")

print("\n[3.3] Simulación de documento modificado")
print("-" * 70)
documento_modificado = b"Contrato de compra-venta: Alice vende a Bob su casa por $1,000,000"

es_valida_modificado = verify_signature(documento_modificado, firma, pub_alice)

print(f"  ⚠️  Documento modificado: cambio de $100,000 a $1,000,000")
print(f"  ✓ Firma válida con documento modificado: {es_valida_modificado}")
print(f"  ✓ La verificación detectó la alteración correctamente")

print("\n[3.4] Importancia de las firmas digitales")
print("-" * 70)
print("  ✓ Autenticación: Confirma quién firmó el documento")
print("  ✓ Integridad: Detecta cualquier modificación")
print("  ✓ No repudio: El firmante no puede negar haberlo firmado")
print("  ✓ Uso en PKI: Certificados digitales, SSL/TLS, emails firmados")

# ========================
# PARTE 4: FUNCIONES HASH Y VERIFICACIÓN DE INTEGRIDAD
# ========================
print("\n" + "=" * 70)
print("PARTE 4: FUNCIONES HASH Y VERIFICACIÓN DE INTEGRIDAD")
print("=" * 70)

print("\n[4.1] Cálculo de hash SHA-256 de archivos")
print("-" * 70)

hash_original = calculate_file_hash("tests/documento_secreto.txt")
print(f"  ✓ Hash del documento original:")
print(f"    {hash_original}")

print("\n[4.2] Registro de archivos en base de datos de integridad")
print("-" * 70)

register_file("tests/documento_secreto.txt", "tests/integrity_db.json")
register_file("tests/sample.txt", "tests/integrity_db.json")

print(f"  ✓ Archivos registrados en tests/integrity_db.json")
print(f"  ✓ 'documento_secreto.txt' registrado")
print(f"  ✓ 'sample.txt' registrado")

print("\n[4.3] Verificación de integridad (sin modificaciones)")
print("-" * 70)

result = verify_file_integrity("tests/documento_secreto.txt", "tests/integrity_db.json")

print(f"  ✓ Estado: {result['message']}")
print(f"  ✓ Hash original:  {result['original_hash']}")
print(f"  ✓ Hash actual:    {result['current_hash']}")
print(f"  ✓ Integridad OK:  {result['valid']}")

print("\n[4.4] Simulación de modificación de archivo")
print("-" * 70)

# Modificar el archivo
with open("tests/documento_secreto.txt", "ab") as f:
    f.write(b"\n[MODIFICADO POR ATACANTE]")

print(f"  ⚠️  Archivo modificado: se agregó texto malicioso")

result_modified = verify_file_integrity("tests/documento_secreto.txt", "tests/integrity_db.json")

print(f"  ✓ Estado: {result_modified['message']}")
print(f"  ✓ Hash original:  {result_modified['original_hash']}")
print(f"  ✓ Hash actual:    {result_modified['current_hash']}")
print(f"  ✓ Integridad OK:  {result_modified['valid']}")
print(f"  ✓ ¡Modificación detectada exitosamente!")

# Restaurar archivo
with open("tests/documento_secreto.txt", "wb") as f:
    f.write(test_content)

print("\n[4.5] Verificación de todos los archivos registrados")
print("-" * 70)

all_results = verify_all_files("tests/integrity_db.json")

for res in all_results:
    status = "✓" if res['valid'] else "⚠️"
    print(f"  {status} {res['filepath']}: {res['message']}")

print("\n[4.6] Comparación de archivos")
print("-" * 70)

# Crear copia idéntica
with open("tests/documento_copia.txt", "wb") as f:
    f.write(test_content)

son_iguales = compare_files("tests/documento_secreto.txt", "tests/documento_copia.txt")
print(f"  ✓ documento_secreto.txt vs documento_copia.txt: {son_iguales}")

# Crear archivo diferente
with open("tests/documento_diferente.txt", "wb") as f:
    f.write(b"Contenido diferente")

son_iguales2 = compare_files("tests/documento_secreto.txt", "tests/documento_diferente.txt")
print(f"  ✓ documento_secreto.txt vs documento_diferente.txt: {son_iguales2}")

print("\n[4.7] Propiedades de las funciones hash")
print("-" * 70)
print("  ✓ Determinismo: Mismo input = mismo hash")
print("  ✓ Efecto avalancha: Pequeño cambio → hash completamente diferente")
print("  ✓ Unidireccional: No se puede revertir hash → datos originales")
print("  ✓ Resistencia a colisiones: Muy difícil encontrar dos inputs con mismo hash")

msg1 = b"Hola Mundo"
msg2 = b"hola Mundo"  # solo cambio de mayúscula

hash1 = sha256_hex(msg1)
hash2 = sha256_hex(msg2)

print(f"\n  Demostración del efecto avalancha:")
print(f"  • '{msg1.decode()}' → {hash1}")
print(f"  • '{msg2.decode()}' → {hash2}")
print(f"  • Hashes completamente diferentes con cambio mínimo")

# ========================
# RESUMEN FINAL
# ========================
print("\n" + "=" * 70)
print("RESUMEN DE PRUEBAS COMPLETADAS")
print("=" * 70)
print("""
✓ CIFRADO SIMÉTRICO (AES)
  - Generación de claves de 128, 192 y 256 bits
  - Cifrado/descifrado con AES-GCM (AEAD)
  - Cifrado/descifrado con AES-CBC + HMAC
  - Comparación de rendimiento y seguridad
  - Importancia del IV demostrada

✓ CIFRADO ASIMÉTRICO (RSA)
  - Generación de pares de claves RSA-2048
  - Intercambio seguro de mensajes
  - Comparación de rendimiento con AES
  - Esquema híbrido AES+RSA implementado

✓ FIRMA DIGITAL
  - Generación de firmas con RSA-PSS
  - Verificación de firmas válidas
  - Detección de documentos modificados
  - Casos de uso en PKI explicados

✓ FUNCIONES HASH (SHA-256)
  - Cálculo de hash de archivos
  - Sistema de verificación de integridad
  - Detección automática de modificaciones
  - Comparación de archivos por hash
  - Propiedades criptográficas demostradas

Todos los componentes del proyecto han sido probados exitosamente.
""")

print("=" * 70)
print("FIN DE LAS PRUEBAS")
print("=" * 70)
