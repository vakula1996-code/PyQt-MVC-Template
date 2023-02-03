from pathlib import Path
import os
import datetime
import sys
import LnkParse3

def path_users():
	example_dir  = r"C:\Users"
	lnks = list()
	with os.scandir(example_dir) as files:
		for file in files:
			if file.is_dir() == True:
				path_recent = r"C:\Users\{0}\AppData\Roaming\Microsoft\Windows\Recent".format(str(file.name))
				try:
					pathlist = Path(path_recent)
				except:
					pass
			if len(path_lnk(pathlist)) > 0:
				for i in path_lnk(pathlist,file.name):
					lnks.append(i)
	return lnks

def path_lnk(path,name_user=''):
	my_list = list()
	pathlist = Path(path).glob('*.lnk')
	for i in pathlist:
		with open(i, 'rb') as indata:
			lnk = LnkParse3.lnk_file(indata)
		try:
			local_path = (lnk.get_json()['link_info']['local_base_path'])
		except:
			local_path = "NONE"
		size = (str(os.path.getsize(i)) + " " + 'Kb')
		try:
			date_create = datetime.datetime.fromtimestamp(int(os.path.getctime(i)))
		except:
			date_create = "Warning"

		if local_path != 'NONE':
			my_list.append({
				'user': name_user,
				'date_create': date_create,
				'info': "Otkritye faila abo papku",
				'local_path': local_path.encode('ISO-8859-1', 'ignore').decode('cp1251'),
				'size': size
			})
	return my_list

# print(path_users())

