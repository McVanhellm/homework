age = input('Введите Ваш возраст: ')
while True:
    if age == 'выход':
        break
    elif int(age) < 3:
        print('Билет беспатный')
        break
    elif 3 < int(age) < 12:
        print('Стоимость билета 10$')
        break
    elif int(age)> 12:
        print('Стоимость билета 15$')
        break
    else:
        break
