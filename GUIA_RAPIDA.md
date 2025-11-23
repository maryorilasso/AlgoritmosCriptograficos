# 🎯 GUÍA DE USO RÁPIDO - Proyecto de Criptografía

## 📦 Instalación Rápida

```bash
# 1. Instalar dependencias
pip install pycryptodome

# 2. Navegar al directorio del proyecto
cd crypto_project
```

## 🚀 Ejecución de Pruebas

### Opción 1: Interfaz Gráfica (⭐ Recomendado)
```bash
python gui_app.py
```
**Interfaz moderna con:**
- 🔒 Cifrado/descifrado AES con diferentes tamaños de clave
- 🔑 Generación y gestión de claves RSA
- ✍️ Firma digital y verificación
- 🔍 Sistema de verificación de integridad
- 🔐 Esquema híbrido AES+RSA
- 📊 Logs en tiempo real de todas las operaciones

### Opción 2: Pruebas Comprehensivas
```bash
python tests/comprehensive_tests.py
```
**Incluye:**
- ✅ Comparación de tamaños de clave AES
- ✅ Evaluación GCM vs CBC
- ✅ Análisis de rendimiento
- ✅ Demostración de firmas digitales
- ✅ Sistema de verificación de integridad
- ✅ Casos de fallo y seguridad

### Opción 3: Demo Interactiva (Terminal)
```bash
python demo_interactiva.py
```
**Menú con opciones:**
1. Cifrado Simétrico (AES)
2. Cifrado Asimétrico (RSA)
3. Firma Digital
4. Verificación de Integridad
5. Esquema Híbrido
6. Ejecutar todas las demos

### Opción 4: Pruebas Básicas (Rápido)
```bash
python tests/run_test.py
```

## 💻 Ejemplos de Código

### Cifrar TEXTO directo con AES ⭐ NUEVO
```python
from aescipher import generate_aes_key, encrypt_gcm, decrypt_gcm

# Generar clave
key = generate_aes_key(256)

# Cifrar texto
mensaje = b"Mensaje secreto"
nonce, ciphertext, tag = encrypt_gcm(mensaje, key)

# Descifrar
mensaje_recuperado = decrypt_gcm(nonce, ciphertext, tag, key)
print(mensaje_recuperado)  # b"Mensaje secreto"
```

### Cifrar un archivo con AES
```python
from aescipher import generate_aes_key, encrypt_file_gcm, decrypt_file_gcm

# Generar clave
key = generate_aes_key(256)

# Cifrar
encrypt_file_gcm("documento.txt", "documento.enc", key)

# Descifrar
decrypt_file_gcm("documento.enc", "documento_recuperado.txt", key)
```

### Firmar un documento
```python
from rsautils import generate_rsa_keypair, sign_message, verify_signature
from rsautils import load_private_key, load_public_key

# Generar claves
priv_pem, pub_pem = generate_rsa_keypair(2048)
priv_key = load_private_key(priv_pem)
pub_key = load_public_key(pub_pem)

# Firmar
documento = b"Contrato importante"
firma = sign_message(documento, priv_key)

# Verificar
es_valida = verify_signature(documento, firma, pub_key)
print(f"Firma válida: {es_valida}")
```

### Verificar integridad de archivos
```python
from hashutils import register_file, verify_file_integrity

# Registrar archivo
register_file("documento.txt")

# Verificar integridad
result = verify_file_integrity("documento.txt")
print(result['message'])
```

## 📁 Estructura de Archivos

```
crypto_project/
├── gui_app.py                # ⭐ INTERFAZ GRÁFICA
├── aescipher.py              # Cifrado AES (GCM, CBC)
├── rsautils.py               # RSA y firma digital
├── hashutils.py              # SHA-256 y verificación de integridad
├── hybrid.py                 # Esquema híbrido AES+RSA
├── demo_interactiva.py       # Demo con menú interactivo
└── tests/
    ├── run_test.py           # Pruebas básicas
    ├── comprehensive_tests.py # Pruebas completas
    └── sample.txt            # Archivo de ejemplo
```

## ✅ Verificación de Instalación

Ejecuta este comando para verificar que todo está instalado:
```bash
python -c "from Crypto.Cipher import AES; print('✓ PyCryptodome instalado correctamente')"
```

## 🎓 Componentes del Proyecto

### ✅ Implementado
- [x] Cifrado simétrico AES (128, 192, 256 bits)
- [x] Cifrado asimétrico RSA (2048+ bits)
- [x] Firma digital RSA-PSS
- [x] Funciones hash SHA-256
- [x] Verificación de integridad de archivos
- [x] Esquema híbrido AES+RSA
- [x] Comparaciones de rendimiento
- [x] Análisis de seguridad
- [x] Detección de modificaciones
- [x] Documentación completa

## 📊 Requisitos del Proyecto Cumplidos

| Requisito | Estado | Archivo |
|-----------|--------|---------|
| Cifrado AES (128, 192, 256) | ✅ | `aescipher.py` |
| Cifrado de archivos | ✅ | `aescipher.py` |
| Modos GCM y CBC | ✅ | `aescipher.py` |
| Generación claves RSA 2048+ | ✅ | `rsautils.py` |
| Intercambio seguro mensajes | ✅ | `comprehensive_tests.py` |
| Comparación simétrico vs asimétrico | ✅ | `comprehensive_tests.py` |
| Firma digital | ✅ | `rsautils.py` |
| Verificación de firmas | ✅ | `rsautils.py` |
| Detección de documentos modificados | ✅ | `comprehensive_tests.py` |
| Hash SHA-256 de archivos | ✅ | `hashutils.py` |
| Sistema de verificación de integridad | ✅ | `hashutils.py` |
| Detección automática de modificaciones | ✅ | `hashutils.py` |
| Análisis de seguridad DES | ✅ | `README.md` |
| Mejores prácticas | ✅ | `README.md` |

## 🔒 Conceptos Clave Implementados

1. **IV (Vector de Inicialización)**: Único por cifrado para prevenir análisis de patrones
2. **AEAD (GCM)**: Autenticación integrada con cifrado
3. **HMAC**: Integridad para modos que no son AEAD
4. **RSA-OAEP**: Padding seguro para cifrado asimétrico
5. **RSA-PSS**: Firma probabilística (más segura que PKCS#1 v1.5)
6. **Esquema Híbrido**: Combinación óptima de AES y RSA
7. **Hash criptográfico**: Verificación de integridad con SHA-256

## 📞 Solución de Problemas

### Error: ModuleNotFoundError: No module named 'Crypto'
```bash
pip install pycryptodome
```

### Error: No module named 'rsautils'
Asegúrate de estar en el directorio `crypto_project`:
```bash
cd crypto_project
python tests/run_test.py
```

### Permisos para crear archivos
Los scripts crean archivos temporales en `tests/`. Asegúrate de tener permisos de escritura.

## 🎯 Próximos Pasos Sugeridos

1. Ejecutar `comprehensive_tests.py` para ver todas las funcionalidades
2. Probar `demo_interactiva.py` para experimentar interactivamente
3. Leer `README.md` para entender los conceptos teóricos
4. Revisar el código fuente para comprender las implementaciones

## 📚 Recursos Adicionales

- **README.md**: Documentación completa con teoría y análisis
- **comprehensive_tests.py**: Ejemplos de todas las funcionalidades
- **demo_interactiva.py**: Experimentación guiada

---

**Autor**: Maryori Lasso - Jean Esguerra - Juan Plata 
**Fecha**: Noviembre 2025  
**Proyecto**: Criptografía - Seguridad Informática
