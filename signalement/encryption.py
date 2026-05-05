import os
import json
import hashlib
from cryptography.fernet import Fernet
from django.conf import settings


def get_or_create_key():
    key_path = settings.ENCRYPTION_KEY_PATH
    if os.path.exists(key_path):
        with open(key_path, 'rb') as f:
            return f.read()
    key = Fernet.generate_key()
    with open(key_path, 'wb') as f:
        f.write(key)
    return key


def chiffrer(texte):
    f = Fernet(get_or_create_key())
    return f.encrypt(texte.encode()).decode()


def dechiffrer(texte_chiffre):
    f = Fernet(get_or_create_key())
    return f.decrypt(texte_chiffre.encode()).decode()


def calculer_checksum(texte):
    return hashlib.sha256(texte.encode()).hexdigest()


def sauvegarder_json(signalement_data, code_anonyme):
    json_dir = settings.BASE_DIR / 'signalements_json'
    os.makedirs(json_dir, exist_ok=True)
    filepath = json_dir / f"{code_anonyme}.json"
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(signalement_data, f, ensure_ascii=False, indent=2)