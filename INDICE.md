# 📚 ÍNDICE DE ARCHIVOS DEL PROYECTO

## 🎯 ¿Qué archivo necesito?

### 🚀 Para USAR el Proyecto

| Necesito... | Archivo | Comando |
|------------|---------|---------|
| **Interfaz gráfica** | `gui_app.py` | `python gui_app.py` |
| **Demo interactiva (terminal)** | `demo_interactiva.py` | `python demo_interactiva.py` |
| **Probar todo rápido** | `tests/run_test.py` | `python tests/run_test.py` |
| **Pruebas completas** | `tests/comprehensive_tests.py` | `python tests/comprehensive_tests.py` |

### 📖 Para ENTENDER el Proyecto

| Necesito... | Archivo | Descripción |
|------------|---------|-------------|
| **Documentación completa** | `README.md` | 600+ líneas con teoría, análisis, mejores prácticas |
| **Empezar rápido** | `GUIA_RAPIDA.md` | Comandos principales y ejemplos |
| **Usar la interfaz** | `GUIA_GUI.md` | Manual de uso de la GUI |
| **Cifrar texto directo** | `EJEMPLO_CIFRADO_TEXTO.md` | ⭐ Tutorial paso a paso |
| **Ver la interfaz** | `CAPTURAS_GUI.md` | Visualización ASCII de la GUI |
| **Resumen ejecutivo** | `RESUMEN_PROYECTO.md` | Estado del proyecto, estadísticas |

### 🎤 Para PRESENTAR el Proyecto

| Necesito... | Archivo | Descripción |
|------------|---------|-------------|
| **Guía de presentación** | `GUIA_PRESENTACION.md` | Script detallado paso a paso |
| **Resumen ejecutivo** | `RESUMEN_PROYECTO.md` | Métricas y logros |
| **Demo visual** | `gui_app.py` | Mostrar funcionalidades |

### 💻 Para PROGRAMAR

| Necesito... | Archivo | Funciones Principales |
|------------|---------|---------------------|
| **Cifrado AES** | `crypto_project/aescipher.py` | `generate_aes_key()`, `encrypt_file_gcm()`, `decrypt_file_gcm()` |
| **Cifrado RSA** | `crypto_project/rsautils.py` | `generate_rsa_keypair()`, `rsa_encrypt()`, `rsa_decrypt()` |
| **Firma digital** | `crypto_project/rsautils.py` | `sign_message()`, `verify_signature()` |
| **Hash e integridad** | `crypto_project/hashutils.py` | `calculate_file_hash()`, `verify_file_integrity()` |
| **Híbrido** | `crypto_project/hybrid.py` | `encrypt_file_hybrid()`, `decrypt_file_hybrid()` |

---

## 📁 Estructura Completa

```
AlgoritmosCriptograficos/
│
├── 📖 DOCUMENTACIÓN
│   ├── README.md                   ⭐ Documentación principal (LEER PRIMERO)
│   ├── GUIA_RAPIDA.md             🚀 Inicio rápido
│   ├── GUIA_GUI.md                🎨 Manual de la interfaz
│   ├── GUIA_PRESENTACION.md       🎤 Script para presentar
│   ├── CAPTURAS_GUI.md            📸 Visualización de la GUI
│   ├── RESUMEN_PROYECTO.md        📊 Resumen ejecutivo
│   ├── INDICE.md                  📚 Este archivo
│   └── requirements.txt           📦 Dependencias
│
├── 💻 CÓDIGO FUENTE
│   └── crypto_project/
│       ├── gui_app.py             ⭐ INTERFAZ GRÁFICA (ejecutar esto)
│       ├── demo_interactiva.py    🎮 Demo por terminal
│       ├── aescipher.py           🔒 Cifrado AES
│       ├── rsautils.py            🔑 RSA y firmas
│       ├── hashutils.py           🔍 SHA-256 e integridad
│       ├── hybrid.py              🔐 Esquema híbrido
│       └── tests/
│           ├── run_test.py        ✅ Pruebas básicas
│           ├── comprehensive_tests.py ✅ Pruebas completas
│           └── sample.txt         📄 Archivo de ejemplo
│
└── ⚙️ CONFIGURACIÓN
    └── .gitignore                 🚫 Archivos ignorados por git
```

---

## 🎯 Flujos de Trabajo Comunes

### Escenario 1: "Quiero probar el proyecto rápidamente"
```bash
1. Abrir terminal en crypto_project/
2. python gui_app.py
3. Explorar las 5 pestañas
```

### Escenario 2: "Necesito entender la teoría"
```
1. Abrir README.md
2. Leer secciones:
   - Conceptos Teóricos
   - Análisis de Seguridad
   - Mejores Prácticas
```

### Escenario 3: "Voy a presentar el proyecto"
```
1. Leer GUIA_PRESENTACION.md
2. Practicar con gui_app.py
3. Ejecutar comprehensive_tests.py
4. Revisar RESUMEN_PROYECTO.md
```

### Escenario 4: "Quiero usar esto en mi código"
```python
# Leer GUIA_RAPIDA.md sección "Ejemplos de Código"
from crypto_project.aescipher import generate_aes_key, encrypt_file_gcm

key = generate_aes_key(256)
encrypt_file_gcm("mi_archivo.txt", "mi_archivo.enc", key)
```

