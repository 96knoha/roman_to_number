import re

def roman_number():
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    while True:
        total = 0
        prev_value = 0

        roman = input("ローマ数字を入力してください（終了するには「exit」と入力）")

        if roman == 'exit':
            break

        pattern = r"^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

        if not re.match(pattern, roman):
            print("無効なローマ数字：ローマ数字には無効な文字が含まれています")
            continue

        for symbol in reversed(roman):
            value = roman_dict[symbol]
            if value >= prev_value:
                total += value
            else:
                total -= value
            prev_value = value

        print("対応する数値：", total)

roman_number()
