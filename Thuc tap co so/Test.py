import Big_Interger_Library as big

a = 123456789091234567891234
b = 923457901230567491231235
m = int(1e9 + 7)

print("Kiểm tra GCD và nghịch dảo modulo")
print(f"GCD({a},{b}) = {big.gcd(a,b)}")

try:
    reverse = big.mod_reverse(17, m)
    print(f"Nghịch dảo modulo của 17 mod {m} = {reverse}")
except Exception as e:
    print("Không có nghịch dảo modulo", e)