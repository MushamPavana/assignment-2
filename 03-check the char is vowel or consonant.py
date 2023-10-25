##python program to check given character is vowel or consonant.

char = input("Enter the alphabet: ")

if char in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
    print(char, "is a vowel")
else:
    print(char, "is a consonant")
