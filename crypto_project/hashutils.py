# hashutils.py
from Crypto.Hash import SHA256
import json
import os
from datetime import datetime

def sha256_bytes(data: bytes) -> bytes:
    h = SHA256.new(data=data)
    return h.digest()

def sha256_hex(data: bytes) -> str:
    h = SHA256.new(data=data)
    return h.hexdigest()

# ========== VERIFICACIÓN DE INTEGRIDAD DE ARCHIVOS ==========

def calculate_file_hash(filepath: str) -> str:
    """
    Calcula el hash SHA-256 de un archivo.
    
    Args:
        filepath: Ruta del archivo
    
    Returns:
        str: Hash hexadecimal del archivo
    """
    sha256 = SHA256.new()
    
    try:
        with open(filepath, 'rb') as f:
            # Leer en bloques para archivos grandes
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        raise FileNotFoundError(f"Archivo no encontrado: {filepath}")
    except Exception as e:
        raise Exception(f"Error al calcular hash: {e}")

def save_hash_database(db_file: str, hash_db: dict):
    """
    Guarda la base de datos de hashes en formato JSON.
    
    Args:
        db_file: Ruta del archivo de base de datos
        hash_db: Diccionario con hashes {filepath: {hash, timestamp}}
    """
    with open(db_file, 'w') as f:
        json.dump(hash_db, f, indent=2)

def load_hash_database(db_file: str) -> dict:
    """
    Carga la base de datos de hashes desde un archivo JSON.
    
    Args:
        db_file: Ruta del archivo de base de datos
    
    Returns:
        dict: Base de datos de hashes
    """
    if not os.path.exists(db_file):
        return {}
    
    with open(db_file, 'r') as f:
        return json.load(f)

def register_file(filepath: str, db_file: str = "hash_database.json"):
    """
    Registra un archivo en la base de datos de hashes.
    
    Args:
        filepath: Ruta del archivo a registrar
        db_file: Ruta de la base de datos
    
    Returns:
        str: Hash del archivo registrado
    """
    file_hash = calculate_file_hash(filepath)
    hash_db = load_hash_database(db_file)
    
    hash_db[filepath] = {
        "hash": file_hash,
        "timestamp": datetime.now().isoformat(),
        "size": os.path.getsize(filepath)
    }
    
    save_hash_database(db_file, hash_db)
    return file_hash

def verify_file_integrity(filepath: str, db_file: str = "hash_database.json") -> dict:
    """
    Verifica si un archivo ha sido modificado comparando con el hash registrado.
    
    Args:
        filepath: Ruta del archivo a verificar
        db_file: Ruta de la base de datos
    
    Returns:
        dict: {
            "valid": bool,
            "message": str,
            "original_hash": str,
            "current_hash": str,
            "registered_date": str
        }
    """
    hash_db = load_hash_database(db_file)
    
    if filepath not in hash_db:
        return {
            "valid": False,
            "message": "Archivo no registrado en la base de datos",
            "original_hash": None,
            "current_hash": None,
            "registered_date": None
        }
    
    original_data = hash_db[filepath]
    original_hash = original_data["hash"]
    current_hash = calculate_file_hash(filepath)
    
    is_valid = original_hash == current_hash
    
    return {
        "valid": is_valid,
        "message": "Integridad verificada ✓" if is_valid else "⚠️ ARCHIVO MODIFICADO - Integridad comprometida",
        "original_hash": original_hash,
        "current_hash": current_hash,
        "registered_date": original_data["timestamp"]
    }

def verify_all_files(db_file: str = "hash_database.json") -> list:
    """
    Verifica la integridad de todos los archivos registrados.
    
    Args:
        db_file: Ruta de la base de datos
    
    Returns:
        list: Lista de resultados de verificación
    """
    hash_db = load_hash_database(db_file)
    results = []
    
    for filepath in hash_db.keys():
        if os.path.exists(filepath):
            result = verify_file_integrity(filepath, db_file)
            result["filepath"] = filepath
            results.append(result)
        else:
            results.append({
                "filepath": filepath,
                "valid": False,
                "message": "⚠️ Archivo no encontrado (eliminado o movido)",
                "original_hash": hash_db[filepath]["hash"],
                "current_hash": None,
                "registered_date": hash_db[filepath]["timestamp"]
            })
    
    return results

def compare_files(file1: str, file2: str) -> bool:
    """
    Compara dos archivos usando sus hashes SHA-256.
    
    Args:
        file1: Ruta del primer archivo
        file2: Ruta del segundo archivo
    
    Returns:
        bool: True si los archivos son idénticos
    """
    hash1 = calculate_file_hash(file1)
    hash2 = calculate_file_hash(file2)
    return hash1 == hash2
