import secrets as s
import hashlib as h

# MISC FUNCTION
def randomStr(x):
    dictionary = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_+=@[](),./#~!£$%^&*:;"
    string = ""
    for _ in range(x):
        string += s.choice(dictionary)
    return string

def gen_sha3512_hash(x): 
    obj = h.sha3_512()
    obj.update(x.encode())
    return str(obj.hexdigest())

def genShadow():
    x = randomStr(8092)
    shadow = gen_sha3512_hash(x)
    return shadow