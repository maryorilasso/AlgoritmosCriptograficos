# aescipher.py
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import HMAC, SHA256
import os

# --- Utilidades ---
def generate_aes_key(key_size_bits=256):
    if key_size_bits not in (128, 192, 256):
        raise ValueError("key_size_bits debe ser 128, 192 o 256")
    return get_random_bytes(key_size_bits // 8)

# --- AES-GCM (recomendado: cifrado + integridad) ---
def encrypt_gcm(plaintext: bytes, key: bytes):
    nonce = get_random_bytes(12)  # 96-bit recommended
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    # devolver nonce, tag y ciphertext juntos
    return nonce, ciphertext, tag

def decrypt_gcm(nonce: bytes, ciphertext: bytes, tag: bytes, key: bytes):
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext

# --- AES-CBC (ejemplo). Requiere padding y HMAC para integridad ---
from Crypto.Util.Padding import pad, unpad
def encrypt_cbc(plaintext: bytes, key: bytes):
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct = cipher.encrypt(pad(plaintext, AES.block_size))
    return iv, ct

def decrypt_cbc(iv: bytes, ciphertext: bytes, key: bytes):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return pt

# --- Ejemplo de HMAC (si usas CBC) ---
def compute_hmac(data: bytes, mac_key: bytes):
    h = HMAC.new(mac_key, digestmod=SHA256)
    h.update(data)
    return h.digest()

def verify_hmac(data: bytes, mac: bytes, mac_key: bytes):
    h = HMAC.new(mac_key, digestmod=SHA256)
    h.update(data)
    try:
        h.verify(mac)
        return True
    except ValueError:
        return False

# --- Guardar/leer archivos (ejemplo simple) ---
def save_bytes(path, data: bytes):
    with open(path, "wb") as f:
        f.write(data)

def load_bytes(path):
    with open(path, "rb") as f:
        return f.read()

# ========== CIFRADO/DESCIFRADO DE ARCHIVOS ==========

def encrypt_file_gcm(input_file: str, output_file: str, key: bytes):
    """
    Cifra un archivo completo usando AES-GCM.
    
    Args:
        input_file: Ruta del archivo a cifrar
        output_file: Ruta donde guardar el archivo cifrado
        key: Clave AES (16, 24 o 32 bytes)
    
    Returns:
        tuple: (nonce, tag) necesarios para descifrar
    """
    # Leer archivo
    with open(input_file, 'rb') as f:
        plaintext = f.read()
    
    # Cifrar
    nonce, ciphertext, tag = encrypt_gcm(plaintext, key)
    
    # Guardar: nonce (12) + tag (16) + ciphertext
    with open(output_file, 'wb') as f:
        f.write(nonce)
        f.write(tag)
        f.write(ciphertext)
    
    return nonce, tag

def decrypt_file_gcm(input_file: str, output_file: str, key: bytes):
    """
    Descifra un archivo cifrado con AES-GCM.
    
    Args:
        input_file: Ruta del archivo cifrado
        output_file: Ruta donde guardar el archivo descifrado
        key: Clave AES usada para cifrar
    
    Returns:
        bool: True si el descifrado fue exitoso
    """
    # Leer archivo cifrado
    with open(input_file, 'rb') as f:
        nonce = f.read(12)
        tag = f.read(16)
        ciphertext = f.read()
    
    # Descifrar
    try:
        plaintext = decrypt_gcm(nonce, ciphertext, tag, key)
        
        # Guardar
        with open(output_file, 'wb') as f:
            f.write(plaintext)
        
        return True
    except ValueError:
        print("Error: Autenticación fallida. El archivo fue modificado o la clave es incorrecta.")
        return False

def encrypt_file_cbc(input_file: str, output_file: str, key: bytes, mac_key: bytes = None):
    """
    Cifra un archivo usando AES-CBC con HMAC para integridad.
    
    Args:
        input_file: Ruta del archivo a cifrar
        output_file: Ruta donde guardar el archivo cifrado
        key: Clave AES (16, 24 o 32 bytes)
        mac_key: Clave para HMAC (opcional, se genera si no se proporciona)
    
    Returns:
        tuple: (iv, mac, mac_key) necesarios para descifrar
    """
    if mac_key is None:
        mac_key = get_random_bytes(32)
    
    # Leer archivo
    with open(input_file, 'rb') as f:
        plaintext = f.read()
    
    # Cifrar
    iv, ciphertext = encrypt_cbc(plaintext, key)
    
    # Calcular HMAC
    mac = compute_hmac(iv + ciphertext, mac_key)
    
    # Guardar: iv (16) + mac (32) + ciphertext
    with open(output_file, 'wb') as f:
        f.write(iv)
        f.write(mac)
        f.write(ciphertext)
    
    return iv, mac, mac_key

def decrypt_file_cbc(input_file: str, output_file: str, key: bytes, mac_key: bytes):
    """
    Descifra un archivo cifrado con AES-CBC y verifica HMAC.
    
    Args:
        input_file: Ruta del archivo cifrado
        output_file: Ruta donde guardar el archivo descifrado
        key: Clave AES usada para cifrar
        mac_key: Clave HMAC usada
    
    Returns:
        bool: True si el descifrado fue exitoso
    """
    # Leer archivo cifrado
    with open(input_file, 'rb') as f:
        iv = f.read(16)
        mac = f.read(32)
        ciphertext = f.read()
    
    # Verificar HMAC
    if not verify_hmac(iv + ciphertext, mac, mac_key):
        print("Error: HMAC inválido. El archivo fue modificado.")
        return False
    
    # Descifrar
    try:
        plaintext = decrypt_cbc(iv, ciphertext, key)
        
        # Guardar
        with open(output_file, 'wb') as f:
            f.write(plaintext)
        
        return True
    except ValueError as e:
        print(f"Error al descifrar: {e}")
        return False
