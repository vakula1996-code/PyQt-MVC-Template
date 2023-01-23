import sqlite3
import os
import time

def read_activities():
	path = r'C:\Users'
	mass_activities = []
	for root, dirs, files in os.walk(path):
		for file in files:
			if file.endswith("ActivitiesCache.db"):
				path_file = os.path.join(root, file)
				user_name = (path_file.partition("L.")[2])
				user_name1 = (user_name.partition('\A')[0])
				con = sqlite3.connect(path_file)
				coursor = con.cursor()
				coursor.execute("""SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Activity'""")
				if coursor.fetchone()[0] == 1:
					coursor.execute(
						"""SELECT AppID, StartTime, LastModifiedTime, ExpirationTime, LastModifiedOnClient, EndTime FROM Activity""")
				for i in coursor.fetchall():
					application = i[0]
					start_time = i[1]
					last_modif_time = i[2]
					expiration_time = i[3]
					last_modifiedon_client = i[4]
					end_time = i[5]
					mass_activities.append({
											'aplication': application.split(',')[0][17:-1],
											'starttime': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time)),
											'lastmodifia': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(last_modif_time)),
											'ExpirationTime': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(expiration_time)),
											'LastModifiedOnClient': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(last_modifiedon_client)),
											'EndTime': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time)),
											'UserName':user_name1})
				con.commit()
				coursor.close()
	return mass_activities