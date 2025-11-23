# Implementación y Análisis de Algoritmos Criptográficos

Implementación completa y funcional de los principales algoritmos criptográficos modernos utilizados en seguridad informática: AES (cifrado simétrico), RSA (cifrado asimétrico), SHA-256 (funciones hash) y firma digital RSA-PSS. Incluye interfaz gráfica de usuario, análisis comparativo de rendimiento y documentación técnica completa.

---

## Tabla de Contenidos

- [Descripción General](#descripción-general)
- [Características Implementadas](#características-implementadas)
- [Requisitos e Instalación](#requisitos-e-instalación)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Guía de Uso](#guía-de-uso)
- [Fundamentos Teóricos](#fundamentos-teóricos)
- [Análisis de Seguridad](#análisis-de-seguridad)
- [Resultados y Evaluaciones](#resultados-y-evaluaciones)

---

## Descripción General

Este proyecto implementa los principales algoritmos criptográficos modernos utilizados en sistemas de seguridad de la información, con el objetivo de comprender su funcionamiento, evaluar su seguridad y rendimiento, y demostrar su aplicación práctica.

### Objetivos Completados

- Implementación de sistemas de cifrado simétrico y asimétrico
- Sistema completo de firma digital para autenticación e integridad
- Verificación de integridad de archivos mediante funciones hash
- Esquema híbrido AES+RSA para cifrado eficiente de archivos grandes
- Análisis comparativo de rendimiento y seguridad
- Interfaz gráfica de usuario para todas las funcionalidades

---

## Características Implementadas

### 1. Cifrado Simétrico (AES)

**Generación de claves**
- Soporte para claves de 128, 192 y 256 bits

**Modos de operación**
- AES-GCM: Modo autenticado (AEAD - Authenticated Encryption with Associated Data)
- AES-CBC: Modo tradicional con HMAC-SHA256 para integridad

**Funcionalidades**
- Cifrado y descifrado de texto directo
- Cifrado y descifrado de archivos completos
- Gestión segura de IV (Vector de Inicialización)
- Verificación de integridad automática

### 2. Cifrado Asimétrico (RSA)

- Generación de pares de claves RSA-2048 bits
- Cifrado OAEP (Optimal Asymmetric Encryption Padding) con SHA-256
- Intercambio seguro de mensajes
- Exportación e importación de claves en formato PEM

### 3. Firma Digital

- Algoritmo RSA-PSS (Probabilistic Signature Scheme)
- Hash SHA-256
- Firma de mensajes y texto directo
- Generación y verificación de firmas digitales
- Detección de modificaciones en documentos firmados
- No repudio criptográfico

### 4. Funciones Hash (SHA-256)

- Cálculo de hash de archivos y datos
- Sistema de verificación de integridad con base de datos
- Detección automática de modificaciones
- Comparación de archivos por hash
- Registro y auditoría de cambios

### 5. Esquema Híbrido (AES + RSA)

- RSA para intercambio seguro de claves
- AES-GCM para cifrado de contenido
- Rendimiento de AES para datos grandes
- Seguridad de RSA para distribución de claves

---

## Requisitos e Instalación

### Requisitos

- Python 3.8 o superior
- Biblioteca PyCryptodome

### Instalación

```bash
pip install pycryptodome
```

O usando el archivo de requisitos:

```bash
pip install -r requirements.txt
```

---

## Estructura del Proyecto

```
AlgoritmosCriptograficos/
│
├── crypto_project/
│   ├── gui_app.py                # Interfaz gráfica (Tkinter)
│   ├── aescipher.py              # Cifrado simétrico AES
│   ├── rsautils.py               # Cifrado asimétrico RSA y firma digital
│   ├── hashutils.py              # Funciones hash y verificación de integridad
│   ├── hybrid.py                 # Esquema híbrido AES + RSA
│   ├── demo_interactiva.py       # Demostración interactiva
│   │
│   └── tests/
│       ├── run_test.py           # Pruebas básicas
│       ├── comprehensive_tests.py # Pruebas completas
│       └── sample.txt            # Archivo de prueba
│
├── README.md                     # Este archivo
├── GUIA_RAPIDA.md               # Guía de inicio rápido
├── GUIA_GUI.md                  # Guía de la interfaz gráfica
└── INFORME_ACADEMICO.md        # Informe académico completo
```

---

## Guía de Uso

### Interfaz Gráfica

```bash
cd crypto_project
python gui_app.py
```

La interfaz incluye 5 pestañas:
- Pestaña AES: Cifrado/descifrado con diferentes tamaños de clave
- Pestaña RSA: Generación y gestión de claves públicas/privadas
- Pestaña Firma Digital: Firmar y verificar documentos
- Pestaña Integridad: Sistema de verificación SHA-256
- Pestaña Híbrido: Cifrado eficiente de archivos grandes

### Pruebas del Sistema

**Pruebas básicas:**
```bash
cd crypto_project
python tests/run_test.py
```

**Pruebas comprehensivas:**
```bash
python tests/comprehensive_tests.py
```

### Uso Programático

**Ejemplo: Cifrado AES**
```python
from aescipher import generate_aes_key, encrypt_file_gcm, decrypt_file_gcm

key = generate_aes_key(256)
encrypt_file_gcm("documento.txt", "documento.enc", key)
decrypt_file_gcm("documento.enc", "documento_recuperado.txt", key)
```

**Ejemplo: Firma Digital**
```python
from rsautils import generate_rsa_keypair, sign_message, verify_signature
from rsautils import load_private_key, load_public_key

priv_pem, pub_pem = generate_rsa_keypair(2048)
priv_key = load_private_key(priv_pem)
pub_key = load_public_key(pub_pem)

documento = b"Contrato importante"
firma = sign_message(documento, priv_key)
es_valida = verify_signature(documento, firma, pub_key)
```

---

## Fundamentos Teóricos

### Criptografía Simétrica (AES)

Advanced Encryption Standard (AES) es el estándar de cifrado simétrico más utilizado actualmente.

**Características principales:**
- Utiliza la misma clave para cifrar y descifrar
- Extremadamente rápido para grandes volúmenes de datos
- Tamaños de clave: 128, 192, 256 bits
- Algoritmo de cifrado por bloques de 128 bits

**Modos de operación:**

AES-GCM (Galois/Counter Mode)
- Modo autenticado que proporciona confidencialidad e integridad simultáneamente
- No requiere padding
- Utilizado en TLS 1.3 e IPSec
- Recomendado para nuevas implementaciones

AES-CBC (Cipher Block Chaining)
- Modo tradicional que requiere padding
- Necesita HMAC adicional para garantizar integridad
- Vulnerable a ataques de padding oracle si no se implementa correctamente

**Vector de Inicialización (IV):**
- Debe ser único para cada operación de cifrado
- Asegura que el mismo texto plano produzca diferentes textos cifrados
- Previene ataques de análisis de patrones
- No necesita ser secreto, pero nunca debe reutilizarse con la misma clave

### Criptografía Asimétrica (RSA)

RSA es el algoritmo de clave pública más ampliamente utilizado en la industria.

**Características principales:**
- Par de claves: pública (cifrar/verificar) y privada (descifrar/firmar)
- Seguridad basada en la dificultad de factorizar números grandes
- Tamaño mínimo recomendado: 2048 bits
- Aproximadamente 1000 veces más lento que AES

**Aplicaciones principales:**
- Intercambio de claves (como en TLS)
- Firma digital
- Autenticación

**OAEP (Optimal Asymmetric Encryption Padding):**
- Esquema de padding que proporciona seguridad semántica
- Protege contra ataques de texto cifrado elegido
- Integra función hash (SHA-256) para robustez adicional

**Limitaciones:**
- Solo puede cifrar datos menores que el tamaño de la clave (~190 bytes para RSA-2048)
- Solución: Esquema híbrido (cifrar clave AES con RSA)

### Firma Digital

La firma digital proporciona tres garantías fundamentales:

1. **Autenticación:** Verifica la identidad del firmante
2. **Integridad:** Detecta cualquier modificación del documento
3. **No repudio:** El firmante no puede negar haber firmado

**Proceso de firma:**
1. Se calcula el hash del documento (SHA-256)
2. El hash se cifra con la clave privada del firmante
3. Para verificar: se calcula el hash del documento recibido, se descifra la firma con la clave pública, y se comparan ambos hashes

**RSA-PSS (Probabilistic Signature Scheme):**
- Esquema moderno de firma con RSA
- Utiliza padding aleatorio (mayor seguridad que PKCS#1 v1.5)
- Resistente a ataques de falsificación existencial

**Aplicaciones:**
- Certificados digitales (X.509)
- Infraestructura de Clave Pública (PKI)
- Código firmado (software, actualizaciones)
- Correos electrónicos seguros (S/MIME, PGP)
- Transacciones electrónicas

### Funciones Hash Criptográficas (SHA-256)

SHA-256 (Secure Hash Algorithm 256-bit) forma parte de la familia SHA-2.

**Propiedades esenciales:**

1. **Determinismo:** El mismo input siempre produce el mismo hash
2. **Unidireccional:** Imposible revertir hash a datos originales
3. **Resistencia a colisiones:** Prácticamente imposible encontrar dos inputs diferentes con el mismo hash
4. **Efecto avalancha:** Cambio mínimo en input produce hash completamente diferente
5. **Eficiencia:** Cálculo rápido y eficiente

**Especificaciones:**
- Salida: 256 bits (32 bytes)
- Representación hexadecimal: 64 caracteres

**Aplicaciones:**
- Verificación de integridad de archivos
- Almacenamiento seguro de contraseñas
- Firmas digitales
- Blockchain y criptomonedas
- Certificados SSL/TLS

### Esquema Híbrido (AES + RSA)

**Problema:** RSA es lento y tiene limitaciones de tamaño
**Solución:** Combinar las ventajas de ambos algoritmos

**Proceso de cifrado:**
1. Generar clave AES aleatoria (256 bits)
2. Cifrar el contenido con AES-GCM
3. Cifrar la clave AES con RSA usando la clave pública del receptor
4. Transmitir: clave AES cifrada + contenido cifrado

**Proceso de descifrado:**
1. Descifrar la clave AES con RSA usando la clave privada
2. Usar la clave AES para descifrar el contenido

**Ventajas:**
- Rendimiento de AES para datos grandes
- Seguridad del intercambio de claves de RSA
- No requiere canal seguro previo
- Utilizado en protocolos reales (TLS, PGP, S/MIME)

**Ejemplo en TLS (HTTPS):**
1. Cliente y servidor negocian usando RSA/ECDHE
2. Establecen clave AES compartida
3. Toda la comunicación se cifra con AES

---

## Análisis de Seguridad

### Vulnerabilidades de Algoritmos Obsoletos

**DES (Data Encryption Standard)**

Estado: Completamente inseguro, no utilizar

Problemas:
- Clave de solo 56 bits
- Puede romperse por fuerza bruta en horas
- Vulnerable a criptoanálisis diferencial y lineal

Reemplazo: AES

**3DES (Triple DES)**

Estado: Deprecado, no usar para nuevos sistemas

Problemas:
- Lento (3 veces más que DES)
- Bloques de 64 bits (vulnerable a ataques de colisión)
- Oficialmente deprecado por NIST en 2023
- Clave efectiva de solo 112 bits

Reemplazo: AES-128 o superior

**MD5 y SHA-1**

Estado: No utilizar para aplicaciones de seguridad

MD5:
- Colisiones encontradas en 2004
- Puede generar certificados SSL falsos
- Solo uso aceptable: checksums no criptográficos

SHA-1:
- Colisiones prácticas demostradas en 2017
- Deprecado por navegadores y autoridades certificadoras

Reemplazo: SHA-256 o SHA-3

### Ataques Conocidos y Mitigaciones

**Ataque de Padding Oracle (CBC)**
- Descripción: Explota mensajes de error de padding
- Mitigación: Usar AES-GCM, timing constante, no revelar errores específicos

**Reutilización de IV**
- Descripción: Usar el mismo IV con la misma clave
- Consecuencia: Permite XOR de plaintexts, revelando información
- Mitigación: Generar IV aleatorio para cada cifrado

**Ataque de Replay**
- Descripción: Retransmitir mensajes cifrados válidos
- Mitigación: Incluir timestamp, nonce o contador de secuencia

**Ataque de Texto Cifrado Elegido (RSA)**
- Mitigación: Usar OAEP en lugar de PKCS#1 v1.5

**Ataque de Timing**
- Descripción: Medir tiempo de operaciones para obtener información
- Mitigación: Implementaciones en tiempo constante

**Ataque de Colisión (Hash)**
- Descripción: Encontrar dos inputs con el mismo hash
- Mitigación: Usar SHA-256 o superior

---

## Resultados y Evaluaciones

### Comparación de Rendimiento

**Tamaños de clave AES (archivo de 100 KB)**

| Tamaño  | Cifrado | Descifrado | Nivel de Seguridad |
|---------|---------|------------|-------------------|
| AES-128 | ~2 ms   | ~2 ms      | Seguro hasta 2030+ |
| AES-192 | ~2.3 ms | ~2.3 ms    | Altamente seguro |
| AES-256 | ~2.6 ms | ~2.6 ms    | Máxima seguridad |

Conclusión: AES-256 tiene overhead mínimo (<30%) con máxima seguridad.

**Modos de operación AES**

| Modo | Cifrado | Integridad | Velocidad | Recomendación |
|------|---------|------------|-----------|---------------|
| GCM  | Sí      | Integrada  | Rápido    | Recomendado (TLS 1.3) |
| CBC  | Sí      | Requiere HMAC | Rápido | Legacy, evitar |
| CTR  | Sí      | Requiere HMAC | Muy rápido | Con HMAC separado |

Conclusión: GCM es superior por proporcionar AEAD en una sola operación.

**Comparación simétrico vs asimétrico**

| Operación | AES-256 | RSA-2048 | Diferencia |
|-----------|---------|----------|------------|
| Cifrado (1 KB) | ~0.1 ms | ~5 ms | 50x más lento |
| Descifrado (1 KB) | ~0.1 ms | ~50 ms | 500x más lento |
| Generación de clave | <1 ms | ~300 ms | 300x más lento |

Conclusión: RSA es significativamente más lento, justificando el esquema híbrido.

### Evaluación de Seguridad

**Fortaleza de claves**

| Algoritmo | Tamaño | Equivalencia Simétrica | Estado de Seguridad |
|-----------|--------|------------------------|---------------------|
| AES | 128 bits | 128 bits | Seguro |
| AES | 256 bits | 256 bits | Máximo |
| RSA | 2048 bits | ~112 bits | Seguro hasta 2030 |
| RSA | 3072 bits | ~128 bits | Seguro a largo plazo |
| RSA | 4096 bits | ~152 bits | Máxima seguridad |

**Resistencia a ataques**

AES-256:
- Ataques de fuerza bruta: 2^256 operaciones (prácticamente imposible)
- Criptoanálisis: Máximo 4 rondas comprometidas de 14 totales
- Ataques cuánticos: 2^128 con algoritmo de Grover (aún seguro)

RSA-2048:
- Factorización clásica: >10^9 años con tecnología actual
- Factorización cuántica: Vulnerable a algoritmo de Shor
- Recomendación: Considerar migración a criptografía post-cuántica

SHA-256:
- Colisiones: 2^128 operaciones (seguro)
- Preimagen: 2^256 operaciones (prácticamente imposible)
- Resistente a ataques cuánticos conocidos

---

## Información del Proyecto

**Autores:** Maryori Lasso - Jean Esguerra - Juan Plata
**Repositorio:** https://github.com/maryorilasso/AlgoritmosCriptograficos

