import requests
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
    ### ХУЙ ПОЙМИ ЧТО, УЖЕ ЗАБЫЛ###
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
    ### ЗАПИСЬ В ФАИЛ ЕКСЕЛЬКУ###
    with open('top100.csv', 'w') as fp:
        writer = csv.writer(fp, delimiter=';')
        # writer.writerow(["your", "header", "foo"])  # write header
        writer.writerows(data)
    jopa = 0
    ### СУММА СЕМУКСВО В ДЕЛЕГИРОВАНИИ ###
    for i in summa:
        c = i.split(',')
        try:
            d = int(c[0]+c[1])
            jopa += d
        except IndexError:
            pass
    ###ВРЕМЯ###
    time = datetime.datetime.now()
    time = str(time)
    ### Записываем, как ебаный абориген в текст.###
    f = open('SumDelegate.txt','a')
    jopa = str(jopa)


    file = open('SumDelegate.txt').read().splitlines()
    ###Математика 1 класс###
    bilo = int(file[-2][:8])
    stalo = int(file[-1][:8])
    ostatok = stalo - bilo
    print(file[-1][:8], file[-2][:8])


    file = open('SumDelegate.txt','a')
    f.write(jopa  + ' '+ 'SEM ' + time + '  Lost\Arrived: ' + str(ostatok) + '.' + '\n')
    f.close()
