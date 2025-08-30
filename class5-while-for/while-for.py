names = ['Guilherme', 'Dario', 'Marcelo', 'Jym', 'Sheldon']

for i in names:
    print(i) #That “name” can call anything, like game in games, car in cars, or number in numbers, just every create this making a sense.

for i in range(5): #same thing.
    print(names[i])

for i in range(len(names)): #same thing - Aqui ele pega o tamanho da lista, e printa o tamanho certo caso eu não saiba o tamanho dela
    print(names[i])

###############################################################


##################### OR CAN I USE THIS ###########################
#list_numbers = range(5) - this is the same thing as this behind.
number: int # Here im just add a type to VAR because python as rage me.
for number in range(5): #way to make a list more quickly
    print(number)
# test