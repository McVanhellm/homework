ingredients = []
while True:
    message = input('Введите ингридиент: ')
    if message == 'выход':
        break
    else:
        ingredients.append(message)
print('Ваша пицца состаит из: ')
for ingredient in ingredients:
    print(ingredient)
