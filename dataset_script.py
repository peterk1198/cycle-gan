import pandas as pd
import shutil

df = pd.read_csv("sample_labels.csv")


for index, row in df.iterrows():
	img = row['Image Index']
	s = "./images/" + img
	male = "./images/trainM/" + img
	female = './images/trainF/' + img
	if row['Patient Gender'] == 'M':
		shutil.move(s, male)
	else:
		shutil.move(s, female)

