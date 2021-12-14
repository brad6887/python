k = int(input())
code = input().upper()
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
translated = ''

for i in range(len(code)):
    symbol = code[i]
    p = i + 1
    S = int(3 * p + k)
    if S >= len(SYMBOLS):
            S = S - len(SYMBOLS)    
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol) # Get the number of the symbol
        num = num - S
        translated = translated + SYMBOLS[num]
print(translated)

        