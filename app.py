n = input()

for i in range(6):
    c = chr(i+97)
    print(c)
    if c not in n:
        print(c)
        break
