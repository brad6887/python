"""[summary]
    Moe Bull has a cell phone and after a month of use is trying to
    decide which price plan is the best for his usage pattern. He has
    two options, each plan has different costs for daytime minutes,
    evening minutes and weekend minutes.

Plan	Costs
daytime	evening	weekend
A	100 free minutes then 25 cents per minute
15 cents per minute
20 cents per minute
B	250 free minutes then 45 cents per minute
35 cents per minute
25 cents per minute
Write a program that will input the number of each type of minutes
and output the cheapest plan for this usage pattern, using the
format shown below. The input will be in the order of daytime
minutes, evening minutes and weekend minutes. In the case that the
two plans are the same price, output both plans.
"""

daytime = int(input())
evening = int(input())
weekend = int(input())

Plans = ('A', 'B')

for plan in Plans:
    if plan == 'A':
        if daytime >= 100:
            new_daytime = daytime - 100
        else:
            new_daytime = 0
        a_cost = (new_daytime * .25) + (evening * .15) + (weekend * .20)
        a_cost = round(a_cost,2)
        print(f"Plan A costs {a_cost}")
    elif plan == 'B':
        if daytime >= 250:
            new_daytime = daytime - 250
        else:
            new_daytime = 0
        b_cost = (new_daytime * .45) + (evening * .35) + (weekend * .25)
        b_cost = round(b_cost,2)
        print(f"Plan B costs {b_cost}")



if a_cost == b_cost:
    print('Plan A and B are the same price.')
elif a_cost < b_cost:
    print('Plan A is the cheapest.')
elif b_cost < a_cost:
    print('Plan B is the cheapest.')
    

