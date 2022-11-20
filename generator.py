import random

pass_one = [
    'a', 'b', 'c', 'd', 'e', '1', '2', '3', '#', '$', '%'
]
password = ""
for x in range(16):
    password = password + random.choice(pass_one)[0]
print('Yours password is', password)
