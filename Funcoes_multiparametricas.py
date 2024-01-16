# TRIANGULO RETANGULO

# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b
 
 
# def is_a_right_triangle(a, b, c):
#     if not is_a_triangle(a, b, c):
#         return False
#     if c > a and c > b:
#         return c ** 2 == a ** 2 + b ** 2
#     if a > b and a > c:
#         return a ** 2 == b ** 2 + c ** 2

# print(is_a_right_triangle(5, 3, 4))
# print(is_a_right_triangle(1, 3, 4))



# CALCULANDO A AREA DE UM TRIANGULO
# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b
 
 
# def heron(a, b, c):
#     p = (a + b + c) / 2
#     return (p * (p - a) * (p - b) * (p - c)) ** 0.5
 
 
# def area_of_triangle(a, b, c):
#     if not is_a_triangle(a, b, c):
#         return None
#     return heron(a, b, c)
 
 
# print(area_of_triangle(1., 1., 2. ** .5))

##FUNCAO FATORIAL

# def factorial_function(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
 
#     product = 1
#     for i in range(2, n + 1):
#         product *= i
#     return product
 
 
# for n in range(1, 6): # testando
#     print(n, factorial_function(n))

#NUMEROS DE FIBONACCI

# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1
 
#     elem_1 = elem_2 = 1
#     the_sum = 0
#     for i in range(3, n+1):
#         the_sum = elem_1 + elem_2
#         elem_1, elem_2 = elem_2, the_sum
#     return the_sum
 
 
# for n in range(1,10): # testando
#     print(n, "->", fib(n))

##RECURSAO - USANDO A MESMA FORMULA ANTERIOR.

# def factorial_function(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
#     return n * factorial_function(n - 1)


def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)
 
 
print(fun(25)) # RESULTADO = 56
