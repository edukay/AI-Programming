#!/usr/bin/env python3

import random
import collections
import math
import matplotlib.pyplot as plt

temps = collections.defaultdict(list)

months = ['jan', 'feb', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

for month in months:
    if month == 'jan' or month == 'march' or month == 'may' or month == 'july' or month == 'august' or month == 'october' or month == 'december':
        days = 31
    elif month == 'february' or month == 'april' or month == 'june' or month == 'september' or month == 'november':
        days = 30
    count = 0
    while True:
        if count == days:
            break
        temperature = random.randrange(10, 40)
        temps[month].append(temperature)
        count += 1

# Monthly standard deviations are stored here
sdeviations = []


# Calculate the total for each month and get the Mean for each month
for month in temps:
# if month == 'jan':
    total = 0

    count = 0
    print("The temperatures for ", month, " are: ", temps[month])
    print("Days in ", month, "are ", len(temps[month]))
    for temp in temps[month]:
        total += temp
        count += 1
    mean = total / count
    print("The Mean for ", month, "is: ", mean)

    # Compute the variance
    variance = []
    for temp in temps[month]:
        variance.append((mean - temp) ** 2)

    print("The Variances for the month of ", month, "is: ", variance)

    # Summation of variances
    summation = 0
    for value in variance:
        summation += value

    print("Summation of variances is: ", summation)

    standardDeviation = summation / (len(temps[month]) - 1)
    # square root
    squareRoot = math.sqrt(standardDeviation)

    print("The standard deviation for ", month, " is ", squareRoot)

    sdeviations.append(squareRoot)

x = sdeviations
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

plt.scatter(x, y, s=30, c='blue')

plt.title('Scatter Graph of Standard Deviations against Months')
plt.xlabel('Standard deviation')
plt.ylabel('Months ina year')

plt.show()




