'''
1) Вручную создать текстовый файл с данными (например, марка авто, модель авто, расход топлива, стоимость).
2) Создать doc шаблон, где будут использованы данные параметры.
3) Автоматически сгенерировать отчет о машине в формате doc (как в видео 7.2).
'''

import datetime
from docxtpl import DocxTemplate

def get_context(brand, model, fuel, price): # возвращает словарь аргументов

    return {
        'brand': brand,
        'model': model,
        'fuel': fuel,
        'price': price,
    }

def from_template(brand, model, fuel, price, template):

    template = DocxTemplate(template)
    context = get_context(brand, model, fuel, price)

    template.render(context)
    template.save(str(datetime.datetime.now().date()) + '_report.docx')

def generate_report(brand, model, fuel, price):
    template = 'report.docx'
    document = from_template(brand, model, fuel, price, template)

with open('data') as f:
    for line in f:
        newlist = line.split(',')
    generate_report(newlist[0],newlist[1],newlist[2],newlist[3])

