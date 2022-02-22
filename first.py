import numpy as np
import pandas as pd
from random import randint

from translator import TranslatorToUk

url_ = r'http://smtm.com.ua/_prices/import-retail-horoshop.xls'
source = r'~/learning/parcer_for_sx/tmp/import.xls'


class Item:
    def __init__(self,
                 art=None,
                 name=None,
                 price=None,
                 category=None,
                 descr=None,
                 img=None,
                 other_features=None,
                 brand=None,
                 country=None,
                 warranty=None,
                 material=None,
                 mass=None,
                 packing_length=None,
                 packing_width=None,
                 packing_height=None,
                 packing_mass=None,
                 packing_type=None,

                 ):
        self.art = art
        self.name = name
        self.price = price
        self.category = category
        self.descr = descr
        self.img = img
        self.other_features = other_features
        self.brand = brand
        self.country = country
        self.warranty = warranty
        self.material = material
        self.mass = mass
        self.packing_length = packing_length
        self.packing_width = packing_width
        self.packing_height = packing_height
        self.packing_mass = packing_mass
        self.packing_type = packing_type


a = ['Артикул', 'Название', 'Unnamed: 2', 'Цена', 'Раздел',
     'Описание товара', 'Фото', 'Прочие особенности',
     'Основные характеристики', 'Бренд (Страна)', 'Страна происхождения',
     'Гарантия (мес)', 'Материал', 'Масса (кг)', 'Упаковка: длина (см)',
     'Упаковка: ширина (см)', 'Упаковка: высота (см)',
     'Упаковка: масса (кг)', 'Тип упаковки', 'Новинка', 'Хит', 'Акция',
     'Дополнительные характеристики', 'Цвет', 'Диаметр: максимальный (мм)',
     'Диаметр: минимальный (мм)', 'Диаметр: внутренний (мм)',
     'Вводимая длина (мм)', 'Общая длина (мм)', 'Ширина (мм)', 'Вибрация',
     'Подогрев', 'Пульсация', 'Вакуумная стимуляция', 'Массирующее движение',
     'Управление со смартфона', 'Интеллектуальный режим', 'Пульт Д/У',
     'Питание', 'Батарейки в комплекте', 'Тип стимуляции', 'Для новичков',
     'Водостойкость', 'Размер члена максимальный (см)',
     'Размер члена минимальный (см)', 'Смазка в комплекте', 'Двойной слой',
     'Смещенный центр тяжести', 'Количество моторов', 'Объем (мл)',
     'Косметика: вид', 'Косметика: действие', 'Ароматы любви',
     'Веганфрендли', 'Белье: размер']

df = pd.read_excel(source, sheet_name='TDSheet')
df2 = df.replace({np.nan: None})

rows = df.count()['Артикул']
my_list = []
for item in range(0, rows):
    it = Item()
    it.art = 'RZ' + str(df2['Артикул'][item]) + str(randint(0, 9)) + str(randint(0, 9))
    it.name = df2['Название'][item]
    it.price = df2['Цена'][item].item()
    it.mass = df2['Прочие особенности'][item]
    it.descr = df2['Описание товара'][item]
    my_list.append(it)

print(df)
