from pwdlib import PasswordHash

hashed_password=PasswordHash.recommended()

def hash_password(password):
    return hashed_password.hash(password)


def verify_password(password,hash_password):
    return hashed_password.verify(password, hash_password)



