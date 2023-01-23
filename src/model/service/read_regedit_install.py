from winreg import ConnectRegistry,OpenKey,EnumKey,HKEY_LOCAL_MACHINE,QueryValueEx

def read_file():
	aReg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
	aKey = OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")
	mass = list()
	i = 0

	try:
		while True:
			keyname = EnumKey(aKey, i)
			asubkey = OpenKey(aKey, keyname)
			try:
				display_name = (QueryValueEx(asubkey, "DisplayName")[0])
			except:
				display_name = 'Інформація відсутня'
			try:
				DisplayVersion = (QueryValueEx(asubkey, "DisplayVersion")[0])
			except:
				DisplayVersion = 'Інформація відсутня'
			try:
				InstallDate = (QueryValueEx(asubkey, "InstallDate")[0])
			except:
				InstallDate = 'Інформація відсутня'
			try:
				InstallSource = (QueryValueEx(asubkey, "InstallSource")[0])
			except:
				InstallSource = 'Інформація відсутня'
			try:
				Publisher = (QueryValueEx(asubkey, "Publisher")[0])
			except:
				Publisher = 'Інформація відсутня'
			try:
				InstallLocation = (QueryValueEx(asubkey, "InstallLocation")[0])
			except:
				InstallLocation = 'Інформація відсутня'
			i += 1
			mass.append({
				'display_name': display_name,
				'DisplayVersion': DisplayVersion,
				'InstallDate': InstallDate,
				'InstallSource': InstallSource,
				'Publisher': Publisher,
				'InstallLocation': InstallLocation
			})
	except:
		pass

	return mass