slogan = 'hello world, that is my python code, have fun !!'
print(slogan)
print(slogan.upper())
print(slogan.lower())
print(slogan[0]) #print in slogan just the first letter (letter number 0).
print(slogan[0:5]) #print the index inside couchettes RANGE.
print(slogan[::-1]) #Slogan invert

slogan_divider = slogan.split(',') #the parameter: where gonna split(separate) the slogan.
print(slogan_divider)

#####################################################################################

list_name = ['Dario', 'Ju', 'Ana', 'Dario Junior','Ju', 'Dario Junior']
list_name.append('Barbara') #add item in the last index.
list_name.append('Friday') #add item in the last index.
list_name.remove('Dario') #remove
list_name.insert(0, 'Jesus') # parameter(INDEX, Object)
#CLEAR THE LIST ---- list_name.clear()

count_name = list_name.count('Dario Junior')

print(list_name)
print(list_name[3]) #print the index inside couchettes.
print(list_name[0:3]) #print the index inside couchettes RANGE.
print(list_name[-1]) #print the last index (use if the list so far).
print(len(list_name)) #Len = length = size
print(count_name) #count name in variable