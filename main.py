#MapPlot.py
#Name:
#Date:
#Assignment:

import food
import pandas
import matplotlib.pyplot as plt

report = food.get_report()

descriptions = []
fats = []
for item in report:
    description = item["Description"]
    fat = item["Data"]["Fat"]["Total Lipid"]
    if "Milk" in description.lower() and fat > 15:
        descriptions.append(description)
        fats.append(fat)

df = pandas.DataFrame({"Description": descriptions, "Fat": fats})

df = df.sort_values(by = "Fat", ascending = True)

print(df)

df.plot(kind = 'bar', x = 'Description', y = 'Fat')
plt.xlabel('Milk Description')
plt.ylabel('Total Fat (g)')
plt.title('Fat Content of Milks')
plt.savefig("output")