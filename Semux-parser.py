import requests
import os
from bs4 import BeautifulSoup
import csv
import datetime

ir = 0
while ir < 2:
    ir += 1
    url = 'https://semux.info/delegates'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    name_delegat_all = soup.find_all('td' , class_='country')

    spisok3 = []
    price1 = soup.findAll('tr')
    priceone = price1[1].text
    summa = []
    b = 0
    for i in price1[1:101]:

        if b > 10:
            abc = i.text[3:][:32]
        else:
            abc = i.text[2:][:32]
        L = list(abc)
        spisok3.append(abc)
        b += 1

    data = []

    for i in spisok3:
        pobeda = (i.replace('Validator', ' ').split())
        pobeda2 =(pobeda[0] + ' ' + pobeda[1]).split()
        summa.append(pobeda[1])
        data.append(pobeda2)

    with open('top100.csv', 'w') as fp:
        writer = csv.writer(fp, delimiter=';')
        # writer.writerow(["your", "header", "foo"])  # write header
        writer.writerows(data)
    jopa = 0


    for i in summa:

        try:
            b = int(i.replace(',', ''))
            b = int(i.replace('%', ''))
        except:ValueError

        jopa += b

    time = datetime.datetime.now()
    time = str(time)

    f = open('SumDelegate2.txt','a')
    jopa = str(jopa)

    file = open('SumDelegate2.txt').read().splitlines()

    if os.stat("SumDelegate2.txt").st_size == 0:
        file = open('SumDelegate2.txt', 'a')
        f.write("8443573 SEM 2019-04-22 23:12:31.499806  Top 100: Lost\Arrived: 0." + '\n')
        f.write("8443573 SEM 2019-04-22 23:12:31.499806  Top 100: Lost\Arrived: 0." + '\n')
    try:
        bilo = int(file[-2][:8])
        stalo = int(file[-1][:8])
        print(bilo)
        print(stalo)
        Ostalos = stalo - bilo


    except ValueError:
        pass
    except IndexError:
        pass

    file = open('SumDelegate2.txt','a')
    f.write(jopa + '  ' + ' SEM ' + time + '  Top 100: Lost\Arrived: ' + str(Ostalos) + '.' + '\n')
    f.close()
