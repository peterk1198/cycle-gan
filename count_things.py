import pandas as pd
import os

df = pd.read_csv("sample_labels.csv")

males = 0
females = 0

for index, row in df.iterrows():
	if row["Patient Gender"] == "M":
		males += 1
	else:
		females += 1

print (males, " males")
print (females, " females")


for index, row in df.iterrows():
	remove = row["Image Index"]
	if row["Patient Gender"] == "M" and males > 300:
		os.remove("./images/trainM/" + remove)
		males -= 1
	elif row["Patient Gender"] == "F" and females > 300:
		os.remove("./images/trainF/" + remove)
		females -= 1