# 4) Создать csv файл с данными о машине.

import csv

cardata = [['brand', 'model', 'fuel', 'price'],['Audi', 'Q7', 18, 7000000]]

with open('example.csv', 'w') as f:
    writer = csv.writer(f, delimiter='&')  #
    writer.writerows(cardata)
print('Writing complete!')


with open('example.csv') as f:
    reader = csv.reader(f,delimiter = '&')
    for row in reader:
        print(row)
