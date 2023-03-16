# Changing the file to include all the data for the year of 2018
# Chnage the title to - dialy and low high temperatures - 2018
# extract low temps from the file and add to chart
# shade in the area between high and low

import csv
from datetime import datetime

infile = open("sitka_weather_2018_simple.csv", "r")


csvfile = csv.reader(infile)

header_row = next(csvfile)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []  # y axis
dates = []  # x axis
lows = []  # y axis

# somedate = datetime.striptime("2018-07-01", "%Y-%m-%d")


for row in csvfile:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    thedate = datetime.strptime(row[2], "%Y-%m-%d")
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
# plt.show()

plt.subplot(2, 1, 1)
plt.plot(dates, highs, c="red")
plt.title("Highs")

plt.subplot(2, 1, 2)
plt.plot(dates, lows, c="blue")
plt.title("Lows")

plt.suptitle("Highs and Lows of Sitka, Alaska")

plt.show()
