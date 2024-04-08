import random
import string

def gen_pass(length: int = 16):
    alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for i in range(length))
    return password

password = gen_pass()
print(f"Generated Password: {password}")