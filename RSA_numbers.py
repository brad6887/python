"""When a credit card number is sent through the Internet it must 
be protected so that other people cannot see it. Many web browsers use
a protection based on "RSA Numbers."

A number is an RSA number if it has exactly four divisors. In other
words, there are exactly four numbers that divide into it evenly.
For example, 10 is an RSA number because it has exactly four divisors 1, 
2, 5, 10. 12 is not an RSA number because it has too many divisors 
1, 2, 3 4, 5, 12. 11 is not an RSA number either. There is only one 
RSA number in the range 10 ... 12.

Write a program that inputs a range of numbers and then counts how
many numbers from that range are RSA numbers. You may assume that
the numbers in the range are less than 1000.
    """

low = int(input())
high = int(input())

test = low
RSA = 0
while test <= high:
    score = 0
    for i in range(1, high + 1):
        if test % i == 0:
            score += 1
    if score == 4:
        RSA += 1
                
    test += 1
    
print(f'The number of RSA numbers between {low} and {high} is {RSA}')