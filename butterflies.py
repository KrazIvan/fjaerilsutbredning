import csv
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

# Loads the data from the CSV file.
years = {}
northmost = {}
latitudes = {}
observations_by_year = {}
with open("25_years_of_salgskimmer.csv") as f:
    reader = csv.reader(f)
    next(reader) # Skips the first line in the CSV file.
    for row in reader:
        year = row[2][:4]
        latitude = float(row[0])
        if year not in years:
            years[year] = []
            northmost[year] = latitude
            latitudes[year] = []
        years[year].append(latitude)
        latitudes[year].append(latitude)
        northmost[year] = max(northmost[year], latitude)
        if year not in observations_by_year:
            observations_by_year[year] = 0
        observations_by_year[year] += int(row[3])



# ----  At what rate has the purple emperor spread northward? ----

# Plots the northernmost latitude over time.
years_list = list(years.keys())
years_list.sort()
northmost_list = [northmost[year] for year in years_list]
plt.plot(years_list, northmost_list)
plt.xlabel("Year")
plt.ylabel("Northernmost Latitude")
plt.title("Spread of Purple Emperor Butterflies (Northernmost Latitude Over Time)")
plt.savefig("Purple Emperor Spread (Northernmost Latitude Over Time).pdf")
#plt.show() #<------ Uncomment to show
plt.close()

# Plots the average latitude over time.
average_latitudes = [np.mean(latitudes[year]) for year in years_list]
plt.plot(years_list, average_latitudes)
plt.xlabel("Year")
plt.ylabel("Average Latitude")
plt.title("Spread of Purple Emperor Butterflies (Average Latitude Over Time)")
plt.savefig("Purple Emperor Spread (Average Latitude Over Time).pdf")
#plt.show() #<------ Uncomment to show
plt.close()



# ----  How has the number of observations changed over time? ----

# Plots the number of observations over time
observations_list = [observations_by_year[year] for year in years_list]
plt.bar(years_list, observations_list)
plt.xlabel("Year")
plt.ylabel("Number of Observations")
plt.title("Number of Observations of Purple Emperor Butterflies in Sweden")
plt.savefig("Purple Emperor Observations.pdf")
#plt.show() #<------ Uncomment to show
plt.close()



# ----   When did the purple emperor arrive in Gotland? ----

data = []
with open("25_years_of_salgskimmer.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader) # Skips the first line in the CSV file.
    for row in reader:
        latitude = float(row[0])
        longitude = float(row[1])
        year = int(row[2][:4])
        quantity = int(row[3])
        data.append([latitude, longitude, year, quantity])

# Purple Emperor in Gotland
gotland_data = [x for x in data if x[0] >= 57 and x[0] < 58 and x[1] >= 18 and x[1] <= 19.3] # The latitude and longitude of Gotland.
years = defaultdict(int)
for row in gotland_data:
    year = row[2]
    quantity = row[3]
    years[year] += quantity

years = dict(sorted(years.items()))
x = list(years.keys())
y = list(years.values())

plt.bar(x, y)
plt.xlabel("Year")
plt.ylabel("Number of Observations")
plt.title("Purple Emperor Observations in Gotland")
plt.savefig("Purple Emperor Observations in Gotland.pdf")
#plt.show() #<------ Uncomment to show
plt.close()

# Time of the year the Purple Emperor is active
latitude_to_months = defaultdict(lambda: defaultdict(int))
for row in data:
    latitude = row[0]
    year = row[2]
    month = row[2] % 12
    quantity = row[3]
    latitude_to_months[latitude][month] += quantity

plt.figure()
plt.title("Time of the year the Purple Emperor is active")
plt.xlabel("Month")
plt.ylabel("Number of observations")
for latitude, months in latitude_to_months.items():
    x = list(months.keys())
    y = list(months.values())
    plt.plot(x, y)
plt.legend()
plt.savefig("Time of the year the Purple Emperor is active.pdf")
#plt.show() #<------ Uncomment to show
plt.close()