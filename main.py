from statistic import generate_statistic_avg_time, generate_statistic_accuracy, generate_statistic_most_prios
from file_handler import FileHandler
from task_manager import TaskManager, spliter


def switch_case(number):
    match number:
        case 1:
            spliter()
            show_number = int(input('1 - wyswietl wszystkie zadania: \n'
                                    '2 - filtruj zadania: \n'))
            if show_number == 1:
                task_manager.show_all_tasks()
            else:
                spliter()
                filter_number = int(input('1 - filtruj po priorytecie: \n'
                                         '2 - filtruj po terminie wykonania: \n'
                                         '3 - filtruj po statusie: '))
                if filter_number == 1:
                    task_manager.show_tasks_by_prio()
                elif filter_number == 2:
                    task_manager.show_tasks_by_deadline()
                elif filter_number == 3:
                    task_manager.show_tasks_by_status()
                else:
                    spliter()
                    print('xxx')
        case 2:
            task_manager.add_task()
        case 3:
            spliter()
            task_name = input('wprowadz nazwe zadania: ')
            task_manager.delete_task(task_name)
        case 4:
            spliter()
            task_manager.edit_task()
        case 5:
            spliter()
            task_name = input('wprowadz nazwe zadania: ')
            task_manager.make_task_done(task_name)
        case 6:
            spliter()
            statistic_number = int(input('1 - pokaz sredni czas wykonania zadania: \n'
                                         '2 - pokaz procentowe zakonczenie zadan na czas: \n'
                                         '3 - pokaz najczestsze priorytety: \n'))
            if statistic_number == 1:
                generate_statistic_avg_time()
            if statistic_number == 2:
                generate_statistic_accuracy()
            if statistic_number == 3:
                generate_statistic_most_prios()
        case 7:
            exit(0)
        case _:
            spliter()
            print('xxx')


filepath = input('podaj sciezke do pliku z zadaniami: ')
print()
filepath = filepath.replace('"', '')
file_handler = FileHandler(filepath)
task_manager = TaskManager(file_handler)

while True:
    number = int(input('1 - pokaz swoje zadania: \n'
                       '2 - dodaj zadanie: \n'
                       '3 - usun zadanie: \n'
                       '4 - edytuj zadanie: \n'
                       '5 - zaznacz zadanie jako wykonane: \n'
                       '6 - pokaz statystyki: \n'
                       '7 - exit: '))
    switch_case(number)