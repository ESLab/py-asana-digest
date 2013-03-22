# -*- coding: utf-8 -*-

from libs.client_asana import Client as AsanaClient
from libs.client_hipchat import Client as HipchatClient
from conf import CONFIG

asana = AsanaClient(CONFIG['ASANA_APIKEY'])
hipchat = HipchatClient(CONFIG['HIPCHAT_APIKEY'])

projects = asana.get('/projects')

print "ASANA PROJECTS:"
for project in projects['data']:
    print project['id'], " : ", project['name']

print "\nHIPCHAT ROOMS"
rooms = hipchat.get('/rooms/list')
for room in rooms['rooms']:
    print room['room_id'], " : ", room['name'][:20], "("+room['topic'][:20]+") Archived: ", room['is_archived']
