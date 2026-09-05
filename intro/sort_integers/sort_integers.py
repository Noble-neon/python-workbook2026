""" mr. Eraj, if you are reading this, i just wanted to notice that
I could do this task just by using the following code
abc = [a, b, c]
abc.sort()
print(abc.strip([]), or using a cycle or many more things, but I decided to do
it in the way that other freshman should do it, i.e an algebraic approach"""


a = int(input())
b = int(input())
c = int(input())

largest = max(a, b, c)
smallest = min(a, b, c)
middle = (a + b + c) - smallest - largest

print(f"{smallest}, {middle}, {largest}")