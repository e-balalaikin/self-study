import numpy as np

def game_core_v3(number: int = 1) -> int:
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

    while number != predict: # в цикле присваиваем неугаданное значение в качестве левой или правой границы диапазона
        
        predict = int((a+b)/2) # если это значение окажется верным, то при след итерации цикл остановится
        count += 1
        
        # подготовка диапазона для следующей итерации
        
        if number > predict:
            a = int(predict)
        elif number < predict:
            b = int(predict)
    
    # как только происходит совпадение, цикл останавливается и функция отдает значение счетчика попыток
    return count


def score_game(game_core_v3) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        game_core_v3 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = round(np.mean(count_ls),1)
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    
print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)