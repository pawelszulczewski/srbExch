from bs4 import BeautifulSoup
import urllib2

data = []
web_page = urllib2.urlopen("http://www.nbs.rs/kursnaListaModul/srednjiKurs.faces").read()
soup = BeautifulSoup(web_page)

final_link = soup.p.a
final_link.decompose()

table = soup.find('table', {'id': 'index:srednjiKursLista'})
rows = table.find_all('tr')

for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols])

for rates in data:
        d = []
        for rates_data in rates[2:5]:
                if rates_data:
                        d.append(rates_data.splitlines()[0].encode('UTF8'))
                else:
                        d.append("-")
                if (len(d) == 3):
                        print d
             
