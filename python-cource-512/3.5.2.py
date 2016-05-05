import csv

crimes = {}

with open('Crimes.csv', 'r') as f:
	
	reader = csv.reader(f)

	for row in reader:		
		if '2015' in row[2]:
			if row[5] in crimes:
				crimes[row[5]] += 1
			else:
				crimes[row[5]] = 1

print(crimes)
			