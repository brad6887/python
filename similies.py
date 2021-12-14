"""A simile is a combination of an adjective and noun that produces a
phrase such as "Easy as pie" or "Cold as ice".

Write a program to input n adjectives m nouns, and print out all
possible similes. The first two lines of input will provide the values
of m and n, in that order followed, one per line, by n adjectives and
m nouns.

Your program may output the similes in any order."""
adj_list = []
noun_list = []
num_adj = int(input())
num_noun = int(input())

for i in range(0, num_adj):
    adj = input()
    adj_list.append(adj)

for i in range(0, num_noun):
    noun = input()
    noun_list.append(noun)

for i in range(num_adj):
    for j in range(num_noun):
        print(f'{adj_list[i]} as {noun_list[j]}')
