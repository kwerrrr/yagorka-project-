"""
Модуль для учета личных финансов.
Позволяет добавлять расходы, просматривать операции и сохранять данные в JSON.
"""

import json
from datetime import datetime
from typing import List, Dict, Any

DATA_FILE = "finance_data.json"
transactions: List[Dict[str, Any]] = []


def load_data() -> None:
    """
    Загружает данные о транзакциях из JSON-файла.

    При отсутствии файла создает пустой список транзакций.
    Обрабатывает ошибки чтения файла и некорректного формата JSON.
    """
    global transactions

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            transactions = json.load(file)
        print("✅ Данные загружены!")

    except FileNotFoundError:
        print("📁 Файл данных не найден. Начинаем с чистого листа.")
        transactions = []

    except json.JSONDecodeError:
        print("❌ Ошибка: файл поврежден или имеет некорректный формат.")
        transactions = []

    except Exception as error:
        print(f"❌ Неизвестная ошибка при загрузке: {error}")
        transactions = []


def save_data() -> bool:
    """
    Сохраняет данные о транзакциях в JSON-файл.

    Returns:
        bool: True если сохранение успешно, False при ошибке.
    """
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(transactions, file, ensure_ascii=False, indent=4)
        print("💾 Данные сохранены!")
        return True

    except IOError as error:
        print(f"❌ Ошибка записи в файл: {error}")
        return False

    except Exception as error:
        print(f"❌ Неизвестная ошибка при сохранении: {error}")
        return False


def add_expense() -> None:
    """
    Добавляет новую запись о расходе.

    Запрашивает у пользователя сумму, категорию и описание.
    Проверяет корректность ввода суммы.
    """
    print("\n" + "=" * 30)
    print("ДОБАВЛЕНИЕ РАСХОДА")
    print("=" * 30)

    # Ввод и валидация суммы
    while True:
        amount_input = input("Введите сумму расхода: ").strip()
        try:
            amount = float(amount_input)
            if amount <= 0:
                print("❌ Сумма должна быть положительным числом!")
                continue
            break
        except ValueError:
            print("❌ Пожалуйста, введите число (например: 1500.50)")

    # Ввод категории
    category = input("Введите категорию (еда, транспорт, развлечения): ").strip()
    if not category:
        category = "без категории"

    # Ввод описания
    description = input("Введите описание (не обязательно): ").strip()

    # Создание новой транзакции
    new_transaction = {
        "id": len(transactions) + 1,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": "расход",
        "amount": amount,
        "category": category,
        "description": description,
    }

    transactions.append(new_transaction)
    print(f"\n✅ Расход '{category}' на сумму {amount:.2f} руб. добавлен!")


def show_all() -> None:
    """
    Отображает все финансовые операции в табличном формате.

    При отсутствии операций выводит информационное сообщение.
    """
    if not transactions:
        print("\n📭 Список операций пуст.")
        return

    print("\n" + "=" * 70)
    print("ВСЕ ФИНАНСОВЫЕ ОПЕРАЦИИ")
    print("=" * 70)
    print(
        f"{'№':<4} {'Дата':<19} {'Тип':<8} {'Сумма':<12} {'Категория':<15} {'Описание'}"
    )
    print("-" * 70)

    for i, transaction in enumerate(transactions, 1):
        print(
            f"{i:<4} "
            f"{transaction.get('date', 'N/A'):<19} "
            f"{transaction.get('type', 'N/A'):<8} "
            f"{transaction.get('amount', 0):<12.2f} "
            f"{transaction.get('category', 'N/A'):<15} "
            f"{transaction.get('description', '')}"
        )


# Основной блок программы (пример использования)
if __name__ == "__main__":
    load_data()

    while True:
        print("\nМеню:")
        print("1. Добавить расход")
        print("2. Показать все операции")
        print("3. Сохранить данные")
        print("4. Выход")

        choice = input("Выберите действие(1-4): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_all()
        elif choice == "3":
            save_data()
        elif choice == "4":
            save_data()
            print("👋 Выход из программы.")
            break
        else:
            print("❌ Неверный выбор! Пожалуйста, выберите действие от 1 до 4.")
