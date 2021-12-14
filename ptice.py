"""Adrian, Bruno and Goran wanted to join the bird lovers' club.
However, they did not know that all applicants must pass an entrance
exam. The exam consists of N questions, each with three possible answers:
A, B and C.

Unfortunately, they couldn't tell a bird from a whale so they are trying
to guess the correct answers. Each of the three boys has a theory of
what set of answers will work best:

Adrian claims that the best sequence is: A, B, C...

Bruno is convinced that this is better: B A B C...

Goran laughs at them and will use this sequence: C, C, A, A, B, B ...

Write a program that, given the correct answers to the exam, determines
who of the three was right – whose sequence contains the most correct
answers.

Input Specification
The first line contains an integer N, the number of questions on the exam.
The second line contains a string of N letters A, B and C. These are,
in order, the correct answers to the questions in the exam.

Output Specification
On the first line, output , the largest number of correct answers
one of the three boys gets. After that, output the names of the boys
(in alphabetical order) whose sequences result in  correct answers."""

N = int(input())
Answers = (input())
Adrian = 'ABC'
Bruno = 'BABC'
Goran = 'CCAABB'
aScore = 0
bScore = 0
gScore = 0

# Adrian

for i in range(len(Answers)):
    if Answers[i] == Adrian[i % len(Adrian)]:
        aScore += 1
        
    if Answers[i] == Bruno[i % len(Bruno)]:
        bScore += 1

    if Answers[i] == Goran[i % len(Goran)]:
        gScore += 1
# print(aScore, bScore, gScore)        
    
win = 0
if aScore > win:
    win = aScore
if bScore > win:
    win = bScore
if gScore > win:
    win = gScore

print(win)
if aScore >= win:
    print('Adrian')
if bScore >= win:
    print('Bruno')
if gScore >= win:
    print('Goran')
