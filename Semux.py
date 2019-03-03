import requests
from bs4 import BeautifulSoup
import csv


url = 'https://semux.info/delegates'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

name_delegat_all = soup.find_all('td' , class_='country')

spisok3 = []
price1 = soup.findAll('tr')
priceone = price1[1].text
print(priceone)

for i in price1[1:100]:
    abc = i.text[2:][:30]
    L = list(abc)
    spisok3.append(abc)
data = []
for i in spisok3:
    pobeda = (i.replace('Validator', ' ').split())
    pobeda2 =(pobeda[0] + ' ' + pobeda[1]).split()
    data.append(pobeda2)

print(data)

with open('test.csv', 'w') as fp:
    writer = csv.writer(fp, delimiter=';')
    # writer.writerow(["your", "header", "foo"])  # write header
    writer.writerows(data)


print(data)
