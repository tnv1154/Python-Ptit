
def add(a,b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def mod(a, m):
    return a % m

def mod_pow(a, b, m):
    return pow(a, b, m)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_reverse(a, m):
    t, new_t = 0, 1
    r, new_r = m, a
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        raise Exception(f"Không tồn tại nghịch đảo mudulo của {a} mod {m}")
    if t < 0:
        t = t + m
    return t

