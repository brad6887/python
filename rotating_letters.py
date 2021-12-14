"""An artist wants to construct a sign whose letters will rotate freely
in the breeze. In order to do this, she must only use letters that are
not changed by rotation of 180 degrees: I, O, S, H, Z, X, and N.

Write a program that reads a word and determines whether the word can
be used on the sign.

Input Specification
The input will consist of one word, all in uppercase letters,
with no spaces. The maximum length of the word will be 30 letters, and
the word will have at least one letter in it.

Output Specification
Output YES if the input word can be used on the sign; otherwise,
output NO."""

word = input()
N = 0
Y = 0
letters = ['I', 'O', 'S', 'H', 'Z', 'X', 'N']
for i in word:
    if i not in letters:
        N = 1


if N >= 1:
    print('NO')
else:
    print('YES')
