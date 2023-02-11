# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

N = int(input())

def get_prime(N):
    factors = list()
    divisor = 2
    while divisor <= N:
        if (N % divisor == 0):
            factors.append(divisor)
            N = N/divisor
        else:
            divisor += 1
    return factors

print(get_prime(N))



# list = [i for i in range(2,n)]

# def is_prime(x):
#     count = 0
#     for i in range(2, n):
#         if x % i == 0:
#             count += 1
#     if count > 1:
#         return False
#     else:
#         return True
    
# simplelist = []
# for i in range(len(list)):
#     if is_prime(list[i]) == True:
#         simplelist.append(list[i])

# def N(x,list):
#     for i in simplelist:


# print(list)
# print(simplelist)

