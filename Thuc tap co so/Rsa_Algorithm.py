import sympy
import Big_Interger_Library as big

def generate_keys(p, q):
    n = big.multiply(p, q)
    phi = big.multiply(p-1, q-1)

    e = 65537
    d = big.mod_reverse(e, phi)
    return (e, n), (d, n)

def encrypt(text, public_key):
    e, n = public_key
    cipher = [big.mod_pow(ord(ch), e, n) for ch in text]
    return cipher

def decrypt(ciphertext, private_key):
    d, n = private_key
    plain = [chr(big.mod_pow(c, d, n)) for c in ciphertext]
    return ''.join(plain)

if __name__ == "__main__":
    message = "I am B22DCAT288"

    p = sympy.randprime(2**1023, 2**1024)
    q = sympy.randprime(2**1023, 2**1024)
    public_key, private_key = generate_keys(p, q)

    print("Khóa công khai:", public_key)
    print("Khóa bí mật:", private_key)
    print("Bản rõ:", message)
    encrypted = encrypt(message, public_key)
    display_encrypted = "".join(str(c) for c in encrypted)
    print("Bản mã:", display_encrypted)

    decrypted = decrypt(encrypted, private_key)
    print("Giải mã:", decrypted)
