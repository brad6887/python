"""Natalie is learning to count on her fingers. When her Daddy tells her
a number  (), she asks "What is , Daddy?", by which she means "How many
fingers should I hold up on each hand so that the total is ?"

To make matters simple, her Daddy gives her the correct finger
representation according to the following rules:

    the number may be represented on one or two hands;
    if the number is represented on two hands, the larger number
    is given first.
    
For example, if Natalie asks "What is 4, Daddy?", her Dad may reply:

4 is 4.
4 is 3 and 1.
4 is 2 and 2.
Your job is to make sure that Natalie's Daddy gives the correct number
of answers.

Input Specification
The input will be a single integer i such that 1 <= i <= 10.

Output Specification
The output is the number of ways of producing that number on two hands,
subject to the rules outlined above."""

num = 4
score = 0
hand1 = 1


while hand1 <= 5:
    hand2 = 0
    for hand2 in range(0, num):
        print(hand1, hand2)
        if hand1 + hand2 == num:
            score +=1
            print(score)
            hand2 += 1
    hand1 += 1
print(score)
        

# for hand1 in range(1, num + 1):
    
    
    
    
#     for hand2 in range(hand1):
#         print(hand1, hand2)
#         if hand1 + hand2 == num:
#             score += 1
# print('score', score)
    