import csv
import json
import urllib.request
cities = "?locations=Martlock" ## vesszővel pl. Martlock,Bridgewatch

l = csv.writer(open("test.csv", 'w', newline=''))
l.writerow(["item_id", "city", "quality", "sell_price_min", "sell_price_min_date", "sell_price_max", "sell_price_max_date", "buy_price_min", "buy_price_min_date", "buy_price_max", "buy_price_max_date"])


with open("items.txt") as g:
	for item in g:
		url = "https://www.albion-online-data.com/api/v1/stats/prices/"+item.strip()+cities
		print (item.strip(), url)
		
		try:	
			contents = urllib.request.urlopen(url).read()
		
			x = json.loads(contents)
			for x in x:
				l.writerow([x["item_id"],
						x["city"],
						x ["quality"],
						x ["sell_price_min"],
						x ["sell_price_min_date"],
						x ["sell_price_max"],
						x ["sell_price_max_date"],
						x ["buy_price_min"],
						x ["buy_price_min_date"],
						x ["buy_price_max"],
						x ["buy_price_max_date"]])
			
			
			
		except urllib.error.URLError as e: print(e.reason)
		
