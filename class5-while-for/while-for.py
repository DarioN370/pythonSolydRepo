names = ['Guilherme', 'Dario', 'Marcelo', 'Jym', 'Sheldon']

for i in names:
    print(i) #That “name” or "i" can call anything, like game in games, car in cars, or number in numbers, just every create this making a sense. i = item

for i in range(5): # range é uma function que ja vem com o python
    print(names[i])

for i in range(len(names)): #same thing - Here it takes the size of the list, and prints the correct size -in case I don't know its size
    print(names[i])

###############################################################


##################### OR CAN I USE THIS ###########################
#list_numbers = range(5) - this is the same thing as this behind.
number: int # Here im just add a type to VAR because python as rage me.
for number in range(10): #way to make a list of number more quickly
    print(number)
# test