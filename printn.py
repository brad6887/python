"""Without using any string methods, try to print the following:

Note that "" represents the consecutive values in between.

Example

Print the string .

Input Format

The first line contains an integer .

Constraints
1 <= n <= 150

Output Format
Print the list of integers from  through  as a string, without spaces."""

from __future__ import print_function

if __name__ == '__main__':
    raw_input = input()
    n = int(raw_input())
    for i in range(1, n):
        print(i)