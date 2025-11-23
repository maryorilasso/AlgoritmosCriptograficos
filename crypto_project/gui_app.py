"""
Interfaz Gráfica para el Proyecto de Criptografía
Proporciona una GUI moderna con pestañas para todas las funcionalidades
"""

import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext, messagebox
import os
import sys
from pathlib import Path

# Agregar el directorio al path
sys.path.insert(0, str(Path(__file__).parent))

from aescipher import generate_aes_key, encrypt_file_gcm, decrypt_file_gcm, encrypt_gcm, decrypt_gcm
from rsautils import (
    generate_rsa_keypair, load_private_key, load_public_key,
    sign_message, verify_signature
)
from hashutils import (
    calculate_file_hash, register_file, verify_file_integrity,
    verify_all_files
)
from hybrid import encrypt_file_hybrid, decrypt_file_hybrid


class CryptoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Sistema de Criptografía - Proyecto SI")
        self.root.geometry("900x700")
        self.root.configure(bg='#2c3e50')
        
        # Variables
        self.aes_key = None
        self.rsa_private_key = None
        self.rsa_public_key = None
        
        # Estilo
        self.setup_style()
        
        # Crear interfaz
        self.create_widgets()
        
    def setup_style(self):
        """Configurar estilos personalizados"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Colores
        bg_color = '#34495e'
        fg_color = '#ecf0f1'
        accent_color = '#3498db'
        
        style.configure('TNotebook', background=bg_color, borderwidth=0)
        style.configure('TNotebook.Tab', background=bg_color, foreground=fg_color, 
                       padding=[20, 10], font=('Segoe UI', 10, 'bold'))
        style.map('TNotebook.Tab', background=[('selected', accent_color)])
        
        style.configure('TFrame', background=bg_color)
        style.configure('TLabel', background=bg_color, foreground=fg_color, 
                       font=('Segoe UI', 10))
        style.configure('Title.TLabel', font=('Segoe UI', 14, 'bold'))
        style.configure('TButton', font=('Segoe UI', 10, 'bold'), padding=10)
        
    def create_widgets(self):
        """Crear todos los widgets de la interfaz"""
        # Título principal
        title_frame = tk.Frame(self.root, bg='#2c3e50')
        title_frame.pack(fill='x', pady=10)
        
        title = tk.Label(title_frame, text="🔐 Sistema de Criptografía", 
                        font=('Segoe UI', 20, 'bold'), bg='#2c3e50', fg='#ecf0f1')
        title.pack()
        
        subtitle = tk.Label(title_frame, text="Proyecto de Seguridad Informática", 
                           font=('Segoe UI', 11), bg='#2c3e50', fg='#95a5a6')
        subtitle.pack()
        
        # Notebook (pestañas)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Crear pestañas
        self.create_aes_tab()
        self.create_rsa_tab()
        self.create_signature_tab()
        self.create_hash_tab()
        self.create_hybrid_tab()
        
        # Barra de estado
        self.status_bar = tk.Label(self.root, text="Listo", bd=1, relief=tk.SUNKEN, 
                                   anchor=tk.W, bg='#34495e', fg='#ecf0f1')
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def create_aes_tab(self):
        """Pestaña de cifrado AES"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="🔒 Cifrado AES")
        
        # Frame principal con scroll
        canvas = tk.Canvas(tab, bg='#34495e', highlightthickness=0)
        scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Título
        ttk.Label(scrollable_frame, text="Cifrado Simétrico AES", 
                 style='Title.TLabel').grid(row=0, column=0, columnspan=3, pady=10)
        
        # Generación de clave
        ttk.Label(scrollable_frame, text="1. Generar Clave AES:").grid(row=1, column=0, sticky='w', padx=20, pady=5)
        
        key_size_frame = ttk.Frame(scrollable_frame)
        key_size_frame.grid(row=2, column=0, columnspan=3, padx=20, pady=5)
        
        self.aes_key_size = tk.IntVar(value=256)
        ttk.Radiobutton(key_size_frame, text="AES-128", variable=self.aes_key_size, 
                       value=128).pack(side='left', padx=5)
        ttk.Radiobutton(key_size_frame, text="AES-192", variable=self.aes_key_size, 
                       value=192).pack(side='left', padx=5)
        ttk.Radiobutton(key_size_frame, text="AES-256", variable=self.aes_key_size, 
                       value=256).pack(side='left', padx=5)
        
        key_gen_frame = ttk.Frame(scrollable_frame)
        key_gen_frame.grid(row=3, column=0, columnspan=3, pady=10)
        ttk.Button(key_gen_frame, text="Generar Clave", 
                  command=self.generate_aes_key).pack(side='left', padx=5)
        ttk.Button(key_gen_frame, text=" Copiar Clave", 
                  command=self.copy_aes_key).pack(side='left', padx=5)
        
        self.aes_key_label = ttk.Label(scrollable_frame, text="No hay clave generada", 
                                       foreground='#e74c3c')
        self.aes_key_label.grid(row=4, column=0, columnspan=3, pady=5)
        
        # Separador
        ttk.Separator(scrollable_frame, orient='horizontal').grid(row=5, column=0, 
                                                                  columnspan=3, sticky='ew', pady=20)
        
        # === CIFRADO DE TEXTO DIRECTO ===
        ttk.Label(scrollable_frame, text="2. Cifrar/Descifrar Texto:").grid(row=6, column=0, sticky='w', padx=20, pady=5)
        
        # Entrada de texto
        ttk.Label(scrollable_frame, text="Texto a cifrar:").grid(row=7, column=0, sticky='w', padx=20, pady=2)
        self.aes_text_input = scrolledtext.ScrolledText(scrollable_frame, height=4, width=70, 
                                                        bg='#ecf0f1', fg='#2c3e50', font=('Consolas', 9))
        self.aes_text_input.grid(row=8, column=0, columnspan=3, padx=20, pady=5)
        
        # Botones de texto
        text_btn_frame = ttk.Frame(scrollable_frame)
        text_btn_frame.grid(row=9, column=0, columnspan=3, pady=5)
        ttk.Button(text_btn_frame, text="🔒 Cifrar Texto", 
                  command=self.encrypt_aes_text).pack(side='left', padx=5)
        ttk.Button(text_btn_frame, text="🔓 Descifrar Texto", 
                  command=self.decrypt_aes_text).pack(side='left', padx=5)
        ttk.Button(text_btn_frame, text="🗑️ Limpiar", 
                  command=lambda: self.aes_text_output.delete('1.0', tk.END)).pack(side='left', padx=5)
        
        # Salida de texto
        ttk.Label(scrollable_frame, text="Resultado:").grid(row=10, column=0, sticky='w', padx=20, pady=2)
        self.aes_text_output = scrolledtext.ScrolledText(scrollable_frame, height=4, width=70, 
                                                         bg='#ecf0f1', fg='#2c3e50', font=('Consolas', 9))
        self.aes_text_output.grid(row=11, column=0, columnspan=3, padx=20, pady=5)
        
        # Separador
        ttk.Separator(scrollable_frame, orient='horizontal').grid(row=12, column=0, 
                                                                  columnspan=3, sticky='ew', pady=20)
        
        # Cifrado de archivos
        ttk.Label(scrollable_frame, text="3. Cifrar Archivo:").grid(row=13, column=0, sticky='w', padx=20, pady=5)
        
        self.aes_input_file = tk.StringVar()
        ttk.Entry(scrollable_frame, textvariable=self.aes_input_file, 
                 width=50).grid(row=14, column=0, columnspan=2, padx=20, pady=5)
        ttk.Button(scrollable_frame, text="Seleccionar", 
                  command=lambda: self.browse_file(self.aes_input_file)).grid(row=14, column=2, padx=5)
        
        ttk.Button(scrollable_frame, text="🔒 Cifrar Archivo", 
                  command=self.encrypt_aes).grid(row=15, column=0, columnspan=3, pady=10)
        
        # Descifrado de archivos
        ttk.Label(scrollable_frame, text="4. Descifrar Archivo:").grid(row=16, column=0, sticky='w', padx=20, pady=5)
        
        self.aes_encrypted_file = tk.StringVar()
        ttk.Entry(scrollable_frame, textvariable=self.aes_encrypted_file, 
                 width=50).grid(row=17, column=0, columnspan=2, padx=20, pady=5)
        ttk.Button(scrollable_frame, text="Seleccionar", 
                  command=lambda: self.browse_file(self.aes_encrypted_file)).grid(row=17, column=2, padx=5)
        
        ttk.Button(scrollable_frame, text="🔓 Descifrar Archivo", 
                  command=self.decrypt_aes).grid(row=18, column=0, columnspan=3, pady=10)
        
        # Log
        ttk.Label(scrollable_frame, text="Registro de Operaciones:").grid(row=19, column=0, sticky='w', padx=20, pady=5)
        self.aes_log = scrolledtext.ScrolledText(scrollable_frame, height=10, width=80, 
                                                 bg='#2c3e50', fg='#ecf0f1', font=('Consolas', 9))
        self.aes_log.grid(row=20, column=0, columnspan=3, padx=20, pady=5)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
    def create_rsa_tab(self):
        """Pestaña de cifrado RSA"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="🔑 Cifrado RSA")
        
        canvas = tk.Canvas(tab, bg='#34495e', highlightthickness=0)
        scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Título
        ttk.Label(scrollable_frame, text="Cifrado Asimétrico RSA", 
                 style='Title.TLabel').grid(row=0, column=0, columnspan=3, pady=10)
        
        # Generación de claves
        ttk.Label(scrollable_frame, text="1. Generar Par de Claves RSA:").grid(row=1, column=0, sticky='w', padx=20, pady=5)
        
        ttk.Button(scrollable_frame, text="Generar Claves RSA-2048", 
                  command=self.generate_rsa_keys).grid(row=2, column=0, columnspan=3, pady=10)
        
        self.rsa_key_label = ttk.Label(scrollable_frame, text="No hay claves generadas", 
                                       foreground='#e74c3c')
        self.rsa_key_label.grid(row=3, column=0, columnspan=3, pady=5)
        
        # Botones para guardar claves
        btn_frame = ttk.Frame(scrollable_frame)
        btn_frame.grid(row=4, column=0, columnspan=3, pady=5)
        ttk.Button(btn_frame, text="Guardar Clave Privada", 
                  command=self.save_private_key).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Guardar Clave Pública", 
                  command=self.save_public_key).pack(side='left', padx=5)
        
        # Separador
        ttk.Separator(scrollable_frame, orient='horizontal').grid(row=5, column=0, 
                                                                  columnspan=3, sticky='ew', pady=20)
        
        # Cargar claves
        ttk.Label(scrollable_frame, text="2. Cargar Claves Existentes:").grid(row=6, column=0, sticky='w', padx=20, pady=5)
        
        load_frame = ttk.Frame(scrollable_frame)
        load_frame.grid(row=7, column=0, columnspan=3, pady=5)
        ttk.Button(load_frame, text="Cargar Clave Privada", 
                  command=self.load_private_key).pack(side='left', padx=5)
        ttk.Button(load_frame, text="Cargar Clave Pública", 
                  command=self.load_public_key).pack(side='left', padx=5)
        
        # Log
        ttk.Label(scrollable_frame, text="Información:").grid(row=8, column=0, sticky='w', padx=20, pady=5)
        self.rsa_log = scrolledtext.ScrolledText(scrollable_frame, height=15, width=80, 
                                                bg='#2c3e50', fg='#ecf0f1', font=('Consolas', 9))
        self.rsa_log.grid(row=9, column=0, columnspan=3, padx=20, pady=5)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
    def create_signature_tab(self):
        """Pestaña de firma digital"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="✍️ Firma Digital")
        
        canvas = tk.Canvas(tab, bg='#34495e', highlightthickness=0)
        scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Título
        ttk.Label(scrollable_frame, text="Firma Digital RSA-PSS", 
                 style='Title.TLabel').grid(row=0, column=0, columnspan=3, pady=10)
        
        # Firmar documento
        ttk.Label(scrollable_frame, text="1. Firmar Documento:").grid(row=1, column=0, sticky='w', padx=20, pady=5)
        
        ttk.Label(scrollable_frame, text="Documento:").grid(row=2, column=0, sticky='w', padx=20)
        self.sign_text = scrolledtext.ScrolledText(scrollable_frame, height=5, width=70, 
                                                   bg='#2c3e50', fg='#ecf0f1', font=('Consolas', 9))
        self.sign_text.grid(row=3, column=0, columnspan=3, padx=20, pady=5)
        
        ttk.Button(scrollable_frame, text="✍️ Firmar Documento", 
                  command=self.sign_document).grid(row=4, column=0, columnspan=3, pady=10)
        
        # Separador
        ttk.Separator(scrollable_frame, orient='horizontal').grid(row=5, column=0, 
                                                                  columnspan=3, sticky='ew', pady=20)
        
        # Verificar firma
        ttk.Label(scrollable_frame, text="2. Verificar Firma:").grid(row=6, column=0, sticky='w', padx=20, pady=5)
        
        ttk.Label(scrollable_frame, text="Documento:").grid(row=7, column=0, sticky='w', padx=20)
        self.verify_text = scrolledtext.ScrolledText(scrollable_frame, height=5, width=70, 
                                                     bg='#2c3e50', fg='#ecf0f1', font=('Consolas', 9))
        self.verify_text.grid(row=8, column=0, columnspan=3, padx=20, pady=5)
        
        ttk.Label(scrollable_frame, text="Firma (hex):").grid(row=9, column=0, sticky='w', padx=20)
        self.signature_entry = ttk.Entry(scrollable_frame, width=70)
        self.signature_entry.grid(row=10, column=0, columnspan=3, padx=20, pady=5)
        
        ttk.Button(scrollable_frame, text="✅ Verificar Firma", 
                  command=self.verify_signature_gui).grid(row=11, column=0, columnspan=3, pady=10)
        
        # Log
        ttk.Label(scrollable_frame, text="Resultado:").grid(row=12, column=0, sticky='w', padx=20, pady=5)
        self.signature_log = scrolledtext.ScrolledText(scrollable_frame, height=10, width=80, 
                                                       bg='#2c3e50', fg='#ecf0f1', font=('Consolas', 9))
        self.signature_log.grid(row=13, column=0, columnspan=3, padx=20, pady=5)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
    def create_hash_tab(self):
        """Pestaña de verificación de integridad"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="🔍 Integridad")
        
        canvas = tk.Canvas(tab, bg='#34495e', highlightthickness=0)
        scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Título
        ttk.Label(scrollable_frame, text="Verificación de Integridad (SHA-256)", 
                 style='Title.TLabel').grid(row=0, column=0, columnspan=3, pady=10)
        
        # Calcular hash
        ttk.Label(scrollable_frame, text="1. Calcular Hash de Archivo:").grid(row=1, column=0, sticky='w', padx=20, pady=5)
        
        self.hash_file = tk.StringVar()
        ttk.Entry(scrollable_frame, textvariable=self.hash_file, 
                 width=50).grid(row=2, column=0, columnspan=2, padx=20, pady=5)
        ttk.Button(scrollable_frame, text="Seleccionar", 
                  command=lambda: self.browse_file(self.hash_file)).grid(row=2, column=2, padx=5)
        
        ttk.Button(scrollable_frame, text="Calcular Hash", 
                  command=self.calculate_hash).grid(row=3, column=0, columnspan=3, pady=10)
        
        # Registrar archivo
        ttk.Label(scrollable_frame, text="2. Registrar Archivo:").grid(row=4, column=0, sticky='w', padx=20, pady=5)
        ttk.Button(scrollable_frame, text="📝 Registrar en BD de Integridad", 
                  command=self.register_file_gui).grid(row=5, column=0, columnspan=3, pady=10)
        
        # Verificar integridad
        ttk.Label(scrollable_frame, text="3. Verificar Integridad:").grid(row=6, column=0, sticky='w', padx=20, pady=5)
        ttk.Button(scrollable_frame, text="🔍 Verificar Archivo Actual", 
                  command=self.verify_integrity).grid(row=7, column=0, columnspan=3, pady=10)
        
        ttk.Button(scrollable_frame, text="📊 Verificar Todos los Archivos Registrados", 
                  command=self.verify_all).grid(row=8, column=0, columnspan=3, pady=10)
        
        # Log
        ttk.Label(scrollable_frame, text="Resultados:").grid(row=9, column=0, sticky='w', padx=20, pady=5)
        self.hash_log = scrolledtext.ScrolledText(scrollable_frame, height=15, width=80, 
                                                  bg='#2c3e50', fg='#ecf0f1', font=('Consolas', 9))
        self.hash_log.grid(row=10, column=0, columnspan=3, padx=20, pady=5)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
    def create_hybrid_tab(self):
        """Pestaña de esquema híbrido"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="🔐 Híbrido")
        
        canvas = tk.Canvas(tab, bg='#34495e', highlightthickness=0)
        scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Título
        ttk.Label(scrollable_frame, text="Esquema Híbrido AES + RSA", 
                 style='Title.TLabel').grid(row=0, column=0, columnspan=3, pady=10)
        
        info = ("Este esquema combina lo mejor de AES y RSA:\n"
                "• AES: Cifra el archivo (rápido para archivos grandes)\n"
                "• RSA: Cifra la clave AES (seguro para intercambio de claves)")
        ttk.Label(scrollable_frame, text=info, justify='left').grid(row=1, column=0, columnspan=3, padx=20, pady=10)
        
        # Cifrado híbrido
        ttk.Label(scrollable_frame, text="1. Cifrar Archivo (Híbrido):").grid(row=2, column=0, sticky='w', padx=20, pady=5)
        
        self.hybrid_input = tk.StringVar()
        ttk.Entry(scrollable_frame, textvariable=self.hybrid_input, 
                 width=50).grid(row=3, column=0, columnspan=2, padx=20, pady=5)
        ttk.Button(scrollable_frame, text="Seleccionar", 
                  command=lambda: self.browse_file(self.hybrid_input)).grid(row=3, column=2, padx=5)
        
        ttk.Button(scrollable_frame, text="🔒 Cifrar con Esquema Híbrido", 
                  command=self.encrypt_hybrid).grid(row=4, column=0, columnspan=3, pady=10)
        
        # Descifrado híbrido
        ttk.Label(scrollable_frame, text="2. Descifrar Archivo (Híbrido):").grid(row=5, column=0, sticky='w', padx=20, pady=5)
        
        self.hybrid_encrypted = tk.StringVar()
        ttk.Entry(scrollable_frame, textvariable=self.hybrid_encrypted, 
                 width=50).grid(row=6, column=0, columnspan=2, padx=20, pady=5)
        ttk.Button(scrollable_frame, text="Seleccionar Paquete", 
                  command=lambda: self.browse_file(self.hybrid_encrypted)).grid(row=6, column=2, padx=5)
        
        ttk.Button(scrollable_frame, text="🔓 Descifrar con Esquema Híbrido", 
                  command=self.decrypt_hybrid).grid(row=7, column=0, columnspan=3, pady=10)
        
        # Log
        ttk.Label(scrollable_frame, text="Registro:").grid(row=8, column=0, sticky='w', padx=20, pady=5)
        self.hybrid_log = scrolledtext.ScrolledText(scrollable_frame, height=15, width=80, 
                                                    bg='#2c3e50', fg='#ecf0f1', font=('Consolas', 9))
        self.hybrid_log.grid(row=9, column=0, columnspan=3, padx=20, pady=5)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    # ==================== MÉTODOS DE FUNCIONALIDAD ====================
    
    def browse_file(self, var):
        """Abrir diálogo para seleccionar archivo"""
        filename = filedialog.askopenfilename()
        if filename:
            var.set(filename)
            
    def log_message(self, log_widget, message, color='#2ecc71'):
        """Agregar mensaje al log"""
        log_widget.insert(tk.END, f"{message}\n", color)
        log_widget.see(tk.END)
        self.root.update()
        
    def update_status(self, message):
        """Actualizar barra de estado"""
        self.status_bar.config(text=message)
        self.root.update()
        
    # --- AES ---
    def generate_aes_key(self):
        """Generar clave AES"""
        try:
            size = self.aes_key_size.get()
            self.aes_key = generate_aes_key(size)
            key_hex = self.aes_key.hex()
            self.aes_key_label.config(text=f"✓ Clave AES-{size} generada: {key_hex[:32]}...", 
                                     foreground='#2ecc71')
            self.log_message(self.aes_log, f"\n✓ Clave AES-{size} generada exitosamente")
            self.log_message(self.aes_log, f"  Clave COMPLETA: {key_hex}")
            self.log_message(self.aes_log, f"  Longitud: {len(self.aes_key)} bytes = {len(self.aes_key)*8} bits")
            self.log_message(self.aes_log, f"  💡 Usa el botón 'Copiar Clave' para copiar al portapapeles")
            self.update_status(f"Clave AES-{size} generada")
        except Exception as e:
            messagebox.showerror("Error", f"Error al generar clave: {e}")
    
    def copy_aes_key(self):
        """Copiar clave AES al portapapeles"""
        if not self.aes_key:
            messagebox.showwarning("Advertencia", "Primero genera una clave AES")
            return
        
        try:
            key_hex = self.aes_key.hex()
            self.root.clipboard_clear()
            self.root.clipboard_append(key_hex)
            self.root.update()
            self.log_message(self.aes_log, f"\n✓ Clave copiada al portapapeles")
            self.log_message(self.aes_log, f"  {key_hex}")
            messagebox.showinfo("Éxito", f"Clave copiada al portapapeles:\n\n{key_hex}")
            self.update_status("Clave copiada al portapapeles")
        except Exception as e:
            messagebox.showerror("Error", f"Error al copiar: {e}")
            
    def encrypt_aes(self):
        """Cifrar archivo con AES"""
        if not self.aes_key:
            messagebox.showwarning("Advertencia", "Primero genera una clave AES")
            return
            
        input_file = self.aes_input_file.get()
        if not input_file or not os.path.exists(input_file):
            messagebox.showwarning("Advertencia", "Selecciona un archivo válido")
            return
            
        try:
            output_file = input_file + ".enc"
            nonce, tag = encrypt_file_gcm(input_file, output_file, self.aes_key)
            
            self.log_message(self.aes_log, f"\n✓ Archivo cifrado exitosamente")
            self.log_message(self.aes_log, f"  Entrada: {input_file}")
            self.log_message(self.aes_log, f"  Salida: {output_file}")
            self.log_message(self.aes_log, f"  Tamaño original: {os.path.getsize(input_file)} bytes")
            self.log_message(self.aes_log, f"  Tamaño cifrado: {os.path.getsize(output_file)} bytes")
            
            self.update_status("Archivo cifrado exitosamente")
            messagebox.showinfo("Éxito", f"Archivo cifrado guardado en:\n{output_file}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al cifrar: {e}")
            
    def decrypt_aes(self):
        """Descifrar archivo con AES"""
        if not self.aes_key:
            messagebox.showwarning("Advertencia", "Primero genera o carga una clave AES")
            return
            
        encrypted_file = self.aes_encrypted_file.get()
        if not encrypted_file or not os.path.exists(encrypted_file):
            messagebox.showwarning("Advertencia", "Selecciona un archivo válido")
            return
            
        try:
            output_file = encrypted_file.replace(".enc", "_decrypted.txt")
            success = decrypt_file_gcm(encrypted_file, output_file, self.aes_key)
            
            if success:
                self.log_message(self.aes_log, f"\n✓ Archivo descifrado exitosamente")
                self.log_message(self.aes_log, f"  Entrada: {encrypted_file}")
                self.log_message(self.aes_log, f"  Salida: {output_file}")
                self.update_status("Archivo descifrado exitosamente")
                messagebox.showinfo("Éxito", f"Archivo descifrado guardado en:\n{output_file}")
            else:
                messagebox.showerror("Error", "Error en el descifrado. Verifica la clave.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al descifrar: {e}")
    
    def encrypt_aes_text(self):
        """Cifrar texto directo con AES"""
        if not self.aes_key:
            messagebox.showwarning("Advertencia", "Primero genera una clave AES")
            return
        
        # Obtener texto
        texto = self.aes_text_input.get("1.0", tk.END).strip()
        if not texto:
            messagebox.showwarning("Advertencia", "Ingresa un texto para cifrar")
            return
        
        try:
            # Cifrar
            plaintext = texto.encode('utf-8')
            nonce, ciphertext, tag = encrypt_gcm(plaintext, self.aes_key)
            
            # Combinar y convertir a hex para mostrar
            encrypted_data = nonce + tag + ciphertext
            encrypted_hex = encrypted_data.hex()
            
            # Mostrar resultado
            self.aes_text_output.delete("1.0", tk.END)
            self.aes_text_output.insert("1.0", encrypted_hex)
            
            self.log_message(self.aes_log, f"\n✓ Texto cifrado exitosamente")
            self.log_message(self.aes_log, f"  Longitud original: {len(plaintext)} bytes")
            self.log_message(self.aes_log, f"  Longitud cifrada: {len(encrypted_data)} bytes")
            self.log_message(self.aes_log, f"  Formato: HEX (copia el resultado de arriba)")
            
            self.update_status("Texto cifrado exitosamente")
        except Exception as e:
            messagebox.showerror("Error", f"Error al cifrar texto: {e}")
    
    def decrypt_aes_text(self):
        """Descifrar texto directo con AES"""
        if not self.aes_key:
            messagebox.showwarning("Advertencia", "Primero genera o carga una clave AES")
            return
        
        # Obtener texto cifrado (en hex)
        encrypted_hex = self.aes_text_input.get("1.0", tk.END).strip()
        if not encrypted_hex:
            messagebox.showwarning("Advertencia", "Ingresa un texto cifrado para descifrar")
            return
        
        try:
            # Convertir de hex a bytes
            encrypted_data = bytes.fromhex(encrypted_hex)
            
            # Extraer componentes
            nonce = encrypted_data[:12]
            tag = encrypted_data[12:28]
            ciphertext = encrypted_data[28:]
            
            # Descifrar
            plaintext = decrypt_gcm(nonce, ciphertext, tag, self.aes_key)
            decrypted_text = plaintext.decode('utf-8')
            
            # Mostrar resultado
            self.aes_text_output.delete("1.0", tk.END)
            self.aes_text_output.insert("1.0", decrypted_text)
            
            self.log_message(self.aes_log, f"\n✓ Texto descifrado exitosamente")
            self.log_message(self.aes_log, f"  Longitud cifrada: {len(encrypted_data)} bytes")
            self.log_message(self.aes_log, f"  Longitud descifrada: {len(plaintext)} bytes")
            
            self.update_status("Texto descifrado exitosamente")
        except ValueError as e:
            messagebox.showerror("Error", "Error de autenticación. La clave es incorrecta o el texto fue modificado.")
            self.log_message(self.aes_log, f"\n✗ Error de autenticación", color='#e74c3c')
        except Exception as e:
            messagebox.showerror("Error", f"Error al descifrar texto: {e}")
    
    # --- RSA ---
    def generate_rsa_keys(self):
        """Generar par de claves RSA"""
        try:
            self.update_status("Generando claves RSA-2048...")
            priv, pub = generate_rsa_keypair(2048)
            self.rsa_private_key = priv
            self.rsa_public_key = pub
            
            self.rsa_key_label.config(text="✓ Claves RSA-2048 generadas exitosamente", 
                                     foreground='#2ecc71')
            
            self.rsa_log.delete(1.0, tk.END)
            self.log_message(self.rsa_log, "✓ Par de claves RSA-2048 generado")
            self.log_message(self.rsa_log, "\n--- CLAVE PRIVADA ---")
            self.log_message(self.rsa_log, priv.decode()[:200] + "...")
            self.log_message(self.rsa_log, "\n--- CLAVE PÚBLICA ---")
            self.log_message(self.rsa_log, pub.decode())
            self.log_message(self.rsa_log, "\n⚠️ Guarda la clave privada de forma segura")
            
            self.update_status("Claves RSA generadas")
        except Exception as e:
            messagebox.showerror("Error", f"Error al generar claves: {e}")
            
    def save_private_key(self):
        """Guardar clave privada"""
        if not self.rsa_private_key:
            messagebox.showwarning("Advertencia", "Primero genera las claves RSA")
            return
            
        filename = filedialog.asksaveasfilename(defaultextension=".pem",
                                               filetypes=[("PEM files", "*.pem")])
        if filename:
            with open(filename, "wb") as f:
                f.write(self.rsa_private_key)
            messagebox.showinfo("Éxito", f"Clave privada guardada en:\n{filename}")
            
    def save_public_key(self):
        """Guardar clave pública"""
        if not self.rsa_public_key:
            messagebox.showwarning("Advertencia", "Primero genera las claves RSA")
            return
            
        filename = filedialog.asksaveasfilename(defaultextension=".pem",
                                               filetypes=[("PEM files", "*.pem")])
        if filename:
            with open(filename, "wb") as f:
                f.write(self.rsa_public_key)
            messagebox.showinfo("Éxito", f"Clave pública guardada en:\n{filename}")
            
    def load_private_key(self):
        """Cargar clave privada"""
        filename = filedialog.askopenfilename(filetypes=[("PEM files", "*.pem")])
        if filename:
            with open(filename, "rb") as f:
                self.rsa_private_key = f.read()
            self.log_message(self.rsa_log, f"\n✓ Clave privada cargada desde: {filename}")
            messagebox.showinfo("Éxito", "Clave privada cargada")
            
    def load_public_key(self):
        """Cargar clave pública"""
        filename = filedialog.askopenfilename(filetypes=[("PEM files", "*.pem")])
        if filename:
            with open(filename, "rb") as f:
                self.rsa_public_key = f.read()
            self.log_message(self.rsa_log, f"\n✓ Clave pública cargada desde: {filename}")
            messagebox.showinfo("Éxito", "Clave pública cargada")
    
    # --- Firma Digital ---
    def sign_document(self):
        """Firmar documento"""
        if not self.rsa_private_key:
            messagebox.showwarning("Advertencia", "Primero genera o carga una clave privada")
            return
            
        document = self.sign_text.get(1.0, tk.END).strip()
        if not document:
            messagebox.showwarning("Advertencia", "Escribe un documento para firmar")
            return
            
        try:
            priv_key = load_private_key(self.rsa_private_key)
            signature = sign_message(document.encode(), priv_key)
            
            self.signature_log.delete(1.0, tk.END)
            self.log_message(self.signature_log, "✓ Documento firmado exitosamente")
            self.log_message(self.signature_log, f"\nDocumento:\n{document}")
            self.log_message(self.signature_log, f"\nFirma (hex):\n{signature.hex()}")
            self.log_message(self.signature_log, f"\nFirma (base64):\n{signature.hex()[:100]}...")
            
            # Copiar firma al campo de verificación
            self.signature_entry.delete(0, tk.END)
            self.signature_entry.insert(0, signature.hex())
            
            self.update_status("Documento firmado")
            messagebox.showinfo("Éxito", "Documento firmado. La firma se copió al campo de verificación.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al firmar: {e}")
            
    def verify_signature_gui(self):
        """Verificar firma digital"""
        if not self.rsa_public_key:
            messagebox.showwarning("Advertencia", "Primero genera o carga una clave pública")
            return
            
        document = self.verify_text.get(1.0, tk.END).strip()
        signature_hex = self.signature_entry.get().strip()
        
        if not document or not signature_hex:
            messagebox.showwarning("Advertencia", "Proporciona el documento y la firma")
            return
            
        try:
            pub_key = load_public_key(self.rsa_public_key)
            signature = bytes.fromhex(signature_hex)
            is_valid = verify_signature(document.encode(), signature, pub_key)
            
            self.signature_log.delete(1.0, tk.END)
            if is_valid:
                self.log_message(self.signature_log, "✅ FIRMA VÁLIDA")
                self.log_message(self.signature_log, "\n• El documento NO ha sido modificado")
                self.log_message(self.signature_log, "• La firma es auténtica")
                self.log_message(self.signature_log, "• El firmante es quien dice ser")
                messagebox.showinfo("Verificación", "✅ Firma Válida\n\nEl documento es auténtico.")
            else:
                self.log_message(self.signature_log, "❌ FIRMA INVÁLIDA", '#e74c3c')
                self.log_message(self.signature_log, "\n⚠️ El documento fue modificado o la firma no es auténtica")
                messagebox.showwarning("Verificación", "❌ Firma Inválida\n\nEl documento fue modificado o la firma no es auténtica.")
                
            self.update_status("Verificación completada")
        except Exception as e:
            messagebox.showerror("Error", f"Error al verificar: {e}")
    
    # --- Hash e Integridad ---
    def calculate_hash(self):
        """Calcular hash de archivo"""
        file_path = self.hash_file.get()
        if not file_path or not os.path.exists(file_path):
            messagebox.showwarning("Advertencia", "Selecciona un archivo válido")
            return
            
        try:
            file_hash = calculate_file_hash(file_path)
            self.hash_log.delete(1.0, tk.END)
            self.log_message(self.hash_log, f"✓ Hash calculado exitosamente")
            self.log_message(self.hash_log, f"\nArchivo: {file_path}")
            self.log_message(self.hash_log, f"Tamaño: {os.path.getsize(file_path)} bytes")
            self.log_message(self.hash_log, f"\nSHA-256:\n{file_hash}")
            self.update_status("Hash calculado")
        except Exception as e:
            messagebox.showerror("Error", f"Error al calcular hash: {e}")
            
    def register_file_gui(self):
        """Registrar archivo en base de datos de integridad"""
        file_path = self.hash_file.get()
        if not file_path or not os.path.exists(file_path):
            messagebox.showwarning("Advertencia", "Selecciona un archivo válido")
            return
            
        try:
            file_hash = register_file(file_path, "integrity_db.json")
            self.log_message(self.hash_log, f"\n✓ Archivo registrado en base de datos")
            self.log_message(self.hash_log, f"  Archivo: {file_path}")
            self.log_message(self.hash_log, f"  Hash: {file_hash}")
            self.update_status("Archivo registrado")
            messagebox.showinfo("Éxito", "Archivo registrado en la base de datos de integridad")
        except Exception as e:
            messagebox.showerror("Error", f"Error al registrar: {e}")
            
    def verify_integrity(self):
        """Verificar integridad de archivo"""
        file_path = self.hash_file.get()
        if not file_path or not os.path.exists(file_path):
            messagebox.showwarning("Advertencia", "Selecciona un archivo válido")
            return
            
        try:
            result = verify_file_integrity(file_path, "integrity_db.json")
            self.hash_log.delete(1.0, tk.END)
            
            if result['valid']:
                self.log_message(self.hash_log, "✅ INTEGRIDAD VERIFICADA")
            else:
                self.log_message(self.hash_log, "❌ INTEGRIDAD COMPROMETIDA", '#e74c3c')
                
            self.log_message(self.hash_log, f"\n{result['message']}")
            self.log_message(self.hash_log, f"\nArchivo: {file_path}")
            if result['original_hash']:
                self.log_message(self.hash_log, f"Hash original:  {result['original_hash']}")
                self.log_message(self.hash_log, f"Hash actual:    {result['current_hash']}")
                self.log_message(self.hash_log, f"Registrado:     {result['registered_date']}")
            
            self.update_status("Verificación completada")
            
            if result['valid']:
                messagebox.showinfo("Verificación", "✅ Integridad Verificada\n\nEl archivo NO ha sido modificado.")
            else:
                messagebox.showwarning("Verificación", "❌ Integridad Comprometida\n\nEl archivo fue modificado.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al verificar: {e}")
            
    def verify_all(self):
        """Verificar todos los archivos registrados"""
        try:
            results = verify_all_files("integrity_db.json")
            self.hash_log.delete(1.0, tk.END)
            self.log_message(self.hash_log, "📊 VERIFICACIÓN DE TODOS LOS ARCHIVOS\n")
            
            valid_count = 0
            invalid_count = 0
            
            for res in results:
                if res['valid']:
                    self.log_message(self.hash_log, f"✅ {res['filepath']}")
                    valid_count += 1
                else:
                    self.log_message(self.hash_log, f"❌ {res['filepath']}", '#e74c3c')
                    invalid_count += 1
                self.log_message(self.hash_log, f"   {res['message']}\n")
            
            self.log_message(self.hash_log, f"\n═══════════════════════════")
            self.log_message(self.hash_log, f"Total verificados: {len(results)}")
            self.log_message(self.hash_log, f"Válidos: {valid_count}")
            self.log_message(self.hash_log, f"Modificados: {invalid_count}")
            
            self.update_status(f"Verificados: {valid_count} OK, {invalid_count} modificados")
        except Exception as e:
            messagebox.showerror("Error", f"Error al verificar: {e}")
    
    # --- Híbrido ---
    def encrypt_hybrid(self):
        """Cifrar con esquema híbrido"""
        if not self.rsa_public_key:
            messagebox.showwarning("Advertencia", "Primero genera o carga una clave pública RSA")
            return
            
        input_file = self.hybrid_input.get()
        if not input_file or not os.path.exists(input_file):
            messagebox.showwarning("Advertencia", "Selecciona un archivo válido")
            return
            
        try:
            # Leer archivo
            with open(input_file, "rb") as f:
                plaintext = f.read()
            
            # Cifrar con esquema híbrido
            enc_key, nonce, tag, ciphertext = encrypt_file_hybrid(plaintext, self.rsa_public_key)
            
            # Guardar paquete completo
            output_file = input_file + ".hybrid"
            with open(output_file, "wb") as f:
                # Formato: [len_enc_key][enc_key][nonce][tag][ciphertext]
                f.write(len(enc_key).to_bytes(4, 'big'))
                f.write(enc_key)
                f.write(nonce)
                f.write(tag)
                f.write(ciphertext)
            
            self.log_message(self.hybrid_log, "✓ Archivo cifrado con esquema híbrido")
            self.log_message(self.hybrid_log, f"\n  Archivo original: {input_file}")
            self.log_message(self.hybrid_log, f"  Tamaño original: {len(plaintext)} bytes")
            self.log_message(self.hybrid_log, f"  Archivo cifrado: {output_file}")
            self.log_message(self.hybrid_log, f"  Tamaño cifrado: {os.path.getsize(output_file)} bytes")
            self.log_message(self.hybrid_log, f"\n  Clave AES cifrada: {len(enc_key)} bytes")
            self.log_message(self.hybrid_log, f"  Datos cifrados: {len(ciphertext)} bytes")
            
            self.update_status("Cifrado híbrido completado")
            messagebox.showinfo("Éxito", f"Archivo cifrado guardado en:\n{output_file}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al cifrar: {e}")
            
    def decrypt_hybrid(self):
        """Descifrar con esquema híbrido"""
        if not self.rsa_private_key:
            messagebox.showwarning("Advertencia", "Primero genera o carga una clave privada RSA")
            return
            
        encrypted_file = self.hybrid_encrypted.get()
        if not encrypted_file or not os.path.exists(encrypted_file):
            messagebox.showwarning("Advertencia", "Selecciona un archivo válido")
            return
            
        try:
            # Leer paquete
            with open(encrypted_file, "rb") as f:
                enc_key_len = int.from_bytes(f.read(4), 'big')
                enc_key = f.read(enc_key_len)
                nonce = f.read(12)
                tag = f.read(16)
                ciphertext = f.read()
            
            # Descifrar
            plaintext = decrypt_file_hybrid(enc_key, nonce, tag, ciphertext, self.rsa_private_key)
            
            # Guardar archivo descifrado
            output_file = encrypted_file.replace(".hybrid", "_decrypted.txt")
            with open(output_file, "wb") as f:
                f.write(plaintext)
            
            self.log_message(self.hybrid_log, "\n✓ Archivo descifrado con esquema híbrido")
            self.log_message(self.hybrid_log, f"\n  Archivo cifrado: {encrypted_file}")
            self.log_message(self.hybrid_log, f"  Archivo descifrado: {output_file}")
            self.log_message(self.hybrid_log, f"  Tamaño recuperado: {len(plaintext)} bytes")
            
            self.update_status("Descifrado híbrido completado")
            messagebox.showinfo("Éxito", f"Archivo descifrado guardado en:\n{output_file}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al descifrar: {e}")


def main():
    root = tk.Tk()
    app = CryptoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
