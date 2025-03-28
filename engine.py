def run_game(game):
    """Запуск игры с переданной игровой логикой."""
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!\n{game.DESCRIPTION}")

    for _ in range(3):  # Максимальное количество раундов
        question, correct_answer = game.get_question()

        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer == str(correct_answer):
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
