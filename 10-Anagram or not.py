### python program to check string is anagrams or not in Python.

string1 = "flow"
string2 = "wolf"
if sorted(string1) == sorted(string2):
    print("Anagrams")
else:
    print("Not Anagrams")
