# rsautils.py
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes

# Generar par de claves RSA
def generate_rsa_keypair(bits=2048):
    key = RSA.generate(bits)
    private_pem = key.export_key()
    public_pem = key.publickey().export_key()
    return private_pem, public_pem

def load_private_key(pem_bytes):
    return RSA.import_key(pem_bytes)

def load_public_key(pem_bytes):
    return RSA.import_key(pem_bytes)

# Cifrado con OAEP (solo para mensajes cortos -> usar esquema híbrido para archivos)
def rsa_encrypt(message: bytes, public_key):
    cipher = PKCS1_OAEP.new(public_key, hashAlgo=SHA256)
    return cipher.encrypt(message)

def rsa_decrypt(ciphertext: bytes, private_key):
    cipher = PKCS1_OAEP.new(private_key, hashAlgo=SHA256)
    return cipher.decrypt(ciphertext)

# Firma con PSS
def sign_message(message: bytes, private_key):
    h = SHA256.new(message)
    signer = pss.new(private_key)
    signature = signer.sign(h)
    return signature

def verify_signature(message: bytes, signature: bytes, public_key):
    h = SHA256.new(message)
    verifier = pss.new(public_key)
    try:
        verifier.verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False
