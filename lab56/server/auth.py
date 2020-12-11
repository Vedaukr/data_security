import jwt, datetime
from config import app

def decode_auth_token(auth_token):
    try:
        payload = jwt.decode(auth_token, app.config.get('SECRET_JWT_KEY'))
        return payload['sub']
    except jwt.ExpiredSignatureError:
        raise Exception('Signature expired. Please log in again.')
    except jwt.InvalidTokenError:
        raise Exception('Invalid token. Please log in again.')

def encode_auth_token(user_login):
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=5),
            'iat': datetime.datetime.utcnow(),
            'sub': user_login
        }
        return jwt.encode(
            payload,
            app.config.get('SECRET_JWT_KEY'),
            algorithm='HS256'
        ).decode('utf-8')
    except Exception as e:
        return e

