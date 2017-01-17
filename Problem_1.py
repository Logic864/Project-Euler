#If we list all the natural numbers below 10 that are multiples of 3 or 5,
#we get 3, 5, 6 and 9.
#The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

start = 999
total = 0

while start != 0:
    if (start % 5 == 0) or (start % 3 == 0):
        total = total + start

    start = start - 1

print total