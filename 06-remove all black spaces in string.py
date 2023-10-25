###python program to remove all the blank spaces in a given string.

def remove_spaces(input_string):
    return input_string.replace(" ", "")

input_string = "Marolix Technology"
result = remove_spaces(input_string)
print(result)
