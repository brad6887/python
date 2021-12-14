"""COCI '16 Contest 1 #1 Tarifa

Pero has negotiated a Very Good data plan with his internet provider. The provider will let
Pero use up x megabytes to surf the internet per month. Each megabyte that he doesn't spend in
that month gets transferred to the next month and can still be spent. Of course, Pero can only
spend the megabytes he actually has.

If we know how many megabytes Pero has spent in each of the first  months of using the plan,
determine how many megabytes Pero will have available in the  month of using the plan.

Input Specification
The first line of input contains the integer  x.
The second line of input contains the integer n .
Each of the following  lines contains an integer p ,
the number of megabytes spent in each of the first  months of using the plan.
Numbers  will be such that Pero will never use more megabytes than he actually has.

Output Specification
The first and only line of output must contain the required value from the task."""

monthly_mb = int(input())
n = int(input())
excess = 0

for i in range(n):
    used = int(input())
    excess = excess + monthly_mb - used

print(excess + monthly_mb)