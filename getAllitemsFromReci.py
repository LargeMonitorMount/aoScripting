import csv

with open("FullReci.csv", newline='') as f:
	reader = csv.DictReader (f, delimiter=',')
	colsToCheck = []
	for fieldname in reader.fieldnames:

		if len(fieldname.split("/")) > 2 :
			if fieldname.split("/")[2] == "@uniquename":

				colsToCheck.append(fieldname)

	print (colsToCheck)
	for row in reader:
		for col in colsToCheck:
			if row [col] != "":
				print(row [col])
