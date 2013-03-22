# -*- coding: utf-8 -*-


class TaskList():
    def __init__(self, project):
        self.project = project
        self.tasks = {}

    def add(self, user, task):
        if not user in self.tasks:
            self.tasks[user] = []
        self.tasks[user].append(task)

    def tasks_for(self, user):
        return self.tasks.get(user, False)

    def users_of_tasks(self):
        return self.tasks
