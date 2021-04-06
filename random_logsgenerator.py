import json
import datetime
import os

current_date = datetime.datetime.now()

log_file = 'logs_'+ str(current_date.year) +'_' + str(current_date.strftime("%b")) + '.txt'

def get_data_from_logs(self):
	return [l.strip() for l in open(str(self), encoding="utf8", errors='ignore')]

if os.path.exists(log_file):
	os.remove(log_file)

logs = {}
logs2 ={}

for i in range(1,201):

	if i% 2 != 0:
		logs = {}
		logs['ID'] = str(i)
		logs['timestamp'] = current_date.strftime('%Y-%m-%dT%H:%M:%S%z')
		logs['log_level'] = 'INFO'
		logs['thread'] = 'thread' + str(i)
		
		with open(log_file, 'a') as outfile:
    			json.dump(logs, outfile)
    			outfile.write("\n")

	else:
		logs2 ={}
		logs2['CLIENT ID'] = 'CLIENTID' + str(i)
		logs2['timestamp'] = current_date.strftime('%Y-%m-%dT%H:%M:%S%z')
		logs2['log_level'] = 'ERROR'
		logs2['thread'] = 'thread' + str(i)
		with open(log_file, 'a') as outfile:
    			json.dump(logs2, outfile)
    			outfile.write("\n")







