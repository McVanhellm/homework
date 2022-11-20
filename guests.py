guests = ['Алесь', 'Богдан', 'Владислав', 'Алексей', 'Захар']
print(len(guests))
guests.insert(0, 'Ульяна')
guests.insert(2, 'Фома')
guests.insert(5, 'Михаил')
for guest in guests:
    if guest == 'Владислав':
        print(guest + ' не сможет прийти')
        guest = 'Матвей'
    print("Доро пожаловать на вечер - " + guest)
for guest_last in guests:
    if guest_last == 'Алесь' or guest_last == 'Ульяна':
        print('Рад тебя видеть - ' + guest_last)
    else:
        name = guests.pop()
        print('Извини, что не получилоь - ' + name)
