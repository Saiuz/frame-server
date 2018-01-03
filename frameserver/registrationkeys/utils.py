import random
import string

def generateKey():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
