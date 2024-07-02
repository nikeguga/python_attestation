import logging
import sys

class LotteryGame:
# Класс для сравнения лотерейных билетов.

    def __init__(self, ticket, winning_numbers):
        """
        Конструктор класса.
        """
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        stream_handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        try:
            self.ticket = self.parse_numbers(ticket)
            self.winning_numbers = self.parse_numbers(winning_numbers)
        except ValueError as e:
            logger.error(f"Ошибка при парсинге чисел: {e}")
            sys.exit(1)
        except Exception as e:
            logger.exception(f"Непредвиденная ошибка: {e}")
            sys.exit(1)


    def parse_numbers(self, numbers_str):
        """
        Парсит строку с числами в список чисел.
        """
        try:
            numbers = [int(number) for number in numbers_str.split()]
            return numbers
        except ValueError:
            raise ValueError("Ожидается строка с целыми числами, разделенными пробелами.")


    def compare_lists(self):
        """
        Сравнивает числа в билете и выпавшие числа.
        """
        matching_numbers = []
        for number in self.ticket:
            if number in self.winning_numbers:
                matching_numbers.append(number)

        if matching_numbers:
            logger.info(f"Совпадающие числа: {matching_numbers}")
            print(f"Совпадающие числа: {matching_numbers}\nКоличество совпадающих чисел: {len(matching_numbers)}")
        else:
            logger.info("Совпадающих чисел нет.")
            print("Совпадающих чисел нет.")


def main():
    """
    Основная функция программы.
    """
    if len(sys.argv) != 3:
        print("Использование: lottery_game.py <ваш_билет> <выпавшие_числа>")
        sys.exit(1)

    ticket_str = sys.argv[1]
    winning_numbers_str = sys.argv[2]

    game = LotteryGame(ticket_str, winning_numbers_str)
    game.compare_lists()


if __name__ == "__main__":
    main()
