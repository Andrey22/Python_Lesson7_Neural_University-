# 5) Создать json файл с данными о машине.
import json

dict_ex = {'brand': 'Audi', 'Model': 'Q7', 'FuelConsumption': 18, 'Price': 7 }

with open('jsonfile.txt', 'w') as f:
    json.dump(dict_ex, f)

with open('jsonfile.txt') as f:
    data = json.load(f)

print(type(data), data)