human_one = {
    'first_name': 'Фома',
    'last_name': 'Генадьевич',
    'age': 65,
    'city': 'Шчучыншчына'
}
human_two = {
    'first_name': 'Алесь',
    'last_name': 'Дмитриевич',
    'age': 15,
    'city': 'Гродненщина'
}
human_three = {
    'first_name': 'Сан',
    'last_name': 'Саныч',
    'age': 65,
    'city': 'Почему та на....?'
}
people = [human_one, human_two, human_three]
for human in people:
    for key, value in human.items():
        print(key + ":", value)
