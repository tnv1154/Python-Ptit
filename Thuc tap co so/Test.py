import Big_Interger_Library as bil

# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


# Tạo khóa RSA
def generate_rsa_keys():
    # Chọn hai số nguyên tố p và q
    p = 61  # Số nguyên tố thứ nhất
    q = 53  # Số nguyên tố thứ hai

    print(f"p = {p}, q = {q}")

    # Tính n = p * q
    n = bil.multiply(p, q)
    print(f"n = p * q = {n}")

    # Tính φ(n) = (p-1) * (q-1)
    phi_n = bil.multiply(bil.subtract(p, 1), bil.subtract(q, 1))
    print(f"φ(n) = (p-1) * (q-1) = {phi_n}")

    # Chọn e sao cho gcd(e, φ(n)) = 1
    e = 17  # Số mũ công khai thường dùng
    while bil.gcd(e, phi_n) != 1:
        e += 2
    print(f"e = {e}")

    # Tính d = e^(-1) mod φ(n)
    d = bil.mod_reverse(e, phi_n)
    print(f"d = {d}")

    print(f"\nKhóa công khai: (n = {n}, e = {e})")
    print(f"Khóa bí mật: (n = {n}, d = {d})")

    return (n, e, d)


# Chuyển chuỗi thành số
def string_to_numbers(text):
    numbers = []
    for char in text:
        numbers.append(ord(char))
    return numbers


# Chuyển số thành chuỗi
def numbers_to_string(numbers):
    text = ""
    for num in numbers:
        text += chr(num)
    return text


# Mã hóa RSA
def rsa_encrypt(message, n, e):
    print(f"\n--- MÃ HÓA ---")
    print(f"Thông điệp gốc: '{message}'")

    # Chuyển chuỗi thành mảng số ASCII
    numbers = string_to_numbers(message)
    print(f"Mã ASCII: {numbers}")

    # Mã hóa từng ký tự
    encrypted_numbers = []
    for i, num in enumerate(numbers):
        encrypted = bil.mod_pow(num, e, n)
        encrypted_numbers.append(encrypted)
        print(f"'{message[i]}' ({num}) -> {encrypted}")

    print(f"Thông điệp đã mã hóa: {encrypted_numbers}")
    return encrypted_numbers


# Giải mã RSA
def rsa_decrypt(encrypted_numbers, n, d):
    print(f"\n--- GIẢI MÃ ---")
    print(f"Thông điệp đã mã hóa: {encrypted_numbers}")

    # Giải mã từng số
    decrypted_numbers = []
    for encrypted in encrypted_numbers:
        decrypted = bil.mod_pow(encrypted, d, n)
        decrypted_numbers.append(decrypted)

    print(f"Mã ASCII sau giải mã: {decrypted_numbers}")

    # Chuyển về chuỗi
    decrypted_message = numbers_to_string(decrypted_numbers)
    print(f"Thông điệp gốc: '{decrypted_message}'")

    return decrypted_message


# Chương trình chính
def main():
    print("=== CHƯƠNG TRÌNH MÃ HÓA RSA ===\n")

    # Tạo khóa RSA
    n, e, d = generate_rsa_keys()

    # Thông điệp cần mã hóa (thay mã sinh viên của bạn vào đây)
    message = "I am SV001"  # Thay SV001 bằng mã sinh viên của bạn

    # Mã hóa
    encrypted = rsa_encrypt(message, n, e)

    # Giải mã
    decrypted = rsa_decrypt(encrypted, n, d)

    # Kiểm tra kết quả
    print(f"\n--- KẾT QUẢ ---")
    print(f"Thông điệp gốc:      '{message}'")
    print(f"Thông điệp giải mã:  '{decrypted}'")
    print(f"Kết quả đúng:        {message == decrypted}")


if __name__ == "__main__":
    main()