cook_book = {}
ingredients_list = []


with open('recipes.txt', encoding = 'utf-8') as f:
    for line in f:
        dish_name = line.strip()
        ingredients_count = int(f.readline())
        for ingredient_line in range(ingredients_count):
            ingredient = line.strip().split(' | ')
            ingredient_dict = {}
            item1, item2, item3 = f.readline().strip().split(' | ')
            ingredient_dict['ingredient_name'] = item1.strip(' ')
            ingredient_dict['quantity'] = item2.strip(' ')
            ingredient_dict['measure'] = item3.strip('\n')
            ingredients_list.append(ingredient_dict)
cook_book[dish_name] = ingredients_list
# print(cook_book)
print(dish_name)

