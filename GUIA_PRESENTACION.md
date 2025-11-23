# 🎤 GUÍA PARA LA PRESENTACIÓN DEL PROYECTO

## 📋 Preparación Previa

### Antes de la Presentación
1. **Verificar instalación**:
   ```bash
   cd crypto_project
   python -c "from Crypto.Cipher import AES; print('✓ Todo listo')"
   ```

2. **Tener archivos de prueba listos**:
   - Un archivo de texto simple (ej: `contrato.txt`)
   - Contenido sugerido: "Contrato entre Alice y Bob por $100,000"

3. **Cerrar otras aplicaciones** para mejor rendimiento

4. **Tener el proyecto abierto** en VS Code o editor

---

## 🎯 Estructura de la Presentación (20 minutos)

### 1️⃣ INTRODUCCIÓN (2-3 minutos)

**Qué decir:**
```
"Buenos días/tardes. Hoy presento mi proyecto de criptografía donde implementé
y analicé algoritmos modernos de cifrado, firma digital y verificación de 
integridad.

El proyecto incluye:
- Cifrado simétrico con AES (128, 192, 256 bits)
- Cifrado asimétrico con RSA (2048 bits)
- Sistema de firma digital
- Verificación de integridad con SHA-256
- Y como valor agregado, una interfaz gráfica completa
"
```

**Mostrar:**
- Abrir `README.md` brevemente
- Mostrar la tabla de contenidos
- Mencionar 600+ líneas de documentación

---

### 2️⃣ DEMOSTRACIÓN EN VIVO (12-14 minutos)

#### 🔐 Paso 1: Abrir la GUI (1 min)

```bash
python gui_app.py
```

**Qué decir:**
```
"He creado una interfaz gráfica moderna con 5 pestañas que cubren todas
las funcionalidades. Vamos a ver cada una."
```

#### 🔒 Paso 2: Cifrado AES (2-3 min)

**Acciones:**
1. Ir a pestaña "Cifrado AES"
2. Seleccionar AES-256
3. Clic en "Generar Clave"
4. Mostrar la clave generada

**Qué decir:**
```
"Primero, el cifrado simétrico con AES. He implementado soporte para claves
de 128, 192 y 256 bits. Voy a generar una clave de 256 bits, que es el
tamaño más seguro.

[Generar clave]

Como ven, la clave es completamente aleatoria y se muestra en hexadecimal.
Esta es la clave que usaremos tanto para cifrar como para descifrar."
```

5. Seleccionar archivo `contrato.txt`
6. Cifrar archivo

**Qué decir:**
```
"Ahora voy a cifrar un archivo. Selecciono mi archivo de texto...
[Seleccionar y cifrar]

El sistema usa AES-GCM, que es un modo autenticado. Esto significa que no
solo cifra el contenido, sino que también garantiza que no ha sido modificado.
El archivo cifrado se guarda con extensión .enc

Como ven en el log, muestra el tamaño original y el tamaño cifrado. El cifrado
agrega algunos bytes para el nonce y el tag de autenticación."
```

7. Descifrar archivo

**Qué decir:**
```
"Para descifrar, simplemente selecciono el archivo cifrado y uso la misma
clave. Si alguien modificara el archivo cifrado o usara una clave incorrecta,
la verificación de integridad fallaría."
```

#### 🔑 Paso 3: RSA (2 min)

**Acciones:**
1. Ir a pestaña "Cifrado RSA"
2. Generar claves RSA-2048

**Qué decir:**
```
"Ahora el cifrado asimétrico con RSA. A diferencia de AES, RSA usa un par
de claves: una pública y una privada.

[Generar claves]

La generación toma unos segundos porque estamos generando números primos
muy grandes. Estas son claves de 2048 bits, que es el mínimo recomendado
actualmente.

La clave pública se puede compartir con cualquiera. La privada debe
mantenerse secreta. En un escenario real, yo podría dar mi clave pública
a un compañero, él cifraría un mensaje con ella, y solo yo podría 
descifrarlo con mi clave privada."
```

3. Mostrar opción de guardar claves

**Qué decir:**
```
"Puedo guardar estas claves en formato PEM, que es el estándar usado en
certificados SSL, SSH, etc."
```

#### ✍️ Paso 4: Firma Digital (3-4 min)

**Acciones:**
1. Ir a pestaña "Firma Digital"
2. Escribir en el área de texto: "Contrato: Alice vende a Bob su casa por $100,000"
3. Firmar documento

**Qué decir:**
```
"La firma digital es fundamental para garantizar autenticidad e integridad.
Voy a escribir un contrato simple...

[Escribir y firmar]

La firma se genera usando SHA-256 para hacer un hash del documento, y luego
ese hash se cifra con mi clave privada usando RSA-PSS.

Como ven, la firma está en formato hexadecimal. Esta firma se puede verificar
usando mi clave pública."
```

