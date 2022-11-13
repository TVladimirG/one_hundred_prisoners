import random

total_prisoners: int = 100
total_prison: int = 100
max_attempts: int = round(total_prisoners / 2)
list_prisoners: list[int] = list(range(1, total_prisoners + 1))
boxes: dict[int, int] = {}


def start_game() -> bool:
    # Заполним коробки номерами
    init_boxes()
    for number_prisoner in range(1, total_prisoners + 1):
        # Очередной заключенный отправляется в комнату с коробками
        win = visit_the_box_room(number_prisoner)

        # Если не повезло хотябы одному то сразу конец игры
        if not win:
            return False

    # Всем заключенным повезло!
    return True


def visit_the_box_room(number_prisoner):
    # Мы в комнате с коробками

    # Если номер в очередной коробке не совпадает с номером заключенного то он идет к коробке номер которой мы вытащили
    # и так пока не найдем свой номер или пока не откроет максимально допустимое число коробок

    # Начинаем открывать коробку за коробкой, начиная со своего номера
    number_in_box = number_prisoner
    for _ in range(0, max_attempts):
        # Здесь красивее было бы использовать while - но он работает ощутимо дольше

        # Открыли коробку и получили номер
        number_in_box = open_box(number_in_box)  # type: ignore

        # Сверяем номер с номером заключенного
        if number_in_box is not None and number_in_box == number_prisoner:  # Повезло!!!
            return True

    # Посмотрели максимально допустимое число коробок
    # Это означает, что не повезло вообще всем заключенным, это конец игры
    return False


def open_box(number_in_box):
    return boxes.get(number_in_box)


def init_boxes() -> dict[int, int]:
    random.shuffle(list_prisoners)
    for i in range(0, total_prisoners):
        key: int = i + 1
        # boxes[str(key)] = str(list_prisoners[i])
        boxes[key] = list_prisoners[i]

    return boxes


def main():
    total_win: int = 0
    total_lost: int = 0

    # По очереди все тюрьмы
    for _ in range(0, total_prison):
        win: bool = start_game()

        if not win:
            total_lost += 1
        else:
            total_win += 1

    print(
        f'Всего тюрем {total_prison} в каждой по {total_prisoners} заключенных')
    print(f'Выиграно / проиграно = {total_win} / {total_lost}')
    print(f"Шанс на успех = {round(total_win / total_prison * 100, 1)} %")


if __name__ == '__main__':
    main()
