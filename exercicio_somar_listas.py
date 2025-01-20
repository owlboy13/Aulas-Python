
def soma_listas(l1,l2):
    soma = []
    for n1, n2 in zip(l1,l2):
        soma.append(n1 + n2)
    return soma


list_1 = [1,2,3,4,5,6,7]
list_2 = [1,2,3,4,]

lista_somada = soma_listas(list_1,list_2)
print()
print("Método com função e zip")
print(list_1)
print(list_2)
print(lista_somada)

print()
print()

#FORMA COM LOOP pode ser troca o range..
# e len pelo enumerate e adicionar uma variavel no loop
listA1 = [1,2,3,4,5,6,7]
listA2 = [1,2,3,4,]

lista_soma = []
for i in range(len(listA2)):
    lista_soma.append(listA1[i]+listA2[i])
print("Método com looping")
print(listA1)
print(listA2)
print(lista_soma)

#Método com list comprehension com zip_longest (captura a lista maior)
from itertools import zip_longest
list_a = [1,2,3,4,5,6,7]
list_b = [1,2,3,4,]
soma_lista = [x + y for x, y in zip_longest(list_a,list_b, fillvalue=0)]
print()
print()
print("Método com list comprehension")
print(list_a)
print(list_b)
print(soma_lista)








