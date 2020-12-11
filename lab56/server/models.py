from config import db, app
from argon2 import PasswordHasher

DB_SALT = app.config.get('DB_SALT')
pwd_hasher = PasswordHasher()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(64), index=True)
    password_hash = db.Column(db.String(64), index=True)
    first_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(64), index=True)
    phone_number = db.Column(db.String(64), index=True)

    def __repr__(self):
        return '<Customer {}>'.format(self.first_name)

    def to_obj(self):
        return {"Name": self.first_name, "Surname": self.last_name, "Login": self.login, "Email": self.email, "Phone": self.phone_number}

    def set_data(self, data):
        fields = ["first_name", "last_name", "email", "phone_number"]
        for field in fields:
            if field in data:
                setattr(self, field, data.get(field))

    def set_password(self, password):
        self.password_hash = pwd_hasher.hash(DB_SALT + password)

    def verify_password(self, password):
        return pwd_hasher.verify(self.password_hash, DB_SALT + password)


