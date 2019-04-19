import csv

uniqitemName ="T5_PLANKS"

with open("FullReci.csv", newline='') as f:
	reader = csv.DictReader (f, delimiter=',')
	colsToCheck = []
	for fieldname in reader.fieldnames:

		if len(fieldname.split("/")) > 2 :
			if fieldname.split("/")[2] == "@uniquename":

				colsToCheck.append(fieldname)

	recis={}
	mat= {}
	silver=0
	for row in reader: 																			## kikeressük a recut
		for col in colsToCheck: 																## Megnézzük a releváns oszlopokban
			if row [col] == uniqitemName:
				for fieldname in reader.fieldnames:												##ha megtaláltuk akkor megkeressük a hozzávalókat meg a silvert meg ilyeneket
					if not "enchantments" in fieldname:											### ez azért kell hogy az encsinek a receptjét ne vegye bele

						if fieldname.endswith("craftingrequirements/craftresource/@uniquename") and row[fieldname] !="" :
							count = row["/"+fieldname.split("/")[1]+"/craftingrequirements/craftresource/@count"] ### hány darab kell
							mat[row[fieldname]] = count										## EZ az if kezeli a matsot
							print ("mats found for: ",row["/"+fieldname.split("/")[1]+"/craftingrequirements/#id"],"",uniqitemName,"\t",count,"x : ",row[fieldname],"\t" ,fieldname )
							reciID =str(row["/"+fieldname.split("/")[1]+"/craftingrequirements/#id"])
							if reciID not in recis.keys():
								recis[reciID] = {}
							recis[reciID][row[fieldname]] = count										##TEHÁT EZ egy nested dictionary

						if fieldname.endswith("craftingrequirements/@silver") and row[fieldname] !="" :
							silver+=int(row[fieldname])											## ez az if kezelei a silver és ehehz hasonlóan kell a fokuszt meg ilyeneket mellé rakni
	print (recis)
	print (silver)
