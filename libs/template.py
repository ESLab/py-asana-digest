# -*- coding: utf-8 -*-


class Template():
    def __init__(self):
        self.html = ""

    def render(self, project, tasks, user, render_type, date):

        if render_type == "completed_tasks":
            self.html += 'Between '+date.strftime('%d.%m')+'-'+str(date.day+1)+'.'+str(date.month)+'.'+str(date.year)+', <b>'+user+'</b> has completed the following tasks:'
            self.render_complete(project, tasks)

        if render_type == "upcomming_tasks":
            self.html += '<b>'+user +'</b> is currently working on the following tasks:'
            self.render_upcomming(project, tasks)

        if render_type == "unassigned_tasks":
            self.html += 'The following tasks are <b>not</b> assigned to anyone, grab one:'
            self.render_unassigned(project, tasks)

        return self.html

    def render_complete(self, project, tasks):
        for task in tasks:
            self.html += '<br/>&#x2713; '+task["name"]+' ' \
                        '(<a href="https://app.asana.com/0/'+project+'/'+str(task['id'])+'">#'+str(task['id'])+'</a>)'

    def render_upcomming(self, project, tasks):
        for task in tasks:
            self.html += '<br/>&#x25a2; '+task["name"]+' ' \
                        '(<a href="https://app.asana.com/0/'+project+'/'+str(task['id'])+'">#'+str(task['id'])+'</a>)'

    def render_unassigned(self, project, tasks):
        for task in tasks:
            self.html += '<br/>&#215; '+task["name"]+'(<a href="https://app.asana.com/0/'+project+'/'+str(task['id'])+'">#'+str(task['id'])+'</a>)'

