#WAP to find the sum of a number until it becomes a single digit. (example: 9875 → 29→ 11→ 2)
print("Enter a number:")
num = int(input())
while num >= 10:
    sum_of_digits = 0
    while num > 0:
        sum_of_digits += num % 10
        num //= 10
    num = sum_of_digits
print("The single digit sum is:", num)