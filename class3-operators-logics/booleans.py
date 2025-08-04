#BOOLEAN DATAS
# Comparative signals   ==(same), !=(dif), >(more than), <(less than), >=(more or same), <=(less or same), and (and lol).
# Use NOT before True or False to invert the values.

var_true = True
var_false = False
#
# print(var_true)
# print(var_false)
# print(type(var_true))
# print(type(var_false))

# if var_true == True: # pt-br aqui usamos o == para realmente igualar um valor, ou seja, o == é para comparar um valor, o = é para atribuir.
#     print('var_true is truthy')

a = 9
b = 8
age = 22

if a > b:
    print( a, 'is more than number', b)
else:
    print( a, 'is less than number', b )

if age == 22:
    print(' U have 22 years old')
else:
    print(' U dont have 22 years old')