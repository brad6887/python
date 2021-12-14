# With Dictionary
vowels = set('aeiou')
word = input("Provied a word to search for vowels:")
found = vowels.intersection(set(word))
for vowel in found:
    print(vowel)
