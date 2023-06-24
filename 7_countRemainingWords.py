def countRemainingWords(sequence):
    stack = []
    for word in sequence:
        if stack and stack[-1] == word:
            stack.pop()
        else:
            stack.append(word)
    return len(stack)

# Example usage:
sequence = ["ab", "aa", "aa", "bcd", "ab"]
result = countRemainingWords(sequence)
print(result)  # Output: 3

sequence = ["tom", "jerry", "jerry", "tom"]
result = countRemainingWords(sequence)
print(result)  # Output: 0
