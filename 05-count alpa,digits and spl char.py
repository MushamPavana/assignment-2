###python program to count alphabets, digits, and special characters in the string.

def count_characters(string):
    alphabet_count = 0
    digit_count = 0
    special_count = 0

    for char in string:
        if char.isalpha():
            alphabet_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            special_count += 1

    return alphabet_count, digit_count, special_count

string = "Hello World 123!@#"
alphabet_count, digit_count, special_count = count_characters(string)

print("Alphabets:", alphabet_count)
print("Digits:", digit_count)
print("Special Characters:", special_count)
