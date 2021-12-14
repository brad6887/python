notes = input()

measures = notes.split('|')

Amin = 0
Cmaj = 0
key = ''
end = ''
for i in measures:
    if (i[0] == "C")or (i[0] == "F") or (i[0] == 'G'):
        Cmaj += 1
    if (i[0] == 'A') or (i[0] == 'D') or (i[0] == 'E'):
        Amin += 1
if Cmaj > Amin:
    key = 'C-dur'
elif Amin > Cmaj:
    key = 'A-mol'
else:
    if Cmaj == Amin:
        end = (notes[-1])
        if end == 'C':
            key = 'C-dur'
        if end == 'A':
            key = 'A-mol'

print(key)