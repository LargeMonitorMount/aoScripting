import csv
import json
import urllib.request
from bs4 import BeautifulSoup

class Albion2dCrawler(object):

    url = 'https://www.albiononline2d.com/en/item/'
    result = []

    def __init__(self):
        self.crawl()

    def make_request(self, url):
        contents = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(r, "html.parser")
        return soup

    def clean(self, str):
        if str:
            return str.replace('\n', '').replace('\t', '')
        return str

    def pull_item(self, url):
        req = self.make_request(url)
        result = {}
        for table in req.find_all('table', class_='table'):
            if table.find('strong'):
                type = table.find('strong').text
                if not result.get(type):
                    result[type] = []
                for tr in table.find_all('tr'):
                    key, value = tr.find_all('td')
                    property = dict(key=key.text, value=value.text)
                    result[type].append(property)

        return result

    def crawl(self):
        req = self.make_request(self.url)
        for tr in req.find('table', class_='table').find_all('tr'):
            if tr.find_all('td'):
                img = tr.find('img', class_="item-icon").attrs['data-src']
                tds = tr.find_all('td')
                link = tds[1].find('a')
                name = self.clean(link.text)
                url = link.attrs['href']
                tier = self.clean(tds[2].find('p').text)
                type = self.clean(tds[3].find('p').text)
                item = {'img': img,
                        'name': name,
                        'url': url,
                        'tier': tier,
                        'type': type,
                        'attributes': self.pull_item(url)
                        }
                self.result.append(item)

if __name__ == "__main__":
    albion = Albion2dCrawler()
    print (json.dumps(albion.result))