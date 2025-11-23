# hybrid.py
from aescipher import generate_aes_key, encrypt_gcm, decrypt_gcm
from rsautils import rsa_encrypt, rsa_decrypt, load_public_key, load_private_key

def encrypt_file_hybrid(plaintext_bytes: bytes, rsa_pub_pem: bytes):
    # 1) generar clave AES
    aes_key = generate_aes_key(256)
    # 2) cifrar con AES-GCM
    nonce, ciphertext, tag = encrypt_gcm(plaintext_bytes, aes_key)
    # 3) cifrar la clave AES con RSA (pub)
    pub = load_public_key(rsa_pub_pem)
    enc_key = rsa_encrypt(aes_key, pub)
    # devolver estructura
    return enc_key, nonce, tag, ciphertext

def decrypt_file_hybrid(enc_key: bytes, nonce: bytes, tag: bytes, ciphertext: bytes, rsa_priv_pem: bytes):
    priv = load_private_key(rsa_priv_pem)
    aes_key = rsa_decrypt(enc_key, priv)
    plaintext = decrypt_gcm(nonce, ciphertext, tag, aes_key)
    return plaintext
