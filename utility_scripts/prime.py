import math

def is_prime(num):
    """ 判断一个数是否是素数 """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_prime_q(n):
    """ 查找最小的素数 q 使得 q - 1 能够被 n 整除 """
    k = 1
    L = []
    while k<20:
        candidate = k * n + 1
        if is_prime(candidate):
            L.append(candidate)
        k += 1
    return L

# 示例：查找一个素数 q 使得 q - 1 能够被 n 整除
n = 256
L = find_prime_q(n)
for q in L:
    print(f" {n} , {q}")

# L = []
# for k in range(11):
#     for l in range(4):
#         n = 2**k*3**l
#         if n<1152 and n>128:
#             L.append((n,k,l))

# for (n,k,l) in L:
#     print(n,"k=",k,"l=",l)