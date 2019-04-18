
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
					
					crafting_Price = self.lookupIngredientFor(item.strip())
					
					if int(self.lookupIngredientFor(item.strip())) == -1 :
						print ("One or more ingredient price was not found")
					else:
						print ("potential sell Pirce \t\t:", sellPrice)

	def lookupIngredientFor(self, itemID):
		price = 0
		
		
		with open("reciWithouthFormatting.csv") as f:
			for line in f:
				reci = line.split(",")
				if len(reci) > 2 :
					if reci[0] == itemID and reci[3].strip() != "":
					
						price= price + (int(reci[2]) * int(self.lookUpInPriceDtabase(reci[3],7))) # 7 mert abban van a buy
						if int(self.lookUpInPriceDtabase(reci[3],7))< 0 :
							return -1
						print ("Ingerdient Found for:",price,"\tname:" ,reci[3])
		print ("Full ing Pirce \t\t:", price)
		return price
		
		
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