4. Verificar firma (copiar el mismo texto)

**Qué decir:**
```
"Ahora verifico la firma con el mismo documento...

[Verificar]

✅ Firma válida. Esto confirma que el documento no fue modificado y que
efectivamente yo lo firmé."
```

5. **IMPORTANTE**: Modificar el documento

**Qué decir:**
```
"Ahora voy a simular un ataque. Alguien modifica el contrato para cambiar
el monto...

[Cambiar $100,000 por $1,000,000]
[Verificar de nuevo]

❌ Firma inválida. El sistema detectó inmediatamente que el documento fue
alterado. Esto es exactamente lo que previene las firmas digitales: cualquier
modificación, por mínima que sea, invalida la firma."
```

#### 🔍 Paso 5: Verificación de Integridad (2-3 min)

**Acciones:**
1. Ir a pestaña "Integridad"
2. Seleccionar un archivo
3. Calcular hash

**Qué decir:**
```
"La última funcionalidad principal es la verificación de integridad usando
SHA-256.

[Calcular hash]

Este hash es como una huella digital del archivo. Si cambio un solo bit del
archivo, el hash será completamente diferente. Esto demuestra la propiedad
del 'efecto avalancha' de las funciones hash."
```

4. Registrar archivo

**Qué decir:**
```
"Ahora registro este archivo en mi base de datos de integridad...

[Registrar]

El sistema guarda el hash junto con un timestamp. Esto es útil para auditoría."
```

5. Simular: Abrir el archivo en un editor, agregar texto, guardar
6. Verificar integridad

**Qué decir:**
```
"Voy a simular que alguien modificó el archivo...
[Modificar archivo externamente o usar bloc de notas]

Ahora verifico su integridad...

[Verificar]

⚠️ El sistema detectó que el archivo fue modificado. Compara el hash actual
con el hash registrado y son diferentes. Esto es útil para detectar
modificaciones no autorizadas en archivos críticos."
```

#### 🔐 Paso 6: Esquema Híbrido (1-2 min)

**Qué decir:**
```
"Finalmente, el esquema híbrido combina lo mejor de AES y RSA.

RSA es muy seguro pero lento y limitado en tamaño. AES es extremadamente
rápido pero requiere intercambiar la clave de forma segura.

La solución: usar AES para cifrar el archivo (rápido) y RSA para cifrar
la clave AES (seguro). Esto es exactamente lo que hace HTTPS/TLS.

Este es el estándar en comunicaciones seguras modernas."
```

---

### 3️⃣ PRUEBAS TÉCNICAS (3-4 minutos)

**Acciones:**
1. Abrir nueva terminal
2. Ejecutar pruebas comprehensivas

```bash
python tests/comprehensive_tests.py
```

**Qué decir mientras se ejecutan:**
```
"Ahora voy a ejecutar la suite completa de pruebas. Este script:

- Compara tamaños de clave AES (128, 192, 256)
- Evalúa modos de operación (GCM vs CBC)
- Mide rendimiento simétrico vs asimétrico
- Demuestra la importancia del IV
- Prueba firmas digitales con casos de fallo
- Verifica integridad de archivos
- Y más...

[Mientras se ejecuta, ir comentando]

Vean que AES es muchísimo más rápido que RSA - por eso el esquema híbrido
es tan importante.

También muestra cómo el mismo mensaje cifrado dos veces produce ciphertexts
completamente diferentes gracias al IV aleatorio.
"
```

3. Al terminar, mostrar el resumen final

---

### 4️⃣ ANÁLISIS DE SEGURIDAD (2-3 minutos)

**Acciones:**
1. Abrir `README.md`
2. Ir a la sección "Análisis de Seguridad"

**Qué decir:**
```
"Una parte importante del proyecto es el análisis de seguridad. He documentado:

[Mostrar en README]

1. Vulnerabilidades de algoritmos obsoletos:
   - DES: Solo 56 bits, roto en 1998
   - 3DES: Deprecado oficialmente en 2023
   - MD5: Colisiones encontradas
   - SHA-1: Ya no es seguro

2. Ataques conocidos y sus mitigaciones:
   - Padding oracle: Mitigado usando GCM
   - Reutilización de IV: Prevenido con generación aleatoria
   - Ataques de timing: Implementaciones en tiempo constante

3. Mejores prácticas aplicadas:
   - Claves de tamaño adecuado (AES-256, RSA-2048)
   - Algoritmos modernos
   - Autenticación siempre (GCM o HMAC)
   - Verificación antes de descifrar
"
```

