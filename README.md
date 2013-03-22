# Asana Digest

Python port of Tatsuhiko Miyagawas [asana_digest](https://github.com/miyagawa/asana_digest/) with added features. 

py-asana-digest is a command line application to fetch Asana tasks of the previous work day and send them to the appropriate chat room.


## Configuration

The following configurations has to be made in conf.py for the script to work:

- `ASANA_APIKEY`: API-Key for Asana
- `HIPCHAT_APIKEY`: API-Key for HipChat
- `ASANA_HIPCHAT`: Python dictionary including the Asana projects as keys and HipChat rooms as values 

If you are having a hard time finding the IDs for Asana projects and HipChat rooms run:

```
python asana_hipchat_info.py
```

## Usage
```
python asana_digest.py
```

## Requirements

Python 2.7

## Author

Frank Wickström
Embedded Systems Laboratory at Åbo Akademi University

### License
GPLv3 (more info in the LICENCE file)


[![githalytics.com alpha](https://cruel-carlota.pagodabox.com/ea02113340d21dfa3f0c06292e75d32f "githalytics.com")](http://githalytics.com/ESLab/py-asana-digest)
