num = '42390'
odd_num = num[-1::-2]
even_num = num[-2::-2]

o_total = 0
e_total = 0
for i in even_num:
    result = 0
    result += int(i) * 2
    for digit in str(result):
        e_total += int(digit)
        print(e_total)
for j in odd_num:
    o_total += int(j)
    print(o_total)
final = o_total + e_total
print(final)
if final % 10 == 0:
    print('Valid')
else:
    print('Not valid')

