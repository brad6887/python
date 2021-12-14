"""Americans spell differently from Canadians. Americans write neighbor and color
while Canadians write neighbour and colour. Write a program to help
Americans translate to Canadian.

Your program should interact with the user in the following way.
The user should type a word (not to exceed 64 letters) and if the word appears
to use American spelling, the program should echo the Canadian spelling for the
same word. If the word does not appear to use American spelling, it should be
output without change. When the user types quit! the program should terminate.

The rules for detecting American spelling are quite naive: 
If the word has more than four letters and has a suffix consisting of a consonant
followed by or, you may assume it is an American spelling, and that the equivalent
Canadian spelling replaces the or by our. 
Note: you should treat the letter y as a vowel."""

done = False

while not done:

    word = input()
    if word == 'quit!':
        done = True
    elif len(word) > 4 and not (word[-3] in 'aeiouy') and word[-2:] == 'or':
        print(word[:-2] + 'our')
    else:
        print(word)
