from pathlib import Path
import json
from evtx import PyEvtxParser

def read_event_instal_and_delete():
	my_list = list()
	directory = 'C:\Windows\System32\winevt\Logs'
	pathlist = Path(directory).glob('*.evtx')
	for path in pathlist:
		if str(str(path).partition('Logs')[2]).find('Application') != -1:
			# print(path)
			for record in PyEvtxParser(str(path)).records_json():
				json1 = json.loads(record['data'])
				# print(json1)
				if type(json1['Event']['System']['EventID']) == dict:
					if json1['Event']['System']['EventID']['#text'] == 1033 or json1['Event']['System']['EventID']['#text'] == 1034 or json1['Event']['System']['EventID']['#text'] == 11707 or json1['Event']['System']['EventID']['#text'] == 11724:
						try:
							task = json1['Event']['System']['EventID']['#text']
						except:
							task = 'Не знайдено'
						# print(task)
						try:
							programs_name = json1['Event']['EventData']['Data']['#text'][0]
						except:
							programs_name = 'Не знайдено'
						# print(programs_name)
						try:
							programs_version = json1['Event']['EventData']['Data']['#text'][1]
						except:
							programs_version = 'Не знайдено'
						# print(programs_version)
						try:
							programs_product = json1['Event']['EventData']['Data']['#text'][4]
						except:
							programs_product = 'Не знайдено'
						# print(programs_product)
						try:
							programs_time = json1['Event']['System']['TimeCreated']['#attributes']['SystemTime']
							programs_time = programs_time[0:10] + ' ' + programs_time[11:19]
						except:
							programs_time = 'Не знайдено'
						# print(programs_time)
						try:
							computer = json1['Event']['System']['Computer']
						except:
							computer = 'Не знайдено'
						# print(computer)
						if json1['Event']['System']['EventID']['#text'] == 1033:
							info = "Install programms"
							# print(info)
						if json1['Event']['System']['EventID']['#text'] == 1034:
							info = "Delete programs"
							# print(info)
						if json1['Event']['System']['EventID']['#text'] == 11707:
							info = "Install secsessful"
							# print(info)
						if json1['Event']['System']['EventID']['#text'] == 11724:
							info = "Delete secsessful"
							# print(info)
	# 			try:
	# 				date = json1['Event']['System']['TimeCreated']['#attributes']['SystemTime']
	# 				date = date[0:10] + ' ' + date[11:19]
	# 			except:
	# 				date = 'Не знайдено'
						my_list.append({
							'task': task,
							'programs_name': programs_name,
							'programs_version': programs_version,
							'programs_product': programs_product,
							'programs_time': programs_time,
							'computer': computer,
							'info': info
						})
	return my_list
	# print(my_list)
# read_event_instal_and_delete()