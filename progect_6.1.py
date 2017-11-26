"""
Получение рецептов: передаем список продуктов.
"""

import urllib.request
import urllib.parse
import json
import re

ingredient_line = ''

# Ввод ингредиентов
products = str(input("Введите на английском ингредиенты через запятую.\n"))
if re.search('\d+',products):
    print("Строка не должна содержать числа, введите ещё раз.")
    products = str(input("Введите список продуков через запятую.\n"))
ingredients = products.split(",")

# Составление строки поиска по ингридиентам
for ingredient in ingredients:
    ingredient_line = ingredient_line + ingredient + ","
ingredient_line = ingredient_line[:-1]
data = {"i": ingredient_line}
enc_data = urllib.parse.urlencode(data)

# get запрос
response = urllib.request.urlopen("http://www.recipepuppy.com/api/"+"?"+enc_data)
obj1 = response.read().decode()
recipes = json.loads(obj1)

# вывод блюд
print("Список блюд  из ваших ингридиентов:")
for recipe in recipes['results']:
    print(recipe['title'].strip())
