char = ""
emoji = {'CU': 'see you',
        ':-)': "I'm happy",
        ':-(': "I'm unhappy",
        ';-)': 'wink',
        ':-p': 'stick out my tongue',
        '(~.~)': 'sleepy',
        'TA': 'totally awesome',
        'CCC': 'Canadian Computing Competition',
        'CUZ': 'because',
        'TY': 'thank-you',
        "YW": "you're welcome",
        'TTYL': 'talk to you later'}

while char != 'TTYL':
    char = input()
    if char not in emoji:
        print(char)
    else:
        print(emoji[char])

