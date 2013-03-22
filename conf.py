# -*- coding: utf-8 -*-

"""
Configuration:
ASANA_APIKEY: API key for Asana

HIPCHAT_APIKEY: API key for HipChat

ASANA_HIPCHAT:
Link between Asana project and Hipchat room. Get these IDs by running the 'asana_hipchat_info.py' file.
Format: 'ASANA-ID' : 'HIPCHAT-ID'

!Note that you need to have specified both API keys for this to work!

CHATBOT_NAME: Name of the bot (this is the name displayed to user chat users)

"""

CONFIG = {
    "ASANA_APIKEY": "YOUR-API-KEY-HERE",
    "HIPCHAT_APIKEY" : "YOUR-API-KEY-HERE",
    "ASANA_HIPCHAT" : {
        'YOUR-ASANA-PROJECT-ID-HERE':'YOUR-HIPCHAT-ROOM-ID-HERE'
    },
    "CHATBOT_NAME" : "White Rabbit"
}
