"""you have been asked to take a small icon that appears on the screen of a smart telephone and scale it up so it looks bigger on a regular computer screen.

The icon will be encoded as characters (x and *) in a  grid as follows:

Copy
*x*
 xx
* *
Write a program that accepts a positive integer scaling factor and outputs the scaled icon. A scaling factor of  means that each character is replaced by a  grid consisting only of that character.

Input Specification
The input will be a positive integer  such that .

Output Specification
The output will be  lines, which represent each individual line scaled by a factor of  and repeated  times. A line is scaled by a factor of  by replacing each character in the line with  copies of the character."""
scale = int(input())
for i in range(scale):
    print(('*' * scale) + ('x' * scale) + ('*' * scale))
for j in range(scale):
    print((' ' * scale) + ('x' * scale) + ('x' * scale))
for k in range(scale):
    print(('*' * scale) + (' ' * scale) + ('*' * scale))
    