# 🎨 INTERFAZ GRÁFICA - Guía de Uso

## 🚀 Inicio Rápido

Para abrir la interfaz gráfica:

```bash
cd crypto_project
python gui_app.py
```

## 📋 Características de la Interfaz

La aplicación tiene **5 pestañas principales** con interfaz moderna y oscura:

### 🔒 1. Cifrado AES
**Funcionalidades:**
- Generar claves AES (128, 192, 256 bits)
- **Cifrar/descifrar TEXTO directo** ⭐ NUEVO
- Cifrar/descifrar ARCHIVOS con AES-GCM
- Ver logs de todas las operaciones

**Cómo usar (TEXTO):** ⭐ NUEVO
1. Selecciona el tamaño de clave (128, 192 o 256 bits)
2. Haz clic en "Generar Clave"
3. Escribe tu mensaje en "Texto a cifrar"
4. Haz clic en "🔒 Cifrar Texto"
5. El resultado aparece en HEX en "Resultado"
6. Para descifrar: copia el texto cifrado al campo superior
7. Haz clic en "🔓 Descifrar Texto"

**Cómo usar (ARCHIVOS):**
1. Selecciona el tamaño de clave (128, 192 o 256 bits)
2. Haz clic en "Generar Clave"
3. Selecciona un archivo para cifrar
4. Haz clic en "🔒 Cifrar Archivo"
5. El archivo cifrado se guardará con extensión `.enc`
6. Para descifrar, selecciona el archivo `.enc` y usa "🔓 Descifrar Archivo"

### 🔑 2. Cifrado RSA
**Funcionalidades:**
- Generar pares de claves RSA-2048
- Guardar claves en formato PEM
- Cargar claves existentes
- Visualizar claves generadas

**Cómo usar:**
1. Haz clic en "Generar Claves RSA-2048"
2. Guarda la clave privada (¡muy importante!)
3. Guarda la clave pública (para compartir)
4. O carga claves previamente generadas

### ✍️ 3. Firma Digital
**Funcionalidades:**
- Firmar MENSAJES/DOCUMENTOS con RSA-PSS
- Verificar firmas digitales
- Detectar documentos modificados
- **Trabaja con TEXTO directo** (no requiere archivos)

**Cómo usar para firmar:**
1. Asegúrate de tener una clave privada (pestaña RSA)
2. Escribe el mensaje/documento en el área de texto
3. Haz clic en "✍️ Firmar Documento"
4. La firma se mostrará en formato hexadecimal
5. La firma se copia automáticamente al campo de verificación

**Cómo usar para verificar:**
1. Asegúrate de tener la clave pública
2. Pega o escribe el documento EXACTAMENTE igual
3. Pega la firma en formato hexadecimal
4. Haz clic en "✅ Verificar Firma"
5. Si modificas aunque sea un carácter, la firma será INVÁLIDA ❌
5. Verás si la firma es válida o inválida

### 🔍 4. Integridad
**Funcionalidades:**
- Calcular hash SHA-256 de archivos
- Registrar archivos en base de datos de integridad
- Verificar si archivos fueron modificados
- Verificar todos los archivos registrados

**Cómo usar:**
1. **Calcular hash**: Selecciona archivo → "Calcular Hash"
2. **Registrar**: Selecciona archivo → "📝 Registrar en BD de Integridad"
3. **Verificar uno**: Selecciona archivo registrado → "🔍 Verificar Archivo Actual"
4. **Verificar todos**: "📊 Verificar Todos los Archivos Registrados"

**Casos de uso:**
- Detectar modificaciones no autorizadas
- Verificar integridad de descargas
- Auditoría de archivos críticos

### 🔐 5. Híbrido
**Funcionalidades:**
- Cifrado híbrido (AES + RSA) para archivos grandes
- Descifrado híbrido
- Aprovecha velocidad de AES y seguridad de RSA

**Cómo usar:**
1. Asegúrate de tener claves RSA generadas
2. **Para cifrar**:
   - Selecciona archivo
   - Haz clic en "🔒 Cifrar con Esquema Híbrido"
   - Se genera archivo `.hybrid`
3. **Para descifrar**:
   - Selecciona archivo `.hybrid`
   - Haz clic en "🔓 Descifrar con Esquema Híbrido"
   - Necesitas la clave privada correspondiente

## 🎯 Casos de Uso Prácticos

### Caso 1: Cifrar un archivo confidencial
1. Ve a pestaña **Cifrado AES**
2. Genera clave AES-256
3. Selecciona tu archivo
4. Cifra
5. **Guarda la clave de forma segura** (sin ella no podrás descifrar)

### Caso 2: Firmar un contrato digital
1. Ve a pestaña **Cifrado RSA**
2. Genera o carga tu clave privada
3. Ve a pestaña **Firma Digital**
4. Escribe el contrato
5. Firma el documento
6. Comparte el documento y la firma con la otra parte

### Caso 3: Verificar integridad de archivos
1. Ve a pestaña **Integridad**
2. Selecciona archivos importantes
3. Regístralos en la BD
4. Más tarde, verifica si fueron modificados
5. El sistema detectará cualquier cambio

### Caso 4: Enviar archivo grande de forma segura
1. Ve a pestaña **Cifrado RSA**
2. Obtén la clave pública del destinatario
3. Ve a pestaña **Híbrido**
4. Cifra el archivo con su clave pública
5. Envía el archivo `.hybrid`
6. Solo el destinatario con la clave privada podrá descifrar

## 🎨 Características de la Interfaz

- **Diseño moderno**: Tema oscuro profesional
- **Logs en tiempo real**: Cada operación se registra
- **Barra de estado**: Muestra el estado actual
- **Diálogos de archivo**: Fácil selección de archivos
- **Mensajes claros**: Notificaciones de éxito/error
- **Responsive**: Se adapta al tamaño de ventana

## ⚠️ Consejos de Seguridad

1. **Claves Privadas**: NUNCA las compartas ni las pierdas
2. **Claves AES**: Guárdalas de forma segura
3. **Backups**: Haz backup de tus claves
4. **Cifrado**: Usa AES-256 para máxima seguridad
5. **Verificación**: Siempre verifica firmas antes de confiar en documentos

## 🐛 Solución de Problemas

### La ventana no abre
- Verifica que tkinter esté instalado (viene con Python)
- Ejecuta desde la carpeta `crypto_project`

### Error al cifrar/descifrar
- Verifica que hayas generado la clave primero
- Asegúrate de usar la misma clave para cifrar y descifrar

### Error en firma digital
- Verifica que tengas la clave privada (para firmar)
- Verifica que tengas la clave pública (para verificar)

### Archivo no encontrado
- Usa el botón "Seleccionar" en lugar de escribir la ruta
- Verifica que el archivo exista

## 💡 Tips y Trucos

1. **Múltiples archivos**: Puedes cifrar varios archivos secuencialmente
2. **Logs**: Los logs muestran información detallada de cada operación
3. **Copiar firma**: Al firmar, la firma se copia automáticamente
4. **Extensiones**: 
   - `.enc` → Cifrado AES
   - `.hybrid` → Cifrado híbrido
   - `.pem` → Claves RSA

## 🎓 Para tu Presentación

La interfaz es ideal para demostrar:
- ✅ Todas las funcionalidades implementadas
- ✅ Casos de uso reales
- ✅ Diferencias entre algoritmos
- ✅ Detección de modificaciones
- ✅ Facilidad de uso

---

**¡Disfruta de la interfaz gráfica!** 🚀
