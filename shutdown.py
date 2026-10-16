import os
import sys


def clear_console():
    """Очищает консоль в зависимости от ОС."""
    os.system("cls" if os.name == "nt" else "clear")


def main():
    while True:
        clear_console()
        print("=" * 45)
        print("   ИНСТРУКЦИЯ ПО УПРАВЛЕНИЮ ТАЙМЕРОМ ПК")
        print("=" * 45)
        print("1. Введите время в МИНУТАХ для запуска таймера.")
        print("2. Чтобы выйти из программы, введите 'q'.\n")

        user_input = input("Введите время (мин) и нажмите Enter: ").strip()

        if user_input.lower() == "q":
            print("Завершение работы программы...")
            sys.exit()

        if not user_input.isdigit() or int(user_input) <= 0:
            input(
                "\nОшибка: Введите целое положительное число! Нажмите Enter для повтора..."
            )
            continue

        minutes = int(user_input)
        seconds = minutes * 60

        # Запуск таймера выключения через системную команду Windows
        os.system(f"shutdown /s /t {seconds}")

        # Обновление экрана
        clear_console()
        print("=" * 45)
        print(f" STATUS: Таймер успешно запущен на {minutes} мин.")
        print("=" * 45)
        print("\nВы хотите отменить таймер выключения?")
        print("1 — Да, отменить таймер и вернуться в меню")
        print("2 — Нет, оставить таймер и закрыть программу\n")

        choice = input("Выберите действие (1 или 2): ").strip()

        if choice == "1":
            # Отмена выключения
            os.system("shutdown /a")
            input("\nТаймер отменен! Нажмите Enter, чтобы вернуться в меню...")
        else:
            print("\nТаймер активен. Программа закрывается.")
            break


if __name__ == "__main__":
    main()
