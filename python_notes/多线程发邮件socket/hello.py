lista = [1,2,2,2,2,4,4,4,4,4,4,5,5,5,5,5,6,6,7,7,7,8,8,9]
listb = []
for i in lista:
    listb.append(lista.count(i))
print(listb)
print(lista)
dicta = dict(zip(listb, lista))
print('dicta{}'.format(dicta))
listc = []
for i in dicta :
    liste = []
    liste.append(i)
    liste.append(dicta[i])
    listc.append(liste)
print(listc)
listc.sort(reverse=True)
print('listc:{}'.format(listc))
for i in listc :
    print('{}出现了{}次'.format(i[1],i[0]))
#

# set1 = set(listc)
# print('set1{}'.format(set1))
# listd = list(set1)
# # listd = [i for i in set1]
# # listd.sort(reverse=True)
# listd.sort(reverse=True)
# print(listd)
# print(listd[0:3])
# help(list.sort)