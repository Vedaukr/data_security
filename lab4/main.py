from generators import *
from hashers import *
import random, time, hashlib, csv

TOP_1M_PASSWORDS_PATH = ".\\txt\\top1m_pass.txt" 
TOP_100_PASSWORDS_PATH = ".\\txt\\top1m_pass.txt" 
TOP_WORDS_PATH = ".\\txt\\top1m_pass.txt" 

generators = [
    TopPasswordsGenerator(TOP_1M_PASSWORDS_PATH),  
    TopPasswordsGenerator(TOP_100_PASSWORDS_PATH), 
    HumanLikeGenerator(TOP_WORDS_PATH), 
    RandomPasswordGenerator()
]

random.seed(time.time())

def get_password():
    return random.choices(generators, weights=[0.7, 0.1, 0.15, 0.05])[0].generate()

print(get_password())
print(get_password())
print(get_password())
print(get_password())
print(get_password())

MD5_PATH = '.\\hash_data\\md5.csv'
SHA1_PATH = '.\\hash_data\\sha1.csv'
BCRYPT_PATH = '.\\hash_data\\bcrypt.csv'

hashers = [
    MD5Hasher(MD5_PATH, get_password),
    SHA1Hasher(SHA1_PATH, get_password),
    BcryptHasher(BCRYPT_PATH, get_password)
]

for hasher in hashers:
    hasher.export()