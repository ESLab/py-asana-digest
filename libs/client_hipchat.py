# -*- coding: utf-8 -*-

import urllib
import urllib2
import json


class Client():
    def __init__(self, apikey):
        self.apikey = apikey
        self.setup()

    def setup(self):
        self.uri = ''
        self.parameters = {}
        self.parameters['auth_token'] = self.apikey
        self.parameters['format'] = 'json'

    def open_uri(self, path, method='GET'):
        uri = "https://api.hipchat.com/v1"
        parameters = urllib.urlencode(self.parameters)

        if method == 'GET':
            request = urllib2.Request(uri+path+"?"+parameters)
        else:
            request = urllib2.Request(uri+path, parameters)

        result = urllib2.urlopen(request)
        self.setup()

        return json.load(result)

    def get(self, path):
        return self.open_uri(path)

    def post(self, room='', message_from='', message='', format='html', color='yellow', notify=False):
        self.parameters['room_id'] = room
        self.parameters['from'] = message_from[:15]

        if len(message) < 10000:
            self.parameters['message'] = message.encode('utf-8')
        else:
            self.parameters['message'] = message[:10000].encode('utf-8')

        self.parameters['message_format'] = format
        self.parameters[
            'color'] = color  # "yellow", "red", "green", "purple", "gray"

        if notify:
            self.parameters['notify'] = 1
        else:
            self.parameters['notify'] = 0

        return self.open_uri('/rooms/message', 'POST')
