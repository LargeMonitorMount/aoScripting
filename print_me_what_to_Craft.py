import csv
import math

class WhatToCraft(object):

	def __init__(self):
		self.main()
	def main (self):
		with open("items.txt") as g:
			for line in g:
				item = line.strip()
				if item != "" :
					print ("item to lookup:",item.strip())
					sellPrice = self.lookUpInPriceDtabase(item,5) # 5 mert abban van a sell
					
					crafting_Price = self.lookupPriceFor(item.strip())
					
					if int(self.lookupPriceFor(item.strip())) == -1 :
						print ("One or more ingredient price was not found")
					else:
						print ("potential sell Pirce \t\t:", sellPrice)

	def lookupPriceFor(self, itemID):
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
			max = 0
			for reci in recis:
				for reciKey in reci.keys():
					print (reciKey)




		
	def lookUpInPriceDtabase(self,itemID,col):
		max = 0
		maxLoc = ""
		with open("test.csv") as f:
			for line in f:
				price = line.split(",")
				if price[0].strip() == itemID.strip():
					
					if int(max) < int(price[col]):
						maxLoc = price[1]
						max =price[col]
		if max == 0:
			return -1
		else:
			print (maxLoc)
			return max
		
if __name__ == "__main__":
	albion = WhatToCraft()
