def has_only_2_and_3_as_factors(n):
    """检查一个数是否只含有2和3作为质因数"""
    while n % 2 == 0:
        n //= 2
    while n % 3 == 0:
        n //= 3
    return n == 1

def factorize_to_2_and_3(n):
    """将一个数分解为2和3的幂次形式"""
    x, y = 0, 0
    while n % 2 == 0:
        n //= 2
        x += 1
    while n % 3 == 0:
        n //= 3
        y += 1
    return x, y

def find_numbers():
    """查找所有因子只有2和3的数，并表示为2^x * 3^y的形式"""
    numbers = []
    for n in range(500, 3500):  # 包含1500
        if has_only_2_and_3_as_factors(n):
            x, y = factorize_to_2_and_3(n)
            numbers.append((n, x, y))
    return numbers

# 主程序
if __name__ == "__main__":
    numbers = find_numbers()
    if numbers:
        print("Numbers with only 2 and 3 as factors between 500 and 1500:")
        for n, x, y in numbers:
            print(f"{n} = 2^{x} * 3^{y}")
    else:
        print("No numbers with only 2 and 3 as factors found within the given range.")