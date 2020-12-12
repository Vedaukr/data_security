# Lab5
Backend was written using Flask.  
Db schema - sqlite, ORM used - SQLAlchemy.  
User can register and authorize, authentication is implemented using JWT tokens with secret JWT_KEY which is stored in secure place.  
Passwords are hashed using SHA1 on client side, then on the server side it is concatinated with secret DB_SALT which is stored in secure place (not in db obviously) and after that 
hashed using argon2.  

Also added we've added some restrictions on user passwords such as:

Password must contain at least 8 characters and:  
1. at least one lowercase letter  
2. at least one uppercase letter  
3. at least one digit  
4. at least one of special symbols ($@#&!)  

Password length may be as big as user wants.

# Lab 6
For database encryption EncryptedType from SQLAlchemy-utils was used with Fernet encryption engine which is using AES256 to encrypt data.  
DB_ENCRYPTION_KEY should be stored in the safe place (KMS for instance). If database will be stolen without key it is pretty impossible to encrypt db data.  
