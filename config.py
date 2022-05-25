import configparser
import os
import crypto

BASE_DIR = ''
config = configparser.ConfigParser()
path = os.path.join(BASE_DIR, 'settings.ini')
config.read(path)


def get(prefix, key, encrypted=False, fallback=None):
    try:
        res = config.get(prefix, key, fallback=fallback)
        return crypto.decrypt(res) if encrypted else res
    except:
        pass