### Escenario 5: "Necesito verificar que todo funciona"
```bash
1. python tests/run_test.py          # Pruebas básicas
2. python tests/comprehensive_tests.py # Pruebas completas
3. python gui_app.py                  # Interfaz gráfica
```

---

## 📚 Orden de Lectura Recomendado

### Para Estudiantes (Primera Vez)
1. `GUIA_RAPIDA.md` - Empezar aquí
2. Ejecutar `gui_app.py` - Ver cómo funciona
3. `README.md` sección "Conceptos Teóricos" - Aprender teoría
4. `comprehensive_tests.py` - Ver pruebas
5. `README.md` completo - Profundizar

### Para Profesores/Evaluadores
1. `RESUMEN_PROYECTO.md` - Vista general
2. `README.md` - Documentación técnica
3. `comprehensive_tests.py` - Ver implementación
4. `gui_app.py` - Interfaz de usuario

### Para Presentación
1. `GUIA_PRESENTACION.md` - Script detallado
2. `RESUMEN_PROYECTO.md` - Estadísticas
3. Practicar con `gui_app.py`
4. Tener `README.md` abierto para consultas

---

## 🔍 Búsqueda Rápida

### "¿Cómo hago X?"

| Pregunta | Respuesta |
|----------|-----------|
| Instalar dependencias | `GUIA_RAPIDA.md` - Sección "Instalación" |
| Cifrar un archivo | `GUIA_RAPIDA.md` - Ejemplos de código |
| Generar claves RSA | `GUIA_GUI.md` - Pestaña RSA |
| Firmar un documento | `GUIA_GUI.md` - Pestaña Firma Digital |
| Verificar integridad | `GUIA_GUI.md` - Pestaña Integridad |
| Entender AES vs RSA | `README.md` - Sección "Conceptos Teóricos" |
| Ver rendimiento | Ejecutar `comprehensive_tests.py` |
| Entender vulnerabilidades DES | `README.md` - "Análisis de Seguridad" |

### "¿Dónde está X?"

| Busco... | Ubicación |
|----------|-----------|
| Función para cifrar AES | `crypto_project/aescipher.py` |
| Función para firmar | `crypto_project/rsautils.py` - `sign_message()` |
| Sistema de integridad | `crypto_project/hashutils.py` |
| Interfaz gráfica | `crypto_project/gui_app.py` |
| Pruebas | `crypto_project/tests/` |
| Teoría de SHA-256 | `README.md` - Sección "Funciones Hash" |

---

## ⚡ Comandos Más Usados

```bash
# Directorio base del proyecto
cd AlgoritmosCriptograficos

# Instalar dependencias
pip install -r requirements.txt

# Entrar al directorio de código
cd crypto_project

# Abrir interfaz gráfica (⭐ MÁS USADO)
python gui_app.py

# Demo por terminal
python demo_interactiva.py

# Pruebas completas
python tests/comprehensive_tests.py

# Pruebas básicas
python tests/run_test.py

# Verificar instalación
python -c "from Crypto.Cipher import AES; print('✓ OK')"
```

---

## 📞 Ayuda Rápida

### Errores Comunes

| Error | Solución | Archivo de Ayuda |
|-------|----------|------------------|
| `ModuleNotFoundError: No module named 'Crypto'` | `pip install pycryptodome` | `GUIA_RAPIDA.md` |
| `No module named 'rsautils'` | Ejecutar desde `crypto_project/` | `GUIA_RAPIDA.md` |
| GUI no abre | Tkinter viene con Python | `GUIA_GUI.md` |
| Archivo no encontrado | Usar botón "Seleccionar" | `GUIA_GUI.md` |

---

## ✅ Checklist de Entrega

Antes de entregar, verifica que tienes:

- [ ] `README.md` - Documentación principal
- [ ] `GUIA_RAPIDA.md` - Guía de inicio
- [ ] `GUIA_GUI.md` - Manual de interfaz
- [ ] `GUIA_PRESENTACION.md` - Script de presentación
- [ ] `RESUMEN_PROYECTO.md` - Resumen ejecutivo
- [ ] `requirements.txt` - Dependencias
- [ ] `crypto_project/` - Todo el código fuente
  - [ ] `gui_app.py`
  - [ ] `aescipher.py`
  - [ ] `rsautils.py`
  - [ ] `hashutils.py`
  - [ ] `hybrid.py`
  - [ ] `demo_interactiva.py`
  - [ ] `tests/run_test.py`
  - [ ] `tests/comprehensive_tests.py`

---

## 🎓 Resumen

### Los 3 Archivos Más Importantes

1. **`README.md`** 📖
   - Documentación técnica completa
   - Teoría, análisis, mejores prácticas
   - 600+ líneas

2. **`gui_app.py`** 🎨
   - Interfaz gráfica moderna
   - Todas las funcionalidades en un solo lugar
   - Ideal para demostraciones

3. **`comprehensive_tests.py`** ✅
   - Pruebas completas
   - Comparaciones de rendimiento
   - Casos de uso demostrados

### Para Empezar Ahora

```bash
cd crypto_project
python gui_app.py
```

---

**¿Necesitas ayuda?** Consulta los archivos GUIA_*.md según tu necesidad.
