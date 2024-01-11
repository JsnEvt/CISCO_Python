# odd_numbers = 0
# even_numbers = 0
 
# # Leia o primeiro número.
# number = int(input("Digite um número ou digite 0 para parar: "))
 
# # 0 termina a execução.
# while number != 0:
#     # Verifique se o número é ímpar.
#     if number % 2 == 1:
#         # Aumente o contador odd_numbers.S
#         odd_numbers += 1
#     else:
#         # Aumente o contador even_numbers.
#         even_numbers += 1
#     # Leia o número seguinte.
#     number = int(input("Digite um número ou digite 0 para parar: "))
 
# # Imprimir resultados.
# print("Números ímpares contam:", odd_numbers)
# print("Números pares contam:", even_numbers)

#################################


# secret_number = 777


# print(
# """
# +===================================+
# | Bem vindo ao meu jogo, trouxa!    |
# | Insira um número inteiro          |
# | e adivinhar o número que tenho    |
# | escolhidos para você.             |
# | Então, qual é o número secreto?   |
# +===================================+
# """)

# number = int(input("Tente advinhar o numero do mago: "))

# while number != secret_number:
#   print("Ha ha! Você está preso no meu loop!")
#   number = int(input("Tente novamente: "))
#   if(number == secret_number):
#     print("Desmestifiquei o mago!!")
  
  
# import time

# # Escreva um loop for que conte até cinco
# for i in range(1, 6):
#   print(str(i) + " Mississippi")
#   time.sleep(1)
# print("Pronto ou não, aqui vou eu!")

# # Escreva uma função print com a mensagem final.


#BLOCO BREAK

# maior_numero = -99999999
# counter = 0

# while True:
#     number = int(input("Digite um número ou digite -1 para terminar o programa: "))
#     if number == -1:
#         break
#     counter += 1
#     if number > maior_numero:
#         maior_numero = number

# if counter != 0:
#     print("TO maior número é", maior_numero)
# else:
#     print("Você não inseriu nenhum número.")


#BLOCO CONTINUE

# largest_number = -99999999
# counter = 0

# number = int(input("Insira um número ou digite -1 para finalizar o programa: "))

# while number != -1:
#     if number == -1:
#         continue
#     counter += 1

#     if number > largest_number:
#         largest_number = number
#     number = int(input("Insira um número ou digite -1 para finalizar o programa: "))

# if counter:
#     print("O maior número é",  largest_number)
# else:
#     print("Você nnão tem inseriu qualquer número.")


##DECLARACAO BREAK - LAB 3.2.9 - Skillsforall

# palavra = str(input("Insira uma palavra: "))

# while palavra != "chupacabra":
#   palavra = str(input("Insira uma palavra: "))
#   if palavra == "chupacabra":
#     break
# print("Voce saiu do loop com sucesso.")

# ##BLOCO CONTINUE LAB 3.2.10

# word = str(input("Insira uma palavra: "))
# i = 0

# while i < len(word):
#   print(word[i])
#   i +=1

# word = str(input("Digite uma palavra: "))
# vogais = []
# i = 0

# while word :
#   for i in word.__len__:
#     if word[i] == "a" or "e" or "i" or "o" or "u":
#       vogais.append(word[i])
#       word.replace("")
#     continue
#   print("terminado")
  

#CONTAGEM DE BLOCOS - LAB.3.2.14

# count = 0
# lista = []
# total_blocos_usados = 0
# qtd_blocos = int(input("Digite a quantidade blocos: "))

# while qtd_blocos > 0:
#   lista.append(count + 1)
#   count += 1
#   total_blocos_usados = sum(lista)
#   if qtd_blocos < (total_blocos_usados + lista[-1]+1):
#     break
# print("A quantidade de blocos usados foi: ", total_blocos_usados)
# print("A altura da piramide é de: ", len(lista))
    
# for i in range(1, 10):
#   if i % 2 == 0:
#       print(i)
    

#   text = "OpenEDG Python Institute"
# for letter in text:
#     if letter == "P":
#         break
#     print(letter, end="")


# text = "pyxpyxpyx"
# for letter in text:
#     if letter == "x":
#         continue
#     print(letter, end="")
 
#  HIPOTESE DE COLLATZ - LAB.3.2.15
 
c0 = int(input("Digite um numero diferente de zero: "))
valor = 0
valor1 = 0
         
while c0 != 1:
  if c0 % 2 == 0 :
    c0 = c0/2
    print(c0)
    continue
  else:
    c0 = 3*c0+1
    print(c0)
    continue
if c0 == 1.0:
  print("Finalizado.")
    