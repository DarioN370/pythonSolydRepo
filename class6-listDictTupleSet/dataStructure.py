my_list = ['A', 'B', 'C', 'D', 'E', 'F'] #LISTA muda
my_tuple = ('Gui', 'Joao') #imutavel/ só muda se eu mudar ela toda
my_dict = {'name': 'Dario', 'age': 22} #funciona como um dictionary real
my_set = {'Gui', 'Pedro', 'Carr'} #CONJUNTO - no repeat, mesmo que coloque dois iguais, ele vai contar como se tivesse um, alem dele não ter ordem, ou seja, não tem indice, não tem como voce buscar o item numero 0 do conjunto, ou o indice 3

#--------------------TUPLE--------------------
print('\n--------------------TUPLE--------------------')
print(my_tuple)
print(type(my_tuple))
print(my_tuple[1] + ", esse é o nome no indice 1")
for name in my_tuple:
    print (name)
# my_tuple[0] = 'joão' - isso daria erro, a tupla é imutavel lembra ?
if 'Paulin' in my_tuple:
    print('ele esta na tupla.')
else:
    print('Não tem esse nome na Tupla')

#--------------------DICT--------------------
print('\n--------------------DICTIONARY--------------------')
print(my_dict)
print(my_dict.values())
print(my_dict.keys())
print(my_dict['age'])
print(len(my_dict))
if 'Dario' in my_dict.values():
    print('Dario esta no Dict!')
for valores in my_dict.values():
    print(valores)
for chaves in my_dict.keys():
    print(chaves)
my_dict['name'] = 'Donk' #switch name
my_dict['age'] = 17 #switch age
my_dict['address'] = 'Rua Okhotny Ryad' #add some address
my_dict['country'] = 'Russia'
my_dict['phone'] = 888999
print(my_dict)

#--------------------SET ou CONJUNTO--------------------
print('\n--------------------SET--------------------')
print(my_set)
my_set.add('Maria')
my_set.add('Carr') # isso é pra mostrar que ele nao vai add iten repetido
print(my_set)

if 'Gui' in my_set:
    print('O nome foi encontrado dentro do conjunto') #O conjunto é usado para consulta, ele responde quase instantaneamente(igual o dict), ele acha mais rapido, pois cada palavra la dentro vira um codigo, então ele vai pra tipo que uma tabela especial

my_set.remove('Carr')
print(my_set)

#--------------------INICIALIZANDO VAZIO--------------------
#list = []
#tuple = ()
#dict = {} or dict()
#set = set()

#--------------------UM DENTRO DO OUTRO--------------------
loucura = [(1,2), (3,4), (5,6), ({'Sh1ro', 'Magisk'}, {'Donk'})]
print(loucura)