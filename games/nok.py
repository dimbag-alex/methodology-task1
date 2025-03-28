import random
import math

DESCRIPTION = "Find the smallest common multiple of given numbers."

def lcm(a, b):
    """Наименьшее общее кратное (НОК) двух чисел."""
    return abs(a * b) // math.gcd(a, b)

def lcm_of_three(a, b, c):
    """НОК трех чисел."""
    return lcm(lcm(a, b), c)

def get_question():
    """Генерирует случайные числа и их НОК."""
    numbers = [random.randint(1, 100) for _ in range(3)]
    question = " ".join(map(str, numbers))
    correct_answer = lcm_of_three(*numbers)
    return question, correct_answer
