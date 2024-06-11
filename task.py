from datetime import datetime


class Task:

    """
    this class is used as data structure for tasks
    """

    def __init__(self, task_name: str, describtion: str, prio: str, category: str, deadline: datetime, is_active: bool, date_of_insertion: datetime):
        self.task_name = task_name
        self.describtion = describtion
        self.prio = prio
        self.deadline = deadline
        self.category = category
        self.is_active = is_active
        self.date_of_insertion = date_of_insertion

    def __str__(self):

        """
        this method is used to print task objects on cmd in details
        :return:
        """

        return (f"nazwa_zadania: {self.task_name} \nopis: {self.describtion} \npriorytet: {self.prio}"
                f"\nkategoria: {self.category} \ntermin_wykonania: {self.deadline} \nczy_aktywne: {self.is_active}")

