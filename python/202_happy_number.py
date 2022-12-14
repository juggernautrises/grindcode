# https://leetcode.com/problems/happy-number/
def get_digits(number):
    digits = []
    while number > 9:
        digit = number % 10
        digits.append(digit)

        number = number // 10
    if number:
        return [number] + digits


n = 100
res = get_digits(n)
print(res)
