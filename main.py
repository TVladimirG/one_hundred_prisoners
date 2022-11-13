import random

total_prisoners = 100
total_prison = 100
max_attempts = round(total_prisoners / 2, 0)
list_prisoners = list(range(1, total_prisoners + 1))



def start_game():
    boxes = get_boxes()
    for number_prisoner in range(1, total_prisoners + 1):
        # Очередной заключенный отправляется в комнату с коробками
        # Смотрим повезет ли текущему узнику
        win = visit_the_box_room(boxes, str(number_prisoner))

        if not win:
            # Если не повезло одному то сразу конец игры
            return False

    # Всем заключенным повезло!
    return True


def visit_the_box_room(boxes, number_prisoner):
    # Мы в комнате с коробками
    # Открываем коробку с номером заключенного и получаем номер в коробки
    number_in_box = boxes.get(number_prisoner)
    total_attempt = 1

    # Если номер в коробке не совпадает с номером заключенного то идем к коробке номер которой мы вытащили
    # и так пока не найдем свой номер или пока не откроем максимально допустимое число коробок
    while number_in_box != number_prisoner:
        total_attempt += 1

        # Максимально допустимое число коробок
        if total_attempt > max_attempts:
            return False  # Не Повезло, тогда вообще конец игры

        # идем к коробке номер котой мы вытащили и открываем её
        number_in_box = boxes.get(number_in_box)

    return True  # Повезло


def get_boxes():
    boxes = {}
    random.shuffle(list_prisoners)
    for i in range(0, total_prisoners):
        key = i + 1
        boxes[str(key)] = str(list_prisoners[i])

    return boxes


def main():
    total_win: int = 0
    total_lost: int = 0

    # По очереди все тюрьмы
    for number_prison in range(1, total_prison + 1):
        win = start_game()

        if not win:
            total_lost += 1
        else:
            total_win += 1

    print(f'Всего тюрем {total_prison} в каждой по {total_prisoners} заключенных')
    print(f'успех / произрыш = {total_win} / {total_lost}')
    print(f"Шанс на успех = {round(total_win / total_prison * 100, 1)} %")


if __name__ == '__main__':
    main()
