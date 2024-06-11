from collections import Counter


def generate_statistic_avg_time():

    """
    this method load and count statistic about avg time that user need to complete tasks
    :return: void
    """

    with open('statistic.txt', 'r') as file:
        lines = file.readlines()

    task_times = []

    for line in lines:
        if line.startswith('task_time:'):
            times_str = line[len('task_time:'):]
            times_list = times_str.split(';')
            for time in times_list:
                if time:
                    task_times.append(int(time))
        break

    if task_times:
        average_time_seconds = sum(task_times) / len(task_times)
    else:
        average_time_seconds = 0

    hours = int(average_time_seconds // 3600)
    minutes = int((average_time_seconds % 3600) // 60)
    seconds = int(average_time_seconds % 60)

    result_string = f"Średni czas: {hours} godzin, {minutes} minut, {seconds} sekund"

    print(result_string)


def generate_statistic_accuracy():

    """
    this method load and count statistic about accuracy that user has about doing his tasks on time
    :return: void
    """

    with open('statistic.txt', 'r') as file:
        lines = file.readlines()

    n_list = []
    y_list = []

    for line in lines:
        if line.startswith('on_time:'):
            values_str = line[len('on_time:'):]
            values_list = values_str.split(';')
            for value in values_list:
                if value == 'n':
                    n_list.append(value)
                elif value == 'y':
                    y_list.append(value)
            break

    accuracy = len(y_list) / len(n_list) * 100
    result_string = f"masz: {accuracy:.2f}% zadan ukonczonych na czas"

    print(result_string)


def generate_statistic_most_prios():

    """
    this method load and count statistic most common priorities that user inserted into his tasks
    :return: void
    """

    with open('statistic.txt', 'r') as file:
        lines = file.readlines()

    most_common = []

    for line in lines:
        if line.startswith('prios:'):
            words_str = line[len('prios:'):].strip()
            words_list = words_str.split(';')
            word_counter = Counter(words_list)
            most_common = word_counter.most_common(3)
            break

    result_string = f"twoje najczestsze priorytety to: {most_common[0]}, {most_common[1]}, {most_common[2]}"

    print(result_string)

