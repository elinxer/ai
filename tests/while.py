# python while study and exercise
#

__author__ = "Elinx"

numbers = [333, 11, 445, 111]

even = []
odd = []

while len(numbers) > 0:
    number = numbers.pop()
    if ((number % 2) == 0):
        even.append(number)
    else:
        odd.append(number)

print(even)
print(odd)
