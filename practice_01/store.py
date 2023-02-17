# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

#lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
#print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

table_item_1 = store[goods['Стол']][0]
table_item_2 = store[goods['Стол']][1]
price_tables = table_item_1['quantity'] * table_item_1['price'] + table_item_2['quantity'] * table_item_2['price']

print(f'Стол - {table_item_1["quantity"] + table_item_2["quantity"]} шт, стоимость {table_item_1["price"] + table_item_2["price"]} руб')

sofa_item_1 = store[goods['Диван']][0]
sofa_item_2 = store[goods['Диван']][1]

print(f'Диван - {sofa_item_1["quantity"] + sofa_item_2["quantity"]} шт, стоимость {sofa_item_1["price"] + sofa_item_2["price"]} руб')

chair_item_1 = store[goods['Стул']][0]
chair_item_2 = store[goods['Стул']][1]
chair_item_3 = store[goods['Стул']][2]

print(f'Стул - {chair_item_1["quantity"] + chair_item_2["quantity"] + chair_item_3["quantity"]} шт, стоимость {chair_item_1["price"] + chair_item_2["price"] + chair_item_3["price"]} руб')

# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.
