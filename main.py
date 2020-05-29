import math


def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, math.floor(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    answers = []
    for i in [1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]:
        answers.append(is_prime(i))
    print(answers)
