ingradient = []
finish = []
while True:
    ingradient.append(input('Введите ингредиент или "q"-для выхода: '))
    for i in ingradient:
        if i == 'q':
            break
    finish = ingradient
    print(finish)
