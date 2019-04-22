import csv
import math
import datetime

class WhatToCraft(object):

	def __init__(self):
		self.main()
	def main (self): ##### EZZ A MAIIN
		print (datetime.datetime.now())
		print ("ItemName|Krafting Price| selling price|porfit?/item| reci")
		
		with open("items.txt") as g:
			for line in g:
				item = line.strip()
				if item != "" :
					
					sellPrice = self.lookUpInPriceDtabase(item,5) # 5 mert abban van a sell
					crafting_Price,reci,maxReciKey = self.lookupPriceFor(item.strip())

					if int(crafting_Price) < int(sellPrice) and int(crafting_Price) != 10000000000000 and (int(crafting_Price) != -1 and int(sellPrice) != -1):
						#print ("\t#&@#>@>#&@>#&@>#   ilyet Kraftoljáá  #&@#>@>#&@>#&@>#\t", item.strip())

						print (item,"|",crafting_Price ,"|",sellPrice,"|",int(sellPrice)-int(crafting_Price),"|",str(reci[maxReciKey]).replace(","," and") )
						
					#else:
						#print(": Nope",crafting_Price ,"\t vs \t",sellPrice)

					#if int(self.lookupPriceFor(item.strip())) == -1 :
					#	print ("One or more ingredient price was not found")
					#else:
					#	print ("potential sell Pirce \t\t:", sellPrice)

	def lookupPriceFor(self, itemID):
		uniqitemName = itemID

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
									#print ("mats found for: ",row["/"+fieldname.split("/")[1]+"/craftingrequirements/#id"],"",uniqitemName,"\t",count,"x : ",row[fieldname],"\t" ,fieldname )
									reciID =str(row["/"+fieldname.split("/")[1]+"/craftingrequirements/#id"])
									if reciID not in recis.keys():
										recis[reciID] = {}
									recis[reciID][row[fieldname]] = count										##TEHÁT EZ egy nested dictionary

								if fieldname.endswith("craftingrequirements/@silver") and row[fieldname] !="" :
									silver+=int(row[fieldname])											## ez az if kezelei a silver és ehehz hasonlóan kell a fokuszt meg ilyeneket mellé rakni
			#print (recis)
			#print (silver)
			#auhudahsuhfasduofhsdiofasdufhasufhauhauh
			max = 10000000000000  ### ez itt valójában minimum mert nyilván a legolcsóbb recit választjuk ki. auhudahsuhfasduofhsdiofasdufhasufhauhauh
			##auhudahsuhfasduofhsdiofasdufhasufhauhauh
			maxReciID = ""
			for reciID in recis.keys():
				summ  = self.calcRecValue(recis, reciID)
				if summ < max:
					maxReciID = reciID
					max =summ
			#print("Így a legjobb:\t",maxReciID,"\t ",max)
		return max,recis,maxReciID
	def calcRecValue(self,recis,reciID):
		summ = 0
		for mat in recis[reciID].keys():								#RECI ÖSSZEG

			count = recis[reciID][mat]
			priceOfMat = self.lookUpInPriceDtabase(mat,3)
			if priceOfMat == -1:
				return 10000000000000
			#print ("\t\t",priceOfMat,"\t",count,"\t",mat)
			summ = int(priceOfMat)*int(count) + summ
		#print ("\trecept: ",reciID,"\tÁra",summ)
		return summ

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
			return max

if __name__ == "__main__":
	albion = WhatToCraft()
