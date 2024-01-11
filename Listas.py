

# # #LABORATORIO 3.4.6 BASICO DE LISTAS

# # lista = [1,2,3,4,5]
# # subst = int(input("Insira um numero: "))

# # lista[2] = subst
# # print(lista)

# # del(lista[-1])
# # print(lista)

# # print(len(lista))

# # lista.insert(lista[1], 5)
# # print(lista)

# # ## SOMANDO O TOTAL DOS ELEMENTOS DA LISTA:

# # my_list = [10, 1, 8, 3, 5]

# # total = 0

# # for i in range(len(my_list)):

# #   total += my_list[i]

# # print(total)

# # total_lista = sum(my_list)
# # print(total_lista)

# my_list = [1,2,3,4,5,6,7,8,9,10,11]
# my_original_list = [1,2,3,4,5,6,7,8,9,10]
 
# # my_list[0], my_list[4] = my_list[4], my_list[0]
# # my_list[1], my_list[3] = my_list[3], my_list[1]
 
# # print(my_list)

# for i in range(len(my_list)//2):
#     my_list[i], my_list[len(my_list) - i - 1] = my_list[len(my_list) - i - 1], my_list[i]
 
# print(my_original_list)
# print(my_list)

# ##LAB 3.4.11 - BASICO LISTAS - OS BEATLES

# beatles = []

# print("Etapa 1:", beatles)

# beatles.append("John Lennon" )
# beatles.append("Paul McCartney" )
# beatles.append("George Harrison" )

# print("Etapa 2:", beatles)



# lista_musicos = []


# for i in range(2):
#     musicos = input("Insira mais 1 musico")
#     lista_musicos.append(musicos)
#     beatles.append(lista_musicos[i])

# print("Etapa 3:", beatles)

# del(beatles[4])
# del(beatles[3])


# print("Etapa 4:", beatles)

# beatles.insert(0, "Ringo Starr")

# print("Etapa 5:", beatles)



# # testando o tamanho da lista

# ("o fabuloso", len(beatles))


lista = [[1,2,3,4,5,6],[7,8,[10,11,12],9]]

print(lista[0])
print(lista[1][2][0])

 
lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst))
print(len(lst))