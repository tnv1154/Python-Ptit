"""# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""

def fix_score(score: str):

    # Tách phần nguyên và phần thập phân



# Các điểm cần xử lý
scores = ["78", "95", "710", "8"]

# Áp dụng hàm fix_score
fixed_scores = [fix_score(score) for score in scores]
print("Danh sách điểm sau khi sửa:", fixed_scores)