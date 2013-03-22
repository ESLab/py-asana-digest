# -*- coding: utf-8 -*-

from client_asana import Client as AsanaClient
from client_hipchat import Client as HipchatClient
from task_list import TaskList
from template import Template
import datetime
import time
import dateutil.parser


class Task():
    def __init__(self, conf):
        self.asana_hipchat = conf['ASANA_HIPCHAT']
        self.asana = AsanaClient(conf['ASANA_APIKEY'])
        self.hipchat = HipchatClient(conf['HIPCHAT_APIKEY'])
        self.chatbot_name = conf['CHATBOT_NAME']

    def time_in_GMT0(self):
        t = time.time()
        if time.localtime(t).tm_isdst and time.daylight:
            offset = time.altzone
        else:
            offset = time.timezone

        dt = datetime.datetime.fromtimestamp(t+offset)
        return time.mktime(dt.timetuple())

    def date_includes(self, date):
        date = dateutil.parser.parse(date)
        date = time.mktime(date.timetuple())

        if (self.time_in_GMT0() - date) < 86400:
            return True
        else:
            return False

    def render_tasks(self, project, user, render_type, task_list):
        yesterday = datetime.date.today()-datetime.timedelta(days=1)
        message = Template().render(
            project, task_list, user, render_type, yesterday)

        self.hipchat.post(self.asana_hipchat[project], self.chatbot_name, message)

    def run(self):

        projects = {}

        for project in self.asana_hipchat:
            projects[project] = {}
            completed_tasks = TaskList(project)
            upcomming_tasks = TaskList(project)

            tasks = self.asana.get("/projects/"+project+"/tasks?opt_fields=assignee,completed_at,name")
            if tasks.get('error', False):
                print "There was an error in your request"
                break

            tasks = tasks.get('data', False)
            for task in tasks:
                if task['completed_at'] and self.date_includes(task['completed_at']):
                    completed_tasks.add(task['assignee']['id'], task)
                else:
                    upcomming_tasks.add(task['assignee']['id'], task)

            projects[project]['completed_tasks'] = completed_tasks
            projects[project]['upcomming_tasks'] = upcomming_tasks

        users = self.asana.get("/users")
        if users.get('data', False):
            for user in users['data']:
                for project in projects:
                    if projects[project]['completed_tasks'].tasks_for(user['id']):
                        self.render_tasks(project, user['name'],  'completed_tasks', projects[
                                          project]['completed_tasks'].tasks_for(user['id']))
                    if projects[project]['upcomming_tasks'].tasks_for(user['id']):
                        self.render_tasks(project, user['name'], 'upcomming_tasks', projects[
                                          project]['upcomming_tasks'].tasks_for(user['id']))
