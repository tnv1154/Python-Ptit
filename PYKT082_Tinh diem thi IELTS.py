# Hàm chuyển đổi số câu đúng thành band score cho Reading và Listening
import math


def convert_score(correct_answers):
    if 39 <= correct_answers <= 40:
        return 9.0
    elif 37 <= correct_answers <= 38:
        return 8.5
    elif 35 <= correct_answers <= 36:
        return 8.0
    elif 33 <= correct_answers <= 34:
        return 7.5
    elif 30 <= correct_answers <= 32:
        return 7.0
    elif 27 <= correct_answers <= 29:
        return 6.5
    elif 23 <= correct_answers <= 26:
        return 6.0
    elif 20 <= correct_answers <= 22:
        return 5.5
    elif 16 <= correct_answers <= 19:
        return 5.0
    elif 13 <= correct_answers <= 15:
        return 4.5
    elif 10 <= correct_answers <= 12:
        return 4.0
    elif 7 <= correct_answers <= 9:
        return 3.5
    elif 5 <= correct_answers <= 6:
        return 3.0
    elif 3 <= correct_answers <= 4:
        return 2.5
    else:
        return 0.0  # Nếu số câu đúng quá thấp



def main():
    for t in range(int(input())):
        r, l, s, w = map(float, input().split())
        read = convert_score(int(r))
        listen = convert_score(int(l))
        avr = (read + listen + s + w) / 4
        if avr - int(avr) >= 0.75:
            print(int(avr) + 1.0)
        elif avr - int(avr) >= 0.25:
            print(int(avr) + 0.5)
        else:
            print(int(avr))



if __name__ == "__main__":
    main()