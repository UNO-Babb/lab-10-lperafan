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
    if 60< fat < 90:
        descriptions.append(description)
        fats.append(fat)

df = pandas.DataFrame({"Description": descriptions, "Fat": fats})

df = df.sort_values(by = "Fat", ascending = True)

print(df)

df.plot(kind = 'bar', x = 'Description', y = 'Fat')
plt.xlabel('Food Description')
plt.ylabel('Total Fat (g)')
plt.title('Fat Content of Food')
plt.savefig("output")

print()
print("Graph Explation:")
print("My graph shows the fat content in different foods.", "The x-axis lists the food descriptions, while the y-axis indicates the amount of fat in grams.")

print()
print("Insights from the Data:")
print("The graph shows which foods have the most fat in them. For instance, Oil or table fat, NFS and Salt pork, contain really high fat percentages.")
print("The fat content varies quite a bit, starting from around 60 grams going up to more than 87 grams.")

print()
print("Observations and Trends:")
print("Nuts like hazelnuts and pecans are often listed as high-fat foods, which makes sense given what we know about their nutritional content.")
print("The grouping of certain food categories could suggest that some food groups naturally have higher fat content.")
