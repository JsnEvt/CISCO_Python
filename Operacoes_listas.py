# list = [1,2,3,4,5,6]
# new_list = list[:]
# print(new_list)

# my_list = [10, 8, 6, 4, 2,1,9,7]
# new_list = my_list[1:-2]
# print(new_list)

# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest = my_list[0]
 
# for i in my_list[1:]:
#     if i > largest:
#         largest = i
        

# print(my_list[1:]) 
# print(largest)
# print(len(my_list))

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# to_find = 5
# found = False
 
# for i in range(len(my_list)):
#     found = my_list[i] == to_find
#     if found:
#         break
 
# if found:
#     print("Elemento encontrado no índice", i)
# else:
#     print("ausente")

# drawn = [5, 11, 9, 42, 3, 49]
# bets = [3, 7, 11, 42, 34, 49]
# hits = 0
 
# for number in bets:
#     if number in drawn:
#         hits += 1
 
# print(hits)

#LAB 3.6.6 - OPERACOES COM LISTAS
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9,100,25,90,79,34,64,76,58,25,25,25,79,34,64]
list2 = []
indice = 0

for i in range(len(my_list)):
    if my_list[i] not in list2:
        list2.append(my_list[i])
list2.sort()
print(list2)


list_1 = ["A", "B", "C"]
list_2 = list_1[:] # O COLCHETES COM OS 2 PONTOS CRIA UMA NOVA LISTA.
list_3 = list_2[:]
print(list_2)
print(list_3)

 
del list_1[0]
del list_2[0]
 
print(list_3)
print(list_1)
print(list_2)
    