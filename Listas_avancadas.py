##LIST COMPREENSHIONS

# squares = [x ** 2 for x in range(10)]

# print(squares)

# twos = [2 ** i for i in range(8)]

# print(twos)

# odds = [x for x in squares if x % 2 != 0 ]
# print(odds)

# board = []
# EMPTY = " "
 
# for i in range(8):
#     row = [EMPTY for i in range(8)]
#     board.append(row)
    
# print(board)

# board = [[EMPTY for i in range(8)] for j in range(8)]

# board = [[EMPTY for i in range(8)] for j in range(8)]
# board[0][0] = "ROOK"
# board[0][7] = "ROOK"
# board[7][0] = "ROOK"
# board[7][7] = "ROOK"
# board[4][2] = "KNIGHT"
# board[3][4] = "PAWN"

# print(board)

# temps = [[0.0 for h in range(24)] for d in range(31)]
# print(temps)

#NATUREZA MULTIDIMENSIONAL DAS LISTAS:

# temps = [[0.0 for h in range(24)] for d in range(31)]

# temps = [[0.0 for h in range(24)] for d in range(31)]
# #
# # A matriz é magicamente atualizada aqui.
# #
 
# total = 0.0
 
# for day in temps:
#     total += day[11]
 
# average = total / 31
 
# print("Temperatura média ao meio-dia:", average)

# temps = [[0.0 for h in range(24)] for d in range(31)]
#
# A matriz é magicamente atualizada aqui.
#
 
# highest = -100.0
 
# for day in temps:
#     for temp in day:
#         if temp > highest:
#             highest = temp
 
# print("A maior temperatura foi:", highest)

# temps = [[0.0 for h in range(24)] for d in range(31)]
# #
# A matriz é magicamente atualizada aqui.
#
 
# hot_days = 0
 
# for day in temps:
#     if day[11] > 20.0:
#         hot_days += 1
 
# print(hot_days, "dias estavam quentes.")
 
 
#  # MATRIZ TRIDIMENSIONAL
 
#  rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
 
# # Verifique se há vagas no 15º andar do terceiro edifício:

# vacancy = 0
 
# for room_number in range(20):
#     if not rooms[2][14][room_number]:
#         vacancy += 1


##################

# var = 1
# while var < 10:
#     print("#")
#     var = var << 1
# #NESTE EXERCICIO ACIMA, A CONTAGEM FOI BIT A BIT

# z = 10
# y = 0
# x = y < z and z > y or y > z and z < y
# print(x)

# nums = [1, 2, 3]
# vals = nums[-3:-1]
# print(vals)

#E IMPORTANTE OBSERVAR A ORDEM OS INDICES QUANDO RETORNAMOS UMA LISTA.
#PARA FUNCIONAR, O INDICE DO COMECO TEM QUE SER MAIOR(NEGATIVAMENTE)
#DO QUE O FINAL.

# my_list_1 = [1, 2, 3]
# my_list_2 = []
# for v in my_list_1:
#     my_list_2.insert(0, v)
# print(my_list_2)


# NAO CONSIGO ENTENDER PQ ELE REPETE O VALOR INICIAL VARIAS VEZES
# E NAO PEGA O VALOR DO MOMENTO PARA REPOSICIONAR NO INDICE CERTO.
# my_list = [1, 2, 3, 4, 5]
# for v in range(len(my_list)):
#     my_list.insert(1, my_list[v])
# print(my_list)

# RETORNO: [1, 1, 1, 1, 1, 1, 2, 3, 4, 5]


########################

# t = [[3-i for i in range (3)] for j in range (3)]
# s = 0
# for i in range(3):
#     s += t[i][i]
# print(s)

# saida t = [[3, 2, 1], [3, 2, 1], [3, 2, 1]]

my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list[2][0])

#CAUSARA ERRO.