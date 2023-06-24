def reverseNumber(num):
    num_str = str(num)
    stack = []
    reversed_num_str = ""

    for char in num_str:
        stack.append(char)

    while stack:
        reversed_num_str += stack.pop()

    reversed_num = int(reversed_num_str)
    return reversed_num

num1 = 365
print(reverseNumber(num1))
# Output: 563

num2 = 6899
print(reverseNumber(num2))
# Output: 9986
