import bcrypt
import os
from datetime import datetime
import random


def password_generator(password: str = '') -> str:  

    if "".__eq__(password):
        password = datetime.now().strftime('%Y%m%d')
    
    rounds = int(os.environ.get('SALT', 10))
    return password, bcrypt.hashpw(str(password).encode("utf-8"), bcrypt.gensalt(rounds))

def password_compare(password: str, encrypt: str) -> bool:
    return bcrypt.checkpw(password.encode('utf8'), encrypt.encode('utf8'))

def shuffle(word: str = '') -> str:
    return "".join(random.sample(word, len(word)))
