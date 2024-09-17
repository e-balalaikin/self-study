import numpy as np

def game_core_v4(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    # Задаем изначальные значения количества попыток отгадывания, крайние точки диапазона и значение предсказания для запуска цикла
    
    count = 0
    a = 1
    b = 101
    predict = 0

    while number != predict:
        predict = int(round((a+b)/2))
        count += 1
        
        # вставка для отлавливания момента, когда остается всего три числа в диапазоне
        # без нее ломается логика выбора из четырех чисел, превращая одну проверку в трехстадийное отсечение крайних значений
        if (b-a) < 4 and (number == int(b) or number == int(a)):
            break
        
        # подготовка диапазона для следующей итерации
        
        a_temp = a+int(round((b-a)/3))
        b_temp = b-int(round((b-a)/3))
        if number > (b_temp-1):
            """if (b-b_temp) < 2:
                break"""
            a = b_temp
        elif number < a_temp:
            """if (a_temp-a) < 2:
                break"""
            b = a_temp-1
        else:
            """if (b_temp-a_temp) < 2:
                break"""
            a = a_temp
            b = b_temp-1
    return count


def score_game(game_core_v4) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        game_core_v3 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v4(number))

    score = round(np.mean(count_ls),1)
    print(f"Ваш алгоритм угадывает число в среднем за {score} попытки")
    
print('Run benchmarking for game_core_v4: ', end='')
score_game(game_core_v4)