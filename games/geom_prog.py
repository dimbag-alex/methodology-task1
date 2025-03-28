import random

DESCRIPTION = "What number is missing in the progression?"

def generate_geometric_progression():
    """Создает геометрическую прогрессию и скрывает случайный элемент."""
    length = random.randint(5, 10)
    first_term = random.randint(1, 10)
    ratio = random.randint(2, 5)
    progression = [first_term * (ratio ** i) for i in range(length)]

    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."

    question = " ".join(map(str, progression))
    return question, correct_answer

def get_question():
    """Возвращает вопрос и правильный ответ."""
    return generate_geometric_progression()
