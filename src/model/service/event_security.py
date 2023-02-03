import json
from evtx import PyEvtxParser
from pathlib import Path
import time

def event_read():
    my_list = list()
    directory = 'C:\Windows\System32\winevt\Logs'
    pathlist = Path(directory).glob('*.evtx')
    for path in pathlist:
        if str(path).find('Security') != -1:
            for record in PyEvtxParser(str(path)).records_json():
                json1 = json.loads(record['data'])
                try:
                    task = json1['Event']['System']['Task']
                except:
                    task = 'Не знайдено'
                try:
                    event = json1['Event']['System']['EventID']
                except:
                    event = 'Не знайдено'
                try:
                    date = json1['Event']['System']['TimeCreated']['#attributes']['SystemTime']
                    date = date[0:10]+' '+date[11:19]
                except:
                    date = 'Не знайдено'
                try:
                    if type(json1['Event']['System']['Security']) == dict:
                        security = 'Не знайдено'
                    else:
                        security = json1['Event']['System']['Security']
                except:
                    security = 'Не знайдено'
                try:
                    KeyName = json1['Event']['EventData']['SubjectUserName']
                except:
                    KeyName = 'Не знайдено'
                try:
                    DomainName = json1['Event']['EventData']['SubjectDomainName']
                except:
                    DomainName = 'Не знайдено'
                try:
                    PreviousTime = (json1['Event']['EventData']['PreviousTime'])[:10] +' '+ (json1['Event']['EventData']['PreviousTime'])[11:19]
                except:
                    PreviousTime = 'Не знайдено'
                try:
                    NewTime = (json1['Event']['EventData']['NewTime'])[:10] +' '+ (json1['Event']['EventData']['NewTime'])[11:19]
                except:
                    NewTime = 'Не знайдено'

                my_list.append({
                        'task': task,
                        'event': event,
                        'date': date,
                        'security': security,
                        'KeyName': KeyName,
                        'DomainName': DomainName,
                        'PreviousTime': PreviousTime,
                        'NewTime': NewTime
                        })
            # print(my_list['NewTime'])
# event_read()
    return my_list
