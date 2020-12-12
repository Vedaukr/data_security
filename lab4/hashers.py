import hashlib, csv
import secrets
from base64 import b64encode
import bcrypt

class Hasher:
    PASSWORDS_AMOUNT = 100000
    def __init__(self, path, get_password):
        self.path = path
        self.get_password = get_password

    def export(self):
        with open(self.path, 'w') as csvfile:
            writer = csv.writer(csvfile)
            for _ in range(self.PASSWORDS_AMOUNT):
                hash_row = self.get_hash()
                writer.writerow(hash_row)

    def get_hash(self):
        pass
        
class MD5Hasher(Hasher):
    def get_hash(self):
        pwd = bytes(self.get_password(), encoding='utf8')
        return [b64encode(hashlib.md5(pwd).digest()).decode()]

class SHA1Hasher(Hasher):
    def get_hash(self):
        salt = secrets.token_hex(8)
        pwd = bytes(self.get_password() + salt, encoding='utf8')
        return b64encode(hashlib.sha1(pwd).digest()).decode(), salt

class BcryptHasher(Hasher):
    def get_hash(self):
        salt = bcrypt.gensalt(log_rounds=7)
        return [bcrypt.hashpw(self.get_password(), salt)]