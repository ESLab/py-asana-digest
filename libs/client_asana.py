# -*- coding: utf-8 -*-

import urllib2
import base64
import json


class Client():
    def __init__(self, apikey):
        self.apikey = apikey
        self.setup()

    def setup(self):
        self.auth = base64.encodestring('%s:' % (self.apikey))
        self.headers = {"Authorization": "Basic %s" % self.auth}

    def get(self, path):
        uri = "https://app.asana.com/api/1.0"+path
        request = urllib2.Request(uri, None, self.headers)
        result = urllib2.urlopen(request)
        return json.load(result)