**Mostrar tabla de comparación:**
```
"También he incluido comparaciones de rendimiento y fortaleza de claves,
mostrando que RSA-2048 es equivalente a aproximadamente 112 bits de
seguridad simétrica, por eso AES-128 es suficiente en la práctica."
```

---

### 5️⃣ CONCLUSIONES (2 minutos)

**Qué decir:**
```
"Para concluir, este proyecto cumple completamente con los requisitos:

✅ Cifrado simétrico AES con evaluación de tamaños de clave y modos
✅ Cifrado asimétrico RSA con análisis de rendimiento
✅ Firma digital con detección de modificaciones
✅ Verificación de integridad con sistema automático
✅ Análisis de vulnerabilidades de DES y mejores prácticas

Como valor agregado:
✅ Interfaz gráfica moderna y funcional
✅ Suite completa de pruebas automatizadas
✅ Más de 600 líneas de documentación técnica
✅ Esquema híbrido implementado

Aplicaciones prácticas:
- Protección de archivos confidenciales
- Firma de contratos digitales
- Verificación de descargas
- Auditoría de sistemas

Todo el código está documentado, probado y listo para usar.
¿Alguna pregunta?"
```

---

## 🎯 Consejos para la Presentación

### ✅ Hacer
- **Practicar antes** al menos 2 veces
- **Hablar con confianza** - conoces el proyecto
- **Mostrar entusiasmo** por lo que hiciste
- **Explicar conceptos** en términos simples
- **Preparar el archivo de prueba** antes
- **Tener el proyecto abierto** y listo

### ❌ Evitar
- Leer directamente del código
- Ir muy rápido - dar tiempo a procesar
- Saltarse la demo en vivo
- Olvidar cerrar otras aplicaciones
- Perderse en detalles técnicos excesivos

---

## 💡 Preguntas Frecuentes Anticipadas

### "¿Por qué usaste Python?"
```
"Python es ideal para prototipos de criptografía por su simplicidad y
la disponibilidad de bibliotecas robustas como PyCryptodome. En producción
se usarían implementaciones optimizadas en C/C++, pero para demostrar
conceptos y aprender, Python es perfecto."
```

### "¿Es seguro para uso real?"
```
"El código usa algoritmos estándar y bibliotecas establecidas (PyCryptodome),
por lo que la criptografía en sí es segura. Para uso en producción real se
necesitarían aspectos adicionales como gestión de claves con HSM, logs de
auditoría, manejo de errores más robusto, etc. Pero como implementación
educativa y prototipo, cumple con estándares de seguridad."
```

### "¿Por qué no implementaste los algoritmos desde cero?"
```
"Una regla fundamental en criptografía es NUNCA implementar algoritmos
desde cero a menos que seas un experto. Las implementaciones establecidas
han sido revisadas por miles de expertos y probadas exhaustivamente.
Implementar tu propio AES o RSA casi garantiza introducir vulnerabilidades.
Por eso usé PyCryptodome, que es una biblioteca confiable y ampliamente
usada."
```

### "¿Qué fue lo más difícil?"
```
"Entender todos los detalles de seguridad - cosas como por qué el IV debe
ser único, por qué necesitamos autenticación además de cifrado, cómo
funcionan los ataques de padding oracle. La criptografía tiene muchos
detalles sutiles donde un pequeño error puede comprometer toda la seguridad."
```

---

## 📊 Tiempos Estimados

- Introducción: 2-3 min
- Demo GUI: 12-14 min
- Pruebas: 3-4 min
- Seguridad: 2-3 min
- Conclusiones: 2 min
- **Total: ~20-25 minutos**
- Preguntas: 5-10 min

---

## ✅ Checklist Final Antes de Presentar

- [ ] Proyecto funciona correctamente
- [ ] GUI abre sin errores
- [ ] Pruebas pasan completamente
- [ ] Archivo de prueba preparado
- [ ] README abierto en pestaña
- [ ] Terminal lista
- [ ] Otras aplicaciones cerradas
- [ ] Practicaste al menos 2 veces
- [ ] Conoces el orden de la demo
- [ ] Batería del laptop cargada
- [ ] Backup del proyecto (USB/nube)

---

## 🎤 Frases de Cierre

```
"Gracias por su atención. Este proyecto me ayudó a comprender profundamente
cómo funcionan los sistemas de seguridad modernos que usamos todos los días
en HTTPS, email cifrado, firmas digitales, etc.

Estoy orgullosa del resultado y espero que esta demostración haya sido clara
e interesante.

¿Alguna pregunta?"
```

---

**¡Éxito en tu presentación!** 🚀🎓
