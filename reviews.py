import pandas as pd

#Reading csv file
df = pd.read_csv("/Users/lancebiddle/CodeYou/wine-reviews-exercise-ltbiddle/data/winemag-data-130k-v2.csv.zip")

#Assigning desired data to variables
country_count = df.groupby("country").country.count()
points = df.groupby("country").points.mean().round(1)

#Creating new Data Frame
new_df = pd.DataFrame({"Count": (country_count), "Points": (points)})

#Reset name of index
new_df.index.names = ["Country"]

#Save Data Frame to .csv
new_df.to_csv("/Users/lancebiddle/CodeYou/wine-reviews-exercise-ltbiddle/reviews-per-country.csv")
