import re
from collections import Counter

from task import Task


class FileHandler:

    """
    that class contains method to work with file
    """

    def __init__(self, filepath):
        self.filepath = filepath

    def substring(input):

        """
        this method is responsible for substring values from brackets: <> which are common in task file
        :return: values from brackets array
        """

        matches = re.findall(r'<(.*?)>', input)
        return matches

    def load_from_file(self):

        """
        this method is responsible for load values from file, create task objects and append them to the task list in Task_manager object
        :return: list of tasks
        """

        tasks = []
        with open(self.filepath, 'r') as file:
            for line in file:
                task_name = FileHandler.substring(line)[0]
                describtion = FileHandler.substring(line)[1]
                prio = FileHandler.substring(line)[2]
                category = FileHandler.substring(line)[3]
                deadline = FileHandler.substring(line)[4]
                is_active = FileHandler.substring(line)[5]
                date_of_insertion = FileHandler.substring(line)[6]
                tasks.append(Task(task_name, describtion, prio, deadline, category, is_active, date_of_insertion))
        file.close()
        return tasks

    def save_to_file(self, task):

        """
        this method is responsible for saving task to the file
        :param task: task object to be saved
        :return: void
        """

        with open(self.filepath, 'a') as file:
            file.write(
                f"task_name<{task.task_name}>describtion<{task.describtion}>prio<{task.prio}>deadline<{task.deadline}>category<{task.category}>is_active<{task.is_active}>date_of_insertion<{task.date_of_insertion}>\n")
        file.close()

    def clear_file(self):
        """
        this method is responsible for cleaning task file
        :return: void
        """

        with open(self.filepath, 'w') as file:
            file.truncate(0)

    def save_statistic(self, stat: str, value: int):
        """
        this method is responsible for saving statistics to the statistic file
        :param stat: statistic name
        :param value: value of the statistic
        :return: void
        """

        with open('statistic.txt', 'r') as file:
            lines = file.readlines()

        for i in range(len(lines)):
            if stat in lines[i]:
                lines[i] = lines[i].strip() + str(value) + ';' + '\n'
                break

        with open('statistic.txt', 'w') as file:
            file.writelines(lines)


