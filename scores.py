apple3 = int(input())
apple2 = int(input())
apple1 = int(input())
banan3 = int(input())
banan2 = int(input())
banan1 = int(input())
apple_score = (apple3 * 3) + (apple2 * 2) + (apple1)
banan_score = (banan3 * 3) + (banan2 *2)  + (banan1)
if apple_score == banan_score:
    print('T')
elif apple_score > banan_score:
    print('A')
else:
    print('B')