# 📝 EJEMPLO: Cifrar Texto Directo en la GUI

## 🎯 Diferencia entre Cifrar TEXTO vs ARCHIVOS

### Antes (solo archivos)
❌ Para cifrar un mensaje tenías que:
1. Crear un archivo `.txt`
2. Escribir el mensaje
3. Guardar el archivo
4. Seleccionarlo en la GUI
5. Cifrarlo
6. Obtener un archivo `.enc`

### Ahora (texto directo) ⭐ NUEVO
✅ Puedes cifrar directamente:
1. Escribir el mensaje en la GUI
2. Click en "Cifrar Texto"
3. ¡Listo! Resultado inmediato

---

## 🔒 Tutorial: Cifrar Texto con AES

### Paso 1: Abrir la GUI
```bash
cd crypto_project
python gui_app.py
```

### Paso 2: Generar Clave
1. Ve a la pestaña **"🔒 Cifrado AES"**
2. Selecciona **AES-256** (más seguro)
3. Click en **"Generar Clave"**
4. ⚠️ **Guarda la clave** que aparece (la necesitarás para descifrar)

```
Ejemplo de clave generada:
4ac36b98430c58785cc18ba35f1564efd2c2a0701dc3a067
```

### Paso 3: Cifrar Texto
1. En el cuadro **"Texto a cifrar"** escribe tu mensaje:
   ```
   Este es mi mensaje secreto para Alice
   ```

2. Click en **"🔒 Cifrar Texto"**

3. En el cuadro **"Resultado"** aparece el texto cifrado en HEX:
   ```
   a3f8b2c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2
   ```

### Paso 4: Descifrar Texto
1. **Copia** el texto cifrado (todo el código HEX)

2. **Pégalo** en el cuadro **"Texto a cifrar"** (sí, el mismo cuadro)

3. Click en **"🔓 Descifrar Texto"**

4. En **"Resultado"** aparece tu mensaje original:
   ```
   Este es mi mensaje secreto para Alice
   ```

---

## ✍️ Tutorial: Firmar Mensajes

### Paso 1: Generar Claves RSA
1. Ve a la pestaña **"🔑 Cifrado RSA"**
2. Click en **"Generar Claves RSA-2048"**
3. **Guarda** las claves (opcional pero recomendado)

### Paso 2: Firmar un Mensaje
1. Ve a la pestaña **"✍️ Firma Digital"**
2. En el cuadro superior escribe tu mensaje:
   ```
   Contrato: Pago de $100,000 a Bob
   Fecha: 2025-11-23
   Firmado: Alice
   ```

3. Click en **"✍️ Firmar Documento"**

4. La firma aparece en el log:
   ```
   Firma (hex):
   3a7f8b2c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2...
   ```

### Paso 3: Verificar la Firma
1. La firma se copia automáticamente al campo de verificación

2. Si modificas **aunque sea un carácter** del mensaje:
   ```
   Contrato: Pago de $200,000 a Bob  <-- cambió de 100k a 200k
   Fecha: 2025-11-23
   Firmado: Alice
   ```

3. Click en **"✅ Verificar Firma"**

4. Resultado: **❌ FIRMA INVÁLIDA**
   ```
   ⚠️ El documento fue modificado o la firma no es auténtica
   ```

---

## 💡 Casos de Uso Reales

### Caso 1: Enviar Mensaje Secreto
**Escenario:** Quieres enviar tu contraseña a un compañero

1. Genera clave AES-256
2. Cifra el texto: `mi_password_123`
3. Envía por email: 
   - El texto cifrado (HEX)
   - La clave (por otro canal, ej: WhatsApp)
4. Tu compañero descifra con la misma clave

### Caso 2: Firmar un Documento
**Escenario:** Quieres firmar digitalmente un acuerdo

1. Genera claves RSA
2. Escribe el acuerdo en el campo de texto
3. Firma el documento
4. Envía al destinatario:
   - El documento original
   - La firma (HEX)
   - Tu clave pública
5. El destinatario verifica que es auténtico

### Caso 3: Detectar Modificaciones
**Escenario:** Verificar si un mensaje fue alterado

