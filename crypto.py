from cryptography.fernet import Fernet

key = "NPy-S7eZ9NHx7_oSjoh_qf_k8KFh0tiwd2jKo7j_Mw4="


def new_key():
    return Fernet.generate_key()


def encrypt(message):
    fernet = Fernet(key)
    return fernet.encrypt(message.encode()).decode('utf-8')


def decrypt(enc_message):
    fernet = Fernet(key)
    return fernet.decrypt(enc_message.encode()).decode()
