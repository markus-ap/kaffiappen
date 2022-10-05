data = open("coffee.tsv", "r", encoding="utf-8").read().split("\n")

from datetime import datetime, timedelta
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 


def extract(row):
	row = row.split("\t")
	d = row[0].split(" at ")[0]
	t = row[-1].strip()
	
	time = datetime.strptime(d, "%B %d, %Y")
	
	return time, t.lower()

def make_structure():
	structure = {}
	while data:
		row = data.pop(0)
		try:
			date, t = extract(row)
			date = str(date)[:7]
			structure.setdefault(t, {})
			structure[t].setdefault(date, 0)
			structure[t][date] += 1
		except:
			pass
	return structure

def clean_structure(mn=0):
	structure = make_structure()
	dels = []
	for key, value in structure.items():
		for date in value:
			if structure[key][date] <= mn:
				dels.append((key, date))
	for d in dels:
		#print("Deleting", d[0], "at", d[1])
		del structure[d[0]][d[1]]
	dels = []

	for key, value in structure.items():
		if value == dict():
			dels.append(key)
	for d in dels:
		del structure[d]

	return structure

def visualise_structure(mn=0):
	structure = clean_structure(mn)
	df = pd.DataFrame(structure)
	df.plot(kind="bar", stacked=True)
	plt.show()

visualise_structure()
