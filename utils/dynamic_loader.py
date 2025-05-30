# utils/dynamic_loader.py

import importlib.util
import sys
import uuid

def load_cipher_class(file_path):
    module_name = f"user_cipher_{uuid.uuid4().hex}"
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    user_module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = user_module
    spec.loader.exec_module(user_module)
    
    if hasattr(user_module, "CustomBlockCipher"):
        return user_module.CustomBlockCipher()
    else:
        raise ValueError("CustomBlockCipher class not found.")

