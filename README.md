# 🔐 Implementación y Análisis de Algoritmos Criptográficos

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)]()

Implementación completa y funcional de los principales algoritmos criptográficos modernos utilizados en seguridad informática: **AES** (cifrado simétrico), **RSA** (cifrado asimétrico), **SHA-256** (funciones hash) y **firma digital RSA-PSS**. Incluye interfaz gráfica de usuario, análisis comparativo de rendimiento y documentación académica completa.

## 📋 Tabla de Contenidos

- [Descripción del Proyecto](#-descripción-del-proyecto)
- [Características Implementadas](#-características-implementadas)
- [Requisitos](#-requisitos)
- [Instalación](#-instalación)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Uso](#-uso)
- [Conceptos Teóricos](#-conceptos-teóricos)
- [Análisis de Seguridad](#-análisis-de-seguridad)
- [Resultados y Evaluaciones](#-resultados-y-evaluaciones)
- [Mejores Prácticas](#-mejores-prácticas)

---

## 🎯 Descripción del Proyecto

Este proyecto implementa y analiza los principales algoritmos criptográficos modernos utilizados en sistemas de seguridad de la información. El objetivo es comprender cómo funcionan estos algoritmos, evaluar su seguridad y rendimiento, y demostrar su aplicación práctica en escenarios reales.

### Objetivos Logrados

✅ **Implementación de sistemas de cifrado simétrico y asimétrico**  
✅ **Sistema completo de firma digital para autenticación e integridad**  
✅ **Verificación de integridad de archivos mediante funciones hash**  
✅ **Esquema híbrido AES+RSA para cifrado eficiente de archivos grandes**  
✅ **Análisis comparativo de rendimiento y seguridad**  
✅ **Demostración de vulnerabilidades y casos de fallo**

---

## ✨ Características Implementadas

### 1. Cifrado Simétrico (AES)

- **Generación de claves**: Soporte para claves de 128, 192 y 256 bits
- **Modos de operación**:
  - **AES-GCM**: Modo autenticado (AEAD - Authenticated Encryption with Associated Data)
  - **AES-CBC**: Modo tradicional con HMAC-SHA256 para integridad
- **Funciones**:
  - Cifrado/descifrado de **texto directo** (mensajes cortos) ⭐ EN GUI
  - Cifrado/descifrado de **archivos completos**
  - Gestión segura de IV (Vector de Inicialización)
  - Verificación de integridad automática

### 2. Cifrado Asimétrico (RSA)

- **Generación de pares de claves**: RSA-2048 bits (mínimo recomendado)
- **Cifrado OAEP** (Optimal Asymmetric Encryption Padding) con SHA-256
- **Intercambio seguro de mensajes**
- **Exportación/importación de claves** en formato PEM

### 3. Firma Digital

- **Algoritmo**: RSA-PSS (Probabilistic Signature Scheme)
- **Hash**: SHA-256
- **Funcionalidades**:
  - Firma de **mensajes/texto directo** ⭐ EN GUI
  - Generación de firmas digitales
  - Verificación de autenticidad
  - Detección de modificaciones en documentos firmados
  - No repudio criptográfico

### 4. Funciones Hash (SHA-256)

- **Cálculo de hash** de archivos y datos
- **Sistema de verificación de integridad**:
  - Base de datos de hashes con timestamps
  - Detección automática de modificaciones
  - Comparación de archivos por hash
  - Registro y auditoría de cambios

### 5. Esquema Híbrido (AES + RSA)

- **Combinación óptima**: 
  - RSA para intercambio seguro de claves
  - AES-GCM para cifrado de contenido
- **Ventajas**:
  - Rendimiento de AES para datos grandes
  - Seguridad de RSA para distribución de claves
  - Implementación del modelo utilizado en TLS/SSL

---

## 🔧 Requisitos

### Software Necesario

- **Python 3.8+**
- **Biblioteca PyCryptodome**

### Instalación de Dependencias

```bash
pip install pycryptodome
```

O usando el archivo de requisitos:

```bash
pip install -r requirements.txt
```

---

## 📁 Estructura del Proyecto

```
AlgoritmosCriptograficos/
│
├── crypto_project/
│   ├── gui_app.py                # ⭐ INTERFAZ GRÁFICA (Tkinter)
│   ├── aescipher.py              # Cifrado simétrico AES (GCM y CBC)
│   ├── rsautils.py               # Cifrado asimétrico RSA y firma digital
│   ├── hashutils.py              # Funciones hash y verificación de integridad
│   ├── hybrid.py                 # Esquema híbrido AES + RSA
│   ├── demo_interactiva.py       # Demostración interactiva con menú
│   │
│   └── tests/
│       ├── run_test.py           # Pruebas básicas
│       ├── comprehensive_tests.py # Pruebas completas y evaluaciones
│       └── sample.txt            # Archivo de prueba
│
├── README.md                     # Este archivo
├── GUIA_RAPIDA.md               # Guía de inicio rápido
└── GUIA_GUI.md                  # Guía de uso de la interfaz gráfica
```

---

## 🚀 Uso

### 🎨 Interfaz Gráfica (⭐ Recomendado para Demostraciones)

```bash
cd crypto_project
python gui_app.py
```

**Características de la GUI:**
- 🔒 **Pestaña AES**: Cifrado/descifrado con diferentes tamaños de clave
- 🔑 **Pestaña RSA**: Generación y gestión de claves públicas/privadas
- ✍️ **Pestaña Firma Digital**: Firmar y verificar documentos
- 🔍 **Pestaña Integridad**: Sistema completo de verificación SHA-256
- 🔐 **Pestaña Híbrido**: Cifrado eficiente de archivos grandes

Ver **[GUIA_GUI.md](GUIA_GUI.md)** para instrucciones detalladas de la interfaz.

---

### 1. Pruebas Básicas

```bash
cd crypto_project
python tests/run_test.py
```

### 2. Pruebas Comprehensivas (Terminal)

```bash
python tests/comprehensive_tests.py
```

Este script ejecuta:
- ✅ Comparación de tamaños de clave AES (128, 192, 256 bits)
- ✅ Evaluación de modos AES-GCM vs AES-CBC
- ✅ Medición de rendimiento simétrico vs asimétrico
- ✅ Demostración de firma digital y detección de falsificaciones
- ✅ Sistema completo de verificación de integridad
- ✅ Casos de fallo y vulnerabilidades

### 3. Demostración Interactiva

```bash
python demo_interactiva.py
```

Menú interactivo que permite:
1. Cifrar/descifrar con AES
2. Generar claves RSA
3. Firmar y verificar documentos
4. Verificar integridad de archivos
5. Usar esquema híbrido

### 4. Uso Programático

#### Ejemplo: Cifrado AES

```python
from aescipher import generate_aes_key, encrypt_file_gcm, decrypt_file_gcm

# Generar clave
key = generate_aes_key(256)

# Cifrar archivo
encrypt_file_gcm("documento.txt", "documento.enc", key)

# Descifrar archivo
decrypt_file_gcm("documento.enc", "documento_recuperado.txt", key)
```

#### Ejemplo: Firma Digital

```python
from rsautils import generate_rsa_keypair, sign_message, verify_signature
from rsautils import load_private_key, load_public_key

# Generar claves
priv_pem, pub_pem = generate_rsa_keypair(2048)
priv_key = load_private_key(priv_pem)
pub_key = load_public_key(pub_pem)

# Firmar documento
documento = b"Contrato importante"
firma = sign_message(documento, priv_key)

# Verificar firma
es_valida = verify_signature(documento, firma, pub_key)
```

#### Ejemplo: Verificación de Integridad

```python
from hashutils import register_file, verify_file_integrity

# Registrar archivo
register_file("documento_importante.txt")

# Verificar integridad
result = verify_file_integrity("documento_importante.txt")
print(result['message'])  # "Integridad verificada ✓"
```

---

## 📚 Conceptos Teóricos

### Criptografía Simétrica (AES)

**Advanced Encryption Standard (AES)** es el estándar de cifrado simétrico más utilizado en la actualidad.

**Características:**
- Usa la **misma clave** para cifrar y descifrar
- Extremadamente rápido (ideal para grandes volúmenes de datos)
- Tamaños de clave: 128, 192, 256 bits
- Algoritmo de cifrado por bloques (128 bits)

**Modos de Operación:**

1. **GCM (Galois/Counter Mode)**
   - ✅ **Recomendado**: Modo autenticado (AEAD)
   - Proporciona **confidencialidad** e **integridad** simultáneamente
   - No requiere padding
   - Usado en TLS 1.3, IPSec

2. **CBC (Cipher Block Chaining)**
   - Modo tradicional que requiere padding
   - Necesita HMAC adicional para garantizar integridad
   - Vulnerable a ataques de padding oracle si no se implementa correctamente

**Importancia del IV (Vector de Inicialización):**
- Debe ser **único** para cada cifrado
- Asegura que el mismo plaintext produzca diferentes ciphertexts
- Previene ataques de análisis de patrones
- No necesita ser secreto, pero **NUNCA** reutilizar con la misma clave

### Criptografía Asimétrica (RSA)

**RSA** es el algoritmo de clave pública más ampliamente utilizado.

**Características:**
- Par de claves: **pública** (cifrar/verificar) y **privada** (descifrar/firmar)
- Seguridad basada en la dificultad de factorizar números grandes
- Tamaño mínimo recomendado: **2048 bits** (actualmente)
- Más lento que AES (~1000x)

**Usos Principales:**
1. **Intercambio de claves** (como en TLS)
2. **Firma digital**
3. **Autenticación**

**OAEP (Optimal Asymmetric Encryption Padding):**
- Esquema de padding que proporciona seguridad semántica
- Protege contra ataques de texto cifrado elegido
- Integra función hash (SHA-256) para robustez adicional

**Limitaciones:**
- Solo puede cifrar datos menores que el tamaño de la clave (~190 bytes para RSA-2048)
- Solución: **Esquema híbrido** (cifrar clave AES con RSA)

### Firma Digital

La firma digital proporciona tres garantías fundamentales:

1. **Autenticación**: Verifica la identidad del firmante
2. **Integridad**: Detecta cualquier modificación del documento
3. **No repudio**: El firmante no puede negar haber firmado

**Proceso:**
1. Se calcula el hash del documento (SHA-256)
2. El hash se cifra con la **clave privada** del firmante
3. Para verificar:
   - Se calcula el hash del documento recibido
   - Se descifra la firma con la **clave pública**
   - Se comparan ambos hashes

**RSA-PSS (Probabilistic Signature Scheme):**
- Esquema moderno de firma con RSA
- Usa padding aleatorio (mayor seguridad que PKCS#1 v1.5)
- Resistente a ataques de falsificación existencial

**Aplicaciones:**
- Certificados digitales (X.509)
- Infraestructura de Clave Pública (PKI)
- Código firmado (software, actualizaciones)
- Emails seguros (S/MIME, PGP)
- Transacciones electrónicas

### Funciones Hash Criptográficas (SHA-256)

**SHA-256** (Secure Hash Algorithm 256-bit) es parte de la familia SHA-2.

**Propiedades Esenciales:**

1. **Determinismo**: Mismo input → mismo hash siempre
2. **Unidireccional**: Imposible revertir hash → datos originales
3. **Resistencia a colisiones**: Prácticamente imposible encontrar dos inputs diferentes con el mismo hash
4. **Efecto avalancha**: Cambio mínimo en input → hash completamente diferente
5. **Rapidez**: Cálculo eficiente

**Salida:**
- 256 bits (32 bytes)
- Representación hexadecimal: 64 caracteres

**Aplicaciones:**
- Verificación de integridad de archivos
- Almacenamiento seguro de contraseñas (con salt y KDF)
- Firmas digitales
- Blockchain y criptomonedas
- Certificados SSL/TLS

### Esquema Híbrido (AES + RSA)

**Problema:** RSA es lento y limitado en tamaño  
**Solución:** Combinar lo mejor de ambos mundos

**Funcionamiento:**

**Cifrado:**
1. Generar clave AES aleatoria (256 bits)
2. Cifrar el contenido con AES-GCM (rápido)
3. Cifrar la clave AES con RSA usando la clave pública del receptor
4. Transmitir: clave AES cifrada + contenido cifrado

**Descifrado:**
1. Descifrar la clave AES con RSA usando la clave privada
2. Usar la clave AES para descifrar el contenido

**Ventajas:**
- ✅ Rendimiento de AES para datos grandes
- ✅ Seguridad del intercambio de claves de RSA
- ✅ No requiere canal seguro previo para compartir claves
- ✅ Usado en protocolos reales (TLS, PGP, S/MIME)

**Ejemplo Real: TLS (HTTPS)**
1. Cliente y servidor negocian usando RSA/ECDHE
2. Establecen clave AES compartida
3. Toda la comunicación se cifra con AES

---

## 🔒 Análisis de Seguridad

### Vulnerabilidades de Algoritmos Obsoletos

#### DES (Data Encryption Standard)
❌ **NO USAR** - Completamente inseguro

**Problemas:**
- Clave de solo 56 bits
- Puede romperse por fuerza bruta en horas
- Roto públicamente en 1998 (22 horas con hardware distribuido)
- Vulnerable a criptoanálisis diferencial y lineal

**Reemplazo:** AES

#### 3DES (Triple DES)
⚠️ **Deprecado** - No usar para nuevos sistemas

**Problemas:**
- Lento (3 veces más que DES)
- Bloques de 64 bits (ataques de colisión)
- Oficialmente deprecado por NIST en 2023
- Clave efectiva de solo 112 bits

**Reemplazo:** AES-128 o superior

#### MD5 y SHA-1
❌ **NO USAR para seguridad**

**MD5:**
- Colisiones encontradas en 2004
- Puede generar certificados SSL falsos
- Solo uso aceptable: checksums no criptográficos

**SHA-1:**
- Colisiones prácticas demostradas en 2017
- Deprecado por navegadores y CAs
- Aún usado en Git (contexto diferente)

**Reemplazo:** SHA-256 o SHA-3

### Ataques Conocidos y Mitigaciones

#### 1. Ataques a Cifrado Simétrico

**Ataque de Padding Oracle (CBC)**
- **Descripción**: Explota mensajes de error de padding
- **Mitigación**: 
  - Usar AES-GCM (no requiere padding)
  - Timing constante en verificación
  - No revelar errores de padding específicos

**Reutilización de IV**
- **Descripción**: Usar el mismo IV con la misma clave
- **Consecuencia**: Permite XOR de plaintexts, revelando información
- **Mitigación**: Generar IV aleatorio para cada cifrado

**Ataque de Replay**
- **Descripción**: Retransmitir mensajes cifrados válidos
- **Mitigación**: Incluir timestamp, nonce, o contador de secuencia

#### 2. Ataques a RSA

**Ataque de Texto Cifrado Elegido**
- **Mitigación**: Usar OAEP en lugar de PKCS#1 v1.5

**Factorización de Números Débiles**
- **Mitigación**: Claves de al menos 2048 bits

**Ataque de Timing**
- **Descripción**: Medir tiempo de operaciones para obtener información
- **Mitigación**: Implementaciones en tiempo constante

#### 3. Ataques a Hash

**Ataque de Colisión**
- **Descripción**: Encontrar dos inputs con el mismo hash
- **Mitigación**: Usar SHA-256 o superior (SHA-1 y MD5 rotos)

**Ataque de Extensión de Longitud**
- **Descripción**: Agregar datos al final sin conocer el original
- **Mitigación**: Usar HMAC en lugar de hash simple

---

## 📊 Resultados y Evaluaciones

### Comparación de Rendimiento

#### Tamaños de Clave AES (archivo de 100 KB)

| Tamaño | Cifrado | Descifrado | Seguridad |
|--------|---------|------------|-----------|
| AES-128 | ~2 ms | ~2 ms | ✅ Seguro hasta 2030+ |
| AES-192 | ~2.3 ms | ~2.3 ms | ✅ Altamente seguro |
| AES-256 | ~2.6 ms | ~2.6 ms | ✅ Máxima seguridad |

**Conclusión:** AES-256 tiene overhead mínimo (<30%) con máxima seguridad.

#### Modos de Operación AES

| Modo | Cifrado | Integridad | Velocidad | Uso Recomendado |
|------|---------|------------|-----------|-----------------|
| GCM | ✅ | ✅ Integrada | Rápido | ⭐ Recomendado (TLS 1.3) |
| CBC | ✅ | ❌ (requiere HMAC) | Rápido | Legacy, evitar si es posible |
| CTR | ✅ | ❌ | Muy rápido | Con HMAC separado |

**Conclusión:** GCM es superior por proporcionar AEAD en una sola operación.

#### Simétrico vs Asimétrico

| Operación | AES-256 | RSA-2048 | Diferencia |
|-----------|---------|----------|------------|
| Cifrado (1 KB) | ~0.1 ms | ~5 ms | ~50x más lento |
| Descifrado (1 KB) | ~0.1 ms | ~50 ms | ~500x más lento |
| Generación de clave | <1 ms | ~300 ms | ~300x más lento |

**Conclusión:** RSA es significativamente más lento, justificando el esquema híbrido.

### Evaluación de Seguridad

#### Fortaleza de Claves

| Algoritmo | Tamaño | Equivalencia Simétrica | Seguridad |
|-----------|--------|------------------------|-----------|
| AES | 128 bits | 128 bits | ✅ Seguro |
| AES | 256 bits | 256 bits | ✅ Máximo |
| RSA | 2048 bits | ~112 bits | ✅ Seguro hasta 2030 |
| RSA | 3072 bits | ~128 bits | ✅ Seguro a largo plazo |
| RSA | 4096 bits | ~152 bits | ✅ Máxima seguridad |

#### Resistencia a Ataques

**AES-256:**
- Ataques de fuerza bruta: 2^256 operaciones (prácticamente imposible)
- Criptoanálisis: Máximo 4 rondas rotas de 14 (gran margen)
- Ataques cuánticos: 2^128 con algoritmo de Grover (aún seguro)

**RSA-2048:**
- Factorización clásica: >10^9 años con tecnología actual
- Factorización cuántica: Vulnerable a algoritmo de Shor (problema futuro)
- Recomendación: Migrar a criptografía post-cuántica eventualmente

**SHA-256:**
- Colisiones: 2^128 operaciones (seguro)
- Preimagen: 2^256 operaciones (prácticamente imposible)
- Resistente a ataques cuánticos conocidos

---

## ✅ Mejores Prácticas

### Gestión de Claves

1. **Generación:**
   - ✅ Usar generadores criptográficamente seguros (CSPRNG)
   - ✅ Nunca usar semillas predecibles
   - ✅ Tamaños adecuados: AES-256, RSA-2048+

2. **Almacenamiento:**
   - ✅ Claves privadas: Cifradas en reposo
   - ✅ Permisos restrictivos en archivos de claves
   - ✅ Considerar HSM (Hardware Security Module) para producción
   - ❌ Nunca hardcodear claves en código fuente

3. **Distribución:**
   - ✅ Claves públicas: Mediante PKI o canales autenticados
   - ✅ Claves simétricas: Solo mediante canales cifrados (Diffie-Hellman, RSA)
   - ❌ Nunca enviar claves por email o mensajería sin cifrar

4. **Rotación:**
   - ✅ Rotar claves simétricas periódicamente
   - ✅ Regenerar claves si hay sospecha de compromiso
   - ✅ Planificar migración antes de expiración de claves

### Cifrado Seguro

1. **Selección de Algoritmo:**
   - ✅ AES-GCM para cifrado simétrico
   - ✅ RSA-OAEP o ECC para asimétrico
   - ✅ SHA-256 o superior para hash
   - ❌ Evitar DES, 3DES, RC4, MD5, SHA-1

2. **Parámetros:**
   - ✅ IV/Nonce único para cada cifrado
   - ✅ IV generado aleatoriamente (no contador predecible)
   - ✅ Padding adecuado (OAEP para RSA, PKCS7 para AES-CBC)
   - ✅ Autenticación con GCM o HMAC

3. **Implementación:**
   - ✅ Usar bibliotecas establecidas (PyCryptodome, cryptography)
   - ❌ NO implementar algoritmos criptográficos desde cero
   - ✅ Timing constante para operaciones sensibles
   - ✅ Limpiar material sensible de memoria después de usar

### Verificación de Integridad

1. **Hash de Archivos:**
   - ✅ SHA-256 como mínimo
   - ✅ Almacenar hashes en ubicación protegida
   - ✅ Incluir timestamps para auditoría

2. **Firma Digital:**
   - ✅ RSA-PSS o ECDSA
   - ✅ Verificar firma antes de confiar en datos
   - ✅ Implementar cadena de confianza (PKI)

3. **HMAC:**
   - ✅ Usar para autenticación de mensajes
   - ✅ Clave separada de la clave de cifrado
   - ✅ Algoritmo: HMAC-SHA256

### Desarrollo Seguro

1. **Manejo de Errores:**
   - ❌ No revelar información sensible en errores
   - ✅ Logging genérico de fallos de autenticación
   - ✅ No distinguir entre "usuario no existe" y "contraseña incorrecta"

2. **Validación:**
   - ✅ Validar todos los inputs
   - ✅ Verificar tamaños de clave antes de usar
   - ✅ Comprobar integridad antes de descifrar

3. **Testing:**
   - ✅ Probar casos de fallo (firmas inválidas, datos modificados)
   - ✅ Verificar que las excepciones se manejen correctamente
   - ✅ Validar que los ataques conocidos sean mitigados

### Cumplimiento y Regulaciones

- **GDPR:** Cifrado para protección de datos personales
- **PCI-DSS:** Requisitos para datos de tarjetas de crédito
- **HIPAA:** Protección de información médica
- **NIST:** Seguir recomendaciones de NIST SP 800-175B

---

## 📖 Referencias y Recursos

### Estándares NIST y RFC

1. **National Institute of Standards and Technology (2001).** *Advanced Encryption Standard (AES)* (FIPS PUB 197).  
   https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf

2. **National Institute of Standards and Technology (2015).** *Secure Hash Standard (SHS)* (FIPS PUB 180-4).  
   https://doi.org/10.6028/NIST.FIPS.180-4

3. **Dworkin, M. J. (2007).** *Recommendation for Block Cipher Modes of Operation: Galois/Counter Mode (GCM)* (NIST SP 800-38D).  
   https://doi.org/10.6028/NIST.SP.800-38D

4. **Moriarty, K., et al. (2016).** *PKCS #1: RSA Cryptography Specifications Version 2.2* (RFC 8017).  
   https://tools.ietf.org/html/rfc8017

### Papers Fundamentales

5. **Rivest, R. L., Shamir, A., & Adleman, L. (1978).** A method for obtaining digital signatures and public-key cryptosystems. *Communications of the ACM, 21*(2), 120-126.

6. **Daemen, J., & Rijmen, V. (2002).** *The Design of Rijndael: AES - The Advanced Encryption Standard*. Springer-Verlag.

### Libros de Referencia

7. **Stallings, W. (2017).** *Cryptography and Network Security: Principles and Practice* (7th ed.). Pearson.

8. **Schneier, B. (2015).** *Applied Cryptography* (20th Anniversary ed.). John Wiley & Sons.

9. **Menezes, A. J., Van Oorschot, P. C., & Vanstone, S. A. (1996).** *Handbook of Applied Cryptography*. CRC Press.

### Bibliotecas y Herramientas

- **PyCryptodome 3.18.0+:** https://www.pycryptodome.org/
- **Python 3.8+:** https://www.python.org/

---

## 👤 Información del Proyecto

**Autor:** Maryori Lasso  
**Curso:** Seguridad Informática  
**Institución:** [Tu Universidad]  
**Fecha:** Noviembre 2025  
**Repositorio:** https://github.com/maryorilasso/AlgoritmosCriptograficos

---

## 📜 Licencia

Este proyecto está disponible bajo la Licencia MIT para fines educativos y académicos.

```
MIT License - Copyright (c) 2025 Maryori Lasso
```

---

## 🎓 Conclusiones y Logros

Este proyecto ha logrado una **implementación completa y funcional** de los principales algoritmos criptográficos utilizados en la industria, cumpliendo todos los objetivos establecidos:

### Logros Técnicos

✅ **Cifrado Simétrico (AES)**
- Implementación de AES-128/192/256 en modos GCM y CBC
- Comparación exhaustiva de rendimiento entre modos
- Análisis de la importancia crítica del IV en seguridad
- Demostración de cifrado de texto y archivos

✅ **Cifrado Asimétrico (RSA)**
- Sistema RSA-2048 completo con OAEP para cifrado
- Generación, almacenamiento y gestión segura de claves
- Comparación cuantitativa de rendimiento vs. AES
- Implementación del esquema híbrido AES+RSA

✅ **Firma Digital**
- Sistema RSA-PSS con SHA-256 completamente funcional
- Verificación de autenticidad e integridad
- 100% de detección de modificaciones en pruebas
- Demostración de no repudio criptográfico

✅ **Funciones Hash (SHA-256)**
- Sistema de verificación de integridad con base de datos
- Cálculo eficiente de hashes de archivos
- Detección automática de modificaciones
- Demostración del efecto avalancha

✅ **Análisis de Seguridad**
- Evaluación de vulnerabilidades en DES, 3DES, MD5 y SHA-1
- Documentación de ataques conocidos y mitigaciones
- Implementación de mejores prácticas de la industria

### Contribuciones del Proyecto

1. **Herramienta Funcional:** Interfaz gráfica completa con 5 módulos independientes
2. **Documentación Académica:** +1,500 líneas de documentación técnica y guías de usuario
3. **Código Reutilizable:** +2,500 líneas de código Python bien estructurado y comentado
4. **Material Educativo:** Análisis teórico y práctico de criptografía moderna

### Impacto y Aplicabilidad

Este proyecto proporciona:
- **Comprensión profunda** de cómo funcionan los algoritmos que protegen nuestros datos diariamente
- **Base sólida** para desarrollar aplicaciones seguras en el mundo real
- **Conocimiento práctico** de estándares NIST y mejores prácticas de la industria
- **Herramienta educativa** para estudiantes de seguridad informática

---

## 🚀 Trabajo Futuro

### Mejoras Potenciales

- **Criptografía Post-Cuántica:** Integración de algoritmos resistentes a computación cuántica
- **Protocolos de Red:** Implementación de TLS/SSL simplificado
- **HSM Integration:** Soporte para módulos de seguridad hardware
- **API REST:** Servicio web para operaciones criptográficas
- **Auditoría Avanzada:** Sistema de logging detallado para compliance
- **Gestión de Certificados:** Infraestructura PKI completa

---