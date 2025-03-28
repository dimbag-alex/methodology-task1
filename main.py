import engine
import games.nok as nok
import games.geom_prog as progression

GAMES = {
    "1": ("НОК", nok),
    "2": ("Геометрическая прогрессия", progression),
}

def main():
    print("Выберите игру:")
    for key, (name, _) in GAMES.items():
        print(f"{key}. {name}")

    choice = input("Введите номер игры: ").strip()
    game = GAMES.get(choice)

    if game:
        _, game_module = game
        engine.run_game(game_module)
    else:
        print("Некорректный выбор.")

if __name__ == "__main__":
    main()
