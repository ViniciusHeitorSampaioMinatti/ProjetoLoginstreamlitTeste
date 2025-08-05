import json
import os

USUARIOS = "data/usuarios.json"

def load_usuarios():
    if os. path.exists(USUARIOS):
        with open(USUARIOS, "r", encoding="utf-8")as arq_json:
            return json.load(arq_json)
        
    else:
        return []
