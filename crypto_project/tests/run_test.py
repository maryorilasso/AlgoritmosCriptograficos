# ========================
# PRUEBAS DEL PROYECTO
# ========================

import sys
from pathlib import Path

# Agregar el directorio padre al path para importar los módulos
sys.path.insert(0, str(Path(__file__).parent.parent))

print("===== PRUEBA 1: Generar claves RSA =====")
from rsautils import generate_rsa_keypair, load_private_key, load_public_key

priv, pub = generate_rsa_keypair(2048)

with open("priv.pem", "wb") as f:
    f.write(priv)

with open("pub.pem", "wb") as f:
    f.write(pub)

print("Claves RSA generadas y guardadas en priv.pem y pub.pem\n")


# ========================
print("===== PRUEBA 2: Esquema Híbrido AES + RSA =====")
from hybrid import encrypt_file_hybrid, decrypt_file_hybrid

mensaje = b"Este es un texto secreto de prueba"

enc_key, nonce, tag, ct = encrypt_file_hybrid(
    mensaje,
    open("pub.pem", "rb").read()
)

recuperado = decrypt_file_hybrid(
    enc_key, nonce, tag, ct,
    open("priv.pem", "rb").read()
)

print("Mensaje original:", mensaje)
print("Mensaje recuperado:", recuperado)
print("Prueba exitosa:", recuperado == mensaje, "\n")


# ========================
print("===== PRUEBA 3: Firma Digital =====")
from rsautils import sign_message, verify_signature

priv_key = load_private_key(open("priv.pem", "rb").read())
pub_key = load_public_key(open("pub.pem", "rb").read())

msg = b"Documento importante"

firma = sign_message(msg, priv_key)

print("Firma generada:", firma[:20], "...")

ver_ok = verify_signature(msg, firma, pub_key)
print("Verificación correcta:", ver_ok)

# modificar mensaje
ver_fail = verify_signature(msg + b" ", firma, pub_key)
print("Verificación después de modificar:", ver_fail, "\n")


# ========================
print("===== PRUEBA 4: SHA-256 =====")
from hashutils import sha256_hex

hash1 = sha256_hex(b"hola mundo")
print("SHA-256('hola mundo') =", hash1)

hash2 = sha256_hex(b"hola mundo!")
print("SHA-256('hola mundo!') =", hash2)

print("Hashs iguales? :", hash1 == hash2)
