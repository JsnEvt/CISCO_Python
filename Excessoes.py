# temperature = float(input('Digite a temperatura atual:'))

# if temperature > 0:
#  print("Acima de zero")
# elif temperature < 0:
#  print("Abaixo de zero")
# else:
#  print("Zero")
 
while True:
    try:
        number = int(input("Insira um número inteiro: "))
        print(number/2)
        break
    except:
        print("Aviso: o valor inserido não é um número válido. Tente novamente...")