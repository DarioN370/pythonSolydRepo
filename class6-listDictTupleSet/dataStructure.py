my_list = ['A', 'B', 'C', 'D', 'E', 'F'] #LISTA muda
my_tuple = ('Gui', 'Joao') #imutavel
my_dict = {'nome': 'Dario', 'idade': 22} #funciona como um dictionary real
my_set = {'Gui', 'Pedro', 'Carr'} #CONJUNTO - no repeat, mesmo que coloque dois iguais, ele vai contar como se tivesse um, alem dele não ter ordem, ou seja, não tem indice, não tem como voce buscar o item numero 0 do conjunto, ou o indice 3

#TUPLE
print(my_tuple)
print(type(my_tuple))
print(my_tuple[1] + ", esse é o nome no indice 1")
for name in my_tuple:
    print (name)
# my_tuple[0] = 'joão' - isso daria erro, a tupla é imutavel lembra ?