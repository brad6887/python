"""The Archangel is being built! In order to build the Archangel, at
least 1 of a number of parts are required. In the following table, each
part is represented by an uppercase character.

Part Name	        Letter Used
Beam Weapons	    B
Frame (inclusive)	F
Thrusters	        T
Launch Pad	        L
Command Room	    C
However, you appear to be missing some parts. Can you figure out which?

Input Specification
The first line contains a string containing the identifiers of all 
the parts you have. The length of the string will be at least 1 and no
longer than 10.

Output Specification
The missing parts, each on a separate line and in any order.
If there are no missing parts, output NO MISSING PARTS."""

all = 'BFTLC'
parts = all.split()
on_hand = input()
missing = []

for part in all:
    if part not in on_hand:
        missing.append(part)
        
if not missing:
    print('NO MISSING PARTS')
else:
    print(''.join(missing))
