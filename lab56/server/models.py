from config import db, app
from argon2 import PasswordHasher
from sqlalchemy_utils import EncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import FernetEngine
from cryptography.fernet import Fernet
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa
import base64

DB_SALT = app.config.get('DB_SALT')
DB_ENCRYPTION_KEY = app.config.get('DB_ENCRYPTION_KEY')
pwd_hasher = PasswordHasher()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(64), index=True)
    password_hash = db.Column(EncryptedType(db.String, DB_ENCRYPTION_KEY, FernetEngine))
    first_name = db.Column(EncryptedType(db.String, DB_ENCRYPTION_KEY, FernetEngine))
    last_name = db.Column(EncryptedType(db.String, DB_ENCRYPTION_KEY, FernetEngine))
    email = db.Column(EncryptedType(db.String, DB_ENCRYPTION_KEY, FernetEngine))
    phone_number = db.Column(EncryptedType(db.String, DB_ENCRYPTION_KEY, FernetEngine))
    cipher_suite = Fernet(DB_ENCRYPTION_KEY)
   
    def __repr__(self):
        return '<Customer {}>'.format(self.first_name)

    def set_data(self, data):
        fields = ["first_name", "last_name", "email", "phone_number"]
        for field in fields:
            if field in data:
                binary = str.encode(data.get(field))
                field_data = User.cipher_suite.encrypt(binary)
                setattr(self, field, field_data.decode("utf8"))

    def get_field(self, field_name):
        result = getattr(self, field_name)
        if result:
            return User.cipher_suite.decrypt(bytes(result, encoding="utf8"))
        
    
    def hash_password(self, password):
        pass_hash = pwd_hasher.hash(DB_SALT + password)
        self.password_hash = User.cipher_suite.encrypt(bytes(pass_hash, "utf8")).decode("utf8")

    def verify_password(self, password):
        return pwd_hasher.verify(self.password_hash, DB_SALT + password)


