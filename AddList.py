list_1 = [2,1,4,7,8,9,4]
list_2 = [5,3,6,9,7,4,1]


lista_c = []

i = 0 
while i < len(list_1) :
    lista_c.append(list_1[i])
    i = i + 1
x = 0
while x < len(list_2):
    lista_c.append(lista_c[x])
    x = x + 1

print(lista_c)
