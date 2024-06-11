from task import Task
from datetime import datetime


def spliter():
    print('----------------------------------------------------------------------------')


class TaskManager:
    """
    this class contains much methods that allow to managing tasks
    """

    def __init__(self, file_handler):
        self.file_handler = file_handler
        self.tasks = self.file_handler.load_from_file()

    def add_task(self):

        """
        this method adds a task to the tasks list and to the task file
        :return: void
        """

        task_name = input("wprowadz nazwe zadania: ")
        describtion = input("wprowadz opis zadania: ")
        prio = input("wprowadz priorytet zadania: ")
        category = input("wprowadz kategorie zadania: ")
        year = int(input('wprowadz rok deadlinu: '))
        month = int(input('wprowadz miesiac deadlinu: '))
        day = int(input('wprowadz dzien deadlinu: '))
        deadline = datetime(year, month, day)
        today = datetime.today()
        t_year = today.year
        t_month = today.month
        t_day = today.day
        date_of_insertion = datetime(t_year, t_month, t_day)
        if deadline >= today:
            is_active = True
        else:
            is_active = False
        self.file_handler.save_to_file(
            Task(task_name, describtion, prio, category, deadline, is_active, date_of_insertion))
        self.file_handler.save_statistic('prios', prio)
        self.tasks.append(Task(task_name, describtion, prio, category, deadline, is_active, date_of_insertion))
        spliter()

    def delete_task(self, task_name: str):

        """
        this method removes task from the task list and from the task file
        :param task_name: this variable is used to find wanted task
        :return: void
        """

        for task in self.tasks:
            if task.task_name == task_name:
                self.tasks.remove(task)
                break

        self.file_handler.clear_file()
        for t in self.tasks:
            self.file_handler.save_to_file(t)
        print('ZADANIE USUNIETE !')
        spliter()

    def edit_task(self):

        """
        this method edits tasks by task_name, deadline, describtion or category
        :return: void
        """

        task_name = input('wprowadz nazwe zadania do zedytowania: ')
        isExists = False
        for i in self.tasks:
            if i.task_name == task_name:
                task = i
                isExists = True
                break

        if not isExists:
            spliter()
            print('nie ma takiego zadania')
            spliter()
            return

        afix = input("co chcesz zedytowac: ")
        if not afix == 'termin_wykonania':
            new_afix = input("nowy afix: ")
        if afix == 'nazwa_zadania':
            task.task_name = new_afix
        elif afix == 'opis':
            task.describtion = new_afix
        elif afix == 'priorytet':
            task.prio = new_afix
        elif afix == 'termin_wykonania':
            year = input('rok: ')
            month = input('miesiac: ')
            day = input('dzien: ')
            task.deadline = datetime(int(year), int(month), int(day))
        elif afix == 'kategoria':
            task.category = new_afix
        else:
            print("nie ma takiego afixu zadania")

        self.file_handler.clear_file()
        for t in self.tasks:
            self.file_handler.save_to_file(t)
        print('ZADANIE ZOSTALO ZEDYTOWANE !')
        spliter()


    def make_task_done(self, task_name: str):

        """
        this method is changing task value variable that is corresponding to the avaibility of the task
        :param task_name: this variable is used to find wanted task
        :return: void
        """

        for t in self.tasks:
            if t.task_name == task_name:
                t.is_active = False
                self.file_handler.clear_file()
                for task in self.tasks:
                    self.file_handler.save_to_file(task)
                break

        for task in self.tasks:
            if task.task_name == task_name:
                dt_now = datetime.today()
                t_year = int(task.date_of_insertion.split('-')[0])
                t_month = int(task.date_of_insertion.split('-')[1])
                t_day = int(task.date_of_insertion.split('-')[2].split(' ')[0])
                t_dt = datetime(t_year, t_month, t_day)
                task_time = dt_now - t_dt

                task_days = task_time.days
                task_seconds = 0
                while task_days > 0:
                    task_seconds += 86400
                    task_days -= 1
                self.file_handler.save_statistic('task_time', task_time.seconds)

                t_year = int(task.deadline.split('-')[0])
                t_month = int(task.deadline.split('-')[1])
                t_day = int(task.deadline.split('-')[2].split(' ')[0])
                t_dt = datetime(t_year, t_month, t_day)
                if t_dt > dt_now:
                    self.file_handler.save_statistic('on_time', 'y')
                else:
                    self.file_handler.save_statistic('on_time', 'n')

        print('ZADANIE ZOSTALO ZAKONCZONE !')
        spliter()

    def show_all_tasks(self):

        """
        this method shows on cmd all tasks from the file & task list
        :return: void
        """

        print('\t\t\t\t\t|LISTA ZADAN| ')
        spliter()
        for task in self.tasks:
            print(task)
            print()
        spliter()

    def show_tasks_by_prio(self):

        """
        this method shows on cmd all task that are match the given filter
        :return: void
        """

        spliter()
        prio = input('podaj priorytet: ')
        spliter()
        print('\t\t\t\t|LISTA ZADAN Z PODANYM PRIORYTETEM| ')
        for task in self.tasks:
            if task.prio == prio:
                print(task)
                print()
        spliter()

    def show_tasks_by_deadline(self):

        """
        this method shows on cmd all task that are match the given filter
        :return: void
        """

        spliter()
        year = int(input('rok: '))
        month = int(input('miesiac: '))
        day = int(input('dzien: '))
        dt = datetime(year, month, day)
        spliter()
        print(f'\t\t\t\t|LISTA ZADAN DO ZROBIENIA PRZED {dt}|')
        for task in self.tasks:
            t_year = int(task.deadline.split('-')[0])
            t_month = int(task.deadline.split('-')[1])
            t_day = int(task.deadline.split('-')[2].split(' ')[0])
            t_dt = datetime(t_year, t_month, t_day)
            if t_dt < dt:
                print(task)
                print()
        spliter()

    def show_tasks_by_status(self):

        """
        this method shows on cmd all task that are match the given filter
        :return: void
        """

        spliter()
        is_active = input('True/False')
        if is_active == 'True':
            spliter()
            print('\t\t\t\t\t|LISTA AKTYWNYCH ZADAN| ')
            for task in self.tasks:
                if task.is_active:
                    print(task)
                    print()
            spliter()
        else:
            spliter()
            print('\t\t\t\t\t|LISTA NIEAKTYWNYCH ZADAN| ')
            for task in self.tasks:
                if not task.is_active:
                    print(task)
                    print()
        spliter()
