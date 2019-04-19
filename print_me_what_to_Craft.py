import csv
import math

class WhatToCraft(object):

	def __init__(self):
		self.main()
	def main (self): ##### EZZ A MAIIN
		print (self.banner("fasz"))

		with open("items.txt") as g:
			for line in g:
				item = line.strip()
				if item != "" :
					print(item, end='', flush=True)
					sellPrice = self.lookUpInPriceDtabase(item,5) # 5 mert abban van a sell
					crafting_Price,reci,maxReciKey = self.lookupPriceFor(item.strip())



					if int(crafting_Price) < int(sellPrice) and int(crafting_Price) != 10000000000000 and (int(crafting_Price) != -1 and int(sellPrice) != -1):
						print ("\t#&@#>@>#&@>#&@>#   ilyet Kraftoljáá  #&@#>@>#&@>#&@>#\t", item.strip())

						print (crafting_Price ,"\t vs \t",sellPrice )
						print (reci[maxReciKey])
					else:
						print(": Nope",crafting_Price ,"\t vs \t",sellPrice)

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














	def banner(text, ch='=', length=78):
		username = "FASZ"
		style = "*" # input("The options are: *, =, @, #, $, !, ~, ', ^, &, |, %, -, {}, (), [], <> or a BONUS style! or you can add letters to it. \n")

		space = ' '

		# two lists which store the value the input can take...
		style1 = ["*", "=", "@", "#", "$", "!", "~", "'", "^", "&", "|", "%", "-"]
		style2 = ["{}", "()", "[]", "<>"]

		# appends all the letters in style 1. I am really lazy to put them each in the list, so the computer will do that for me.
		for i in "abcdefghijklmnopqrstuvwxyz":
			style1.append(i)

		# finds all the indexes of a char in a string
		def find_indices(char, in_string):
			index = -1
			while True:
				index = in_string.find(char, index + 1)
				if index == -1:
					break
				yield index

		# chars from style1 + letters
		if style in style1:
			# makes the first line, and add as many stars (or anything else). It also add one star on each side to make it look like a border
			linie = style + style * len(username) + style + "\n"
			if " " in username:
			# if there is any space in the input, it will find all the indexes of the " " to remove the stars
				for i in find_indices(space, username):
					linie = list(linie)
					linie[i + 1] = " "
					linie = "".join(linie)
			# prints the border and the input
			print(linie + style + username + style + "\n" + linie)

		# same thing, but the style two include the brackets () [] and the border will be like (--- --- ---).
		if style in style2:
			middle = "-"
			line = style[0] + len(username) * middle + style[1]
			if " " in username:
				for i in find_indices(space, username):
					line = list(line)
					line[i + 1] = " "
					line = "".join(line)
			print(line + "\n" + style[0] + username + style[1] + "\n" + line)

		# here the output would look like
		"""
		^^^^^ ^^^^
		<Abcd efg>
		vvvvv vvvv
		"""
		if style.lower() == "bonus":
			line1 = "^" + "^" * len(username) + "^"
			line2 = "v" + "v" * len(username) + "v"
			if " " in username:
				for i in find_indices(space, username):
					line1 = list(line1)
					line2 = list(line2)
					line1[i + 1] = " "
					line2[i + 1] = " "
					line1 = "".join(line1)
					line2 = "".join(line2)
			print(line1 + "\n" + "<" + username + ">" + "\n" + line2)

if __name__ == "__main__":
	albion = WhatToCraft()
