def zodiac_sign(day, month):
    if (month == 3 and 21 <= day <= 31) or (month == 4 and 1 <= day <= 19):
        return "Bach Duong"
    elif (month == 4 and 20 <= day <= 30) or (month == 5 and 1 <= day <= 20):
        return "Kim Nguu"
    elif (month == 5 and 21 <= day <= 31) or (month == 6 and 1 <= day <= 20):
        return "Song Tu"
    elif (month == 6 and 21 <= day <= 30) or (month == 7 and 1 <= day <= 22):
        return "Cu Giai"
    elif (month == 7 and 23 <= day <= 31) or (month == 8 and 1 <= day <= 22):
        return "Su Tu"
    elif (month == 8 and 23 <= day <= 31) or (month == 9 and 1 <= day <= 22):
        return "Xu Nu"
    elif (month == 9 and 23 <= day <= 30) or (month == 10 and 1 <= day <= 22):
        return "Thien Binh"
    elif (month == 10 and 23 <= day <= 31) or (month == 11 and 1 <= day <= 22):
        return "Thien Yet"
    elif (month == 11 and 23 <= day <= 30) or (month == 12 and 1 <= day <= 21):
        return "Nhan Ma"
    elif (month == 12 and 22 <= day <= 31) or (month == 1 and 1 <= day <= 19):
        return "Ma Ket"
    elif (month == 1 and 20 <= day <= 31) or (month == 2 and 1 <= day <= 18):
        return "Bao Binh"
    elif (month == 2 and 19 <= day <= 29) or (month == 3 and 1 <= day <= 20):
        return "Song Ngu"
    else:
        return "Ngày tháng không hợp lệ"

for i in range(int(input())):
    day , month = map(int, input().split())
    sign = zodiac_sign(day, month)
    print(sign)
