
class ThiSinh:
    def __init__(self, ten, ns, mon1, mon2, mon3):
        self.ten = ThiSinh.chuanHoaTen(ten)
        self.ns = ThiSinh.chuanHoaNs(ns)
        self.tong = mon1 + mon2 + mon3

    @staticmethod
    def chuanHoaTen(ten):
        ten = ten.strip().lower()
        a = ten.split()
        ten_chuanHoa = ""
        for word in a:
            tmp = word[0].upper() + word[1:]
            ten_chuanHoa += tmp + " "
        return ten_chuanHoa.strip()

    @staticmethod
    def chuanHoaNs(ns):
        ns_chuanHoa = list(ns)
        if ns[1] == "/":
            ns_chuanHoa.insert(0, "0")
        if ns_chuanHoa[4] == "/":
            ns_chuanHoa.insert(3, "0")
        return "".join(ns_chuanHoa)

    def __str__(self):
        return f"{self.ten} {self.ns} {self.tong:.1f}"


a = ThiSinh(input(), input(), float(input()), float(input()), float(input()))
print(a)
