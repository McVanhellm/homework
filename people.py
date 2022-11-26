people_one = {
    'first_name': 'Oleg',
    'last_name': "Petrovich",
    'age': 32,
    'city': 'Hrodna'
}
peolpe_two = {
    'first_name': 'Debil',
    'last_name': "Svoloch",
    'age': 56,
    'city': 'Cheboksary'
}
peolpe = [people_one, peolpe_two]
print(peolpe)
for key, value in people_one.items():
    print(key, value)
