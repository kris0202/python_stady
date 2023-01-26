# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['father', 'mother', 'Kristina']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    ['Kristina', 160],
    ['father', 180],
    ['mother', 165],
]
fathers_height = 'Рост отца:'

print(fathers_height + str(my_family_height[1][1]))

print(f"Рост отца: {my_family_height[1][1]}")
# Выведите на консоль рост отца в формате
# Рост отца: 170
# Здесь советую загуглить как использовать f-строки в python

print(my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1])
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
