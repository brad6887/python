"""People who study epidemiology use models to analyze the spread of
disease. In this problem, we use a simple model.

When a person has a disease, they infect exactly  other people but
only on the very next day. No person is infected more than once. We
want to determine when a total of more than  people have had the disease.


Input Specification
There are three lines of input. Each line contains one positive integer.
The first line contains the value of P. The second line contains N,
the number of people who have the disease on Day 0. The third line
contains the value of R. Assume that P<10**7 and N <= P  and R <= 10 .

Output Specification
Output the number of the first day on which the total number of
people who have had the disease is greater than P."""

P = int(input())
N = int(input())
R = int(input())
I = N
D = 0

while I <= P:
    N = N * R
    I += N
    D += 1
print(D) 