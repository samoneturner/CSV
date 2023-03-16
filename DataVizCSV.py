import csv
from datetime import datetime

infile = open("sitka_weather_2018_simple.csv", "r")
infile2 = open("death_valley_2018_simple.csv", "r")

csvfile = csv.reader(infile)
csvfile2 = csv.reader(infile2)

header_row = next(csvfile)
header_row2 = next(csvfile2)

print(type(header_row))

date_index = ""
high_index = ""
low_index = ""

sdates, shighs, slows = [], [], []
ddates, dhighs, dlows = [], [], []


for index, column_header in enumerate(header_row):
    # print(index, column_header)
    if column_header == "TMIN":
        low_index = index
    elif column_header == "TMAX":
        high_index = index
    elif column_header == "DATE":
        date_index = index
for row in csvfile:
    try:
        high = int(row[high_index])
        low = int(row[low_index])
        thedate = datetime.strptime(row[date_index], "%Y-%m-%d")
    except ValueError:
        print(f"Missing data for {thedate}")
    else:
        shighs.append(high)
        slows.append(low)
        sdates.append(thedate)

for index, column_header in enumerate(header_row2):
    # print(index, column_header)
    if column_header == "TMIN":
        low_index = index
    elif column_header == "TMAX":
        high_index = index
    elif column_header == "DATE":
        date_index = index
for row in csvfile2:
    try:
        high = int(row[high_index])
        low = int(row[low_index])
        thedate = datetime.strptime(row[date_index], "%Y-%m-%d")
    except ValueError:
        print(f"Missing data for {thedate}")
    else:
        dhighs.append(high)
        dlows.append(low)
        ddates.append(thedate)


import matplotlib.pyplot as plt

fig = plt.figure()

# Sitka Chart
plt.subplot(2, 1, 1)
plt.plot(sdates, shighs, c="red")  # plot high temperatures in the color red
plt.plot(sdates, slows, c="blue")  # plot low temperatures in the color blue
plt.fill_between(
    sdates, shighs, slows, facecolor="blue", alpha=0.1
)  # fill between highs and lows

# Sitka Chart Features
plt.title("SITKA AIRPORT,AK US", fontsize=12)
plt.ylabel("", fontsize=10)


# Death Valley Chart
plt.subplot(2, 1, 2)
plt.plot(ddates, dhighs, c="red")  # plot high temperatures in the color red
plt.plot(ddates, dlows, c="blue")  # plot low temperatures in the color blue
plt.fill_between(
    ddates, dhighs, dlows, facecolor="blue", alpha=0.1
)  # fill between highs and lows

# Death Valley Chart Features
plt.title("DEATH VALLEY, CA US", fontsize=12)
plt.ylabel("", fontsize=10)


fig.autofmt_xdate()

plt.suptitle(
    "Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US"
)

plt.show()
