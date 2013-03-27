# -*- coding: utf-8 -*-


class TaskList():
    def __init__(self, project):
        self.project = project
        self.tasks = {'unassigned':[]}

    def add(self, user=None, task=None):
        if user:
            if not user in self.tasks:
                self.tasks[user] = []
            self.tasks[user].append(task)
        else:
            self.tasks['unassigned'].append(task)

    def tasks_for(self, user):
        return self.tasks.get(user, False)

    def users_of_tasks(self):
        return self.tasks

    def num_tasks(self, user):
        if self.tasks.get(user,False):
            return len(self.tasks[user])
        else:
            return 0