1. Recibes un mensaje firmado
2. Copias el mensaje en el campo de verificación
3. Pegas la firma
4. Verificas:
   - ✅ Firma válida = mensaje original
   - ❌ Firma inválida = mensaje modificado

---

## 🔐 Ventajas del Cifrado de Texto Directo

| Característica | Texto Directo | Archivos |
|----------------|---------------|----------|
| **Velocidad** | ⚡ Instantáneo | Lento (crear/abrir archivo) |
| **Simplicidad** | ✅ Copiar/Pegar | Gestión de archivos |
| **Uso** | Mensajes cortos | Documentos grandes |
| **Compartir** | Fácil (copiar HEX) | Enviar archivo .enc |

---

## ⚠️ Consejos de Seguridad

### Para Cifrar Texto
1. ✅ **Guarda la clave** en un lugar seguro
2. ✅ Usa **AES-256** (máxima seguridad)
3. ❌ **NO** compartas la clave por el mismo canal que el mensaje cifrado
4. ✅ El texto cifrado está en **HEX** (seguro para copiar/pegar)

### Para Firmar Mensajes
1. ✅ **Protege tu clave privada** (nunca la compartas)
2. ✅ Puedes compartir tu **clave pública** libremente
3. ✅ **Cualquier modificación** invalida la firma
4. ❌ No reutilices claves para diferentes propósitos

---

## 📊 Formato del Texto Cifrado

Cuando cifras texto, el resultado en HEX contiene:

```
[12 bytes: Nonce][16 bytes: Tag][N bytes: Ciphertext]
│             │               │
│             │               └─> Tu mensaje cifrado
│             └─> Autenticación (detecta cambios)
└─> Número único (evita patrones)

Total en HEX: (12 + 16 + N) × 2 caracteres
```

**Ejemplo:**
- Mensaje original: `"Hola"` (4 bytes)
- Nonce: 12 bytes
- Tag: 16 bytes
- Ciphertext: 4 bytes
- **Total: 32 bytes = 64 caracteres HEX**

---

## 🎓 Comparación con Requisitos del Proyecto

| Requisito | Archivo | Texto Directo |
|-----------|---------|---------------|
| Cifrado AES | ✅ | ✅ |
| Firma Digital | ✅ | ✅ |
| Integridad SHA-256 | ✅ (archivos) | ✅ (firma) |
| Demostración | ✅ | ✅ |

**Conclusión:** Ambas formas cumplen los requisitos, pero **texto directo es más práctico para mensajes cortos**.

---

## 🚀 Resumen Rápido

```
CIFRAR TEXTO:
1. Generar clave AES
2. Escribir mensaje
3. Click "Cifrar Texto"
4. Copiar resultado HEX

DESCIFRAR TEXTO:
1. Tener la misma clave
2. Pegar texto cifrado (HEX)
3. Click "Descifrar Texto"
4. Leer mensaje original

FIRMAR MENSAJE:
1. Generar claves RSA
2. Escribir mensaje
3. Click "Firmar Documento"
4. Copiar firma (HEX)

VERIFICAR FIRMA:
1. Tener clave pública
2. Pegar mensaje + firma
3. Click "Verificar Firma"
4. Ver resultado (✅/❌)
```

---

## 📞 Preguntas Frecuentes

**P: ¿Qué formato es el texto cifrado?**
R: Hexadecimal (0-9, a-f). Seguro para copiar/pegar en email, chat, etc.

**P: ¿Puedo cifrar emojis o caracteres especiales?**
R: ✅ Sí, usa UTF-8. Ejemplo: `🔒 Mensaje secreto 🔐`

**P: ¿Cuántos caracteres puedo cifrar?**
R: Con AES: ilimitado. Con RSA: máximo ~200 bytes (usa híbrido para más)

**P: ¿Es seguro?**
R: ✅ Sí. AES-256 es el mismo usado por bancos y gobiernos

**P: ¿Puedo descifrar sin la clave?**
R: ❌ No. Sin la clave correcta es imposible descifrar

**P: ¿La firma detecta cualquier cambio?**
R: ✅ Sí. Incluso cambiar un punto (.) invalida la firma

---

¡Ahora puedes cifrar y firmar mensajes directamente sin crear archivos! 🎉
