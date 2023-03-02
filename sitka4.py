# handle error checking using try and except
# change file to use death valley data

import csv
from datetime import datetime

infile = open("death_valley_2018_simple.csv", "r")

csvfile = csv.reader(infile)

header_row = next(csvfile)

# print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []  # y axis
dates = []  # x axis
lows = []  # y axis

# somedate = datetime.striptime("2018-07-01", "%Y-%m-%d")

for row in csvfile:
    try:
        high = int(row[4])
        low = int(row[5])
        thedate = datetime.strptime(row[2], "%Y-%m-%d")
    except ValueError:
        print(f"Missing data for {thedate}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(thedate)


# print(highs)
# print(lows)

import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c="red", alpha=0.5)  # plot high temperatures in the color red
plt.plot(dates, lows, c="blue", alpha=0.5)  # plot low temperatures in the color blue

plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
# Chart Features

plt.title("Daily and low high temperatures - 2018", fontsize=16)
plt.xlabel("", fontsize=16)
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)


fig.autofmt_xdate()
plt.show()
