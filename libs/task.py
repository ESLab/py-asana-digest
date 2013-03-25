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

    def time_in_UTC0(self, unix=True):

        class UTC(datetime.tzinfo):

            def utcoffset(self, dt):
                return datetime.timedelta(0)

            def tzname(self, dt):
                return "UTC"

            def dst(self, dt):
                return datetime.timedelta(0)

        t = time.time()
        if time.localtime(t).tm_isdst and time.daylight:
            offset = time.altzone
        else:
            offset = time.timezone

        dt = datetime.datetime.fromtimestamp(t+offset)
        dt = dt.replace(tzinfo=UTC())

        if unix:
            return time.mktime(dt.timetuple())
        else:
            return dt

    def date_includes(self, date):
        date = dateutil.parser.parse(date)
        now = self.time_in_UTC0(False)
        yesterday = now-datetime.timedelta(days=1)

        if date.day == now.day or date.day == yesterday.day:
            return True
        else:
            return False

    def render_tasks(self, project, user, render_type, task_list, color='yellow'):
        yesterday = datetime.date.today()-datetime.timedelta(days=1)
        message = Template().render(
            project, task_list, user, render_type, yesterday)

        self.hipchat.post(self.asana_hipchat[project], self.chatbot_name, message, color=color)

    def run(self):

        projects = {}

        for project in self.asana_hipchat:
            projects[project] = {}
            completed_tasks = TaskList(project)
            upcomming_tasks = TaskList(project)
            unassigned_tasks = TaskList(project)

            tasks = self.asana.get("/projects/"+project+"/tasks?opt_fields=assignee,completed_at,name")
            if tasks.get('error', False):
                print "There was an error in your request"
                break

            tasks = tasks.get('data', False)

            for task in tasks:
                if task['completed_at'] and self.date_includes(task['completed_at']):
                    completed_tasks.add(task['assignee']['id'], task)
                elif task['assignee'] and not task['completed_at']:
                    upcomming_tasks.add(task['assignee']['id'], task)
                elif not task['assignee'] and not task['completed_at']:
                    unassigned_tasks.add(None, task)

            projects[project]['completed_tasks'] = completed_tasks
            projects[project]['upcomming_tasks'] = upcomming_tasks
            projects[project]['unassigned_tasks'] = unassigned_tasks

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

        for project in projects:
            if projects[project]['unassigned_tasks'].num_tasks() > 0:
                self.render_tasks(project, None, 'unassigned_tasks', projects[
                    project]['unassigned_tasks'].tasks_for('unassigned'), color='red')
