###python program to Remove Repeated Character from String.

def remove_repeated_characters(input_string):
    unique_chars = ""
    for char in input_string:
        if char not in unique_chars:
            unique_chars += char
    return unique_chars

input_string = "Marolix Technology"
result = remove_repeated_characters(input_string)
print("String with repeated characters removed:", result)
