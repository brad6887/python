# With Dictionary
vowels = ['a', 'e', 'o', 'i', 'u']
word = input("Provied a word to search for vowels:")
found = []
for letter in word:
    if letter in vowels:
        found.append(letter)
for vowel in found:
    print(vowel)
