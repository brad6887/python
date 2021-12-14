"""Canadian Computing Competition: 2011 Stage 1, Senior #1
You would like to do some experiments in natural language processing.
Natural language processing (NLP) involves using machines to recognize human languages.

Your first idea is to write a program that can distinguish English text from French text.

After some analysis, you have concluded that a very reasonable way of distinguishing these
two languages is to compare the occurrences of the letters t and T to the occurrences of the letters s and S. Specifically:

if the given text has more t and T characters than s and S characters, we will say that it is (probably) English text;
if the given text has more s and S characters than t and T characters, we will say that it is (probably) French text;
if the number of t and T characters is the same as the number of s and S characters, we will say that it is (probably) French text.

Input Specification
The input will contain the number  N followed by N lines of text, where each line has at least
one character and no more than 100 characters.

Output Specification
Your output will be one line. This line will either consist of the word English
(indicating the text is probably English) or French (indicating the text is probably French"""

lines = int(input())
eng = 0
fren = 0
position = 0

for n in range(lines):
    text = str(input().upper())
    for i in text:
        if i == "T":
            eng += 1
        if i == "S":
            fren +=1
        
if eng > fren:
    print('English')
else:
    print('French')