
import json
import os

from time import sleep
import os

import datetime
from cryptography.fernet import Fernet
from elasticsearch import Elasticsearch, helpers


current_date = datetime.datetime.now()
SECRETKEY_DIRECTORY = os.getcwd()+ '/secretkeys'
SECRETKEY_FILE = SECRETKEY_DIRECTORY + "/"+ str(current_date.year) +'_' + str(current_date.strftime("%b")) +".key"

if os.path.exists(SECRETKEY_FILE):
  	os.remove(SECRETKEY_FILE)


def get_data_from_logs(self):
	return [l.strip() for l in open(str(self), encoding="utf8", errors='ignore')]

def generate_key():
    
    key = Fernet.generate_key()

    with open(SECRETKEY_FILE, "wb") as key_file:
        key_file.write(key)

def load_key():

    return open(SECRETKEY_FILE, "rb").read()

def encrypt_CLIENTID(id):

    key = load_key()
    encoded_id = id.encode()
    f = Fernet(key)
    encrypted_id = f.encrypt(encoded_id)
    
    return encrypted_id


def read_logs_to_ELK():

	# declare a client instance of the Python Elasticsearch library
	client = Elasticsearch("localhost:9200")

	log_file = 'logs_'+ str(current_date.year) +'_' + str(current_date.strftime("%b")) + '.txt'
	error_doclist =[]
	data_doclist =[]

	docs = get_data_from_logs(log_file)

	generate_key()

	for doc in docs:
		logs_doc = json.loads(doc)
		print(logs_doc)
		for field in logs_doc:
			if field == 'CLIENT ID':
				logs_doc['CLIENT ID'] = str(encrypt_CLIENTID(logs_doc['CLIENT ID']))
				error_doclist.append(logs_doc)
			elif field =='ID':
				data_doclist.append(logs_doc)
		
	try:
		print ("\nAttempting to index the list of  data docs using helpers.bulk()")

		# use the helpers library's Bulk API to index list of Elasticsearch docs
		resp = helpers.bulk(client,data_doclist,index = "data",doc_type = "_doc")

		# print the response returned by Elasticsearch
		print ("helpers.bulk() RESPONSE:", resp)
		print ("helpers.bulk() RESPONSE:", json.dumps(resp, indent=4))



	except Exception as err:

		print("Elasticsearch helpers.bulk() ERROR:", err)

	
	try:
		print ("\nAttempting to index the list of error docs using helpers.bulk()")

		# use the helpers library's Bulk API to index list of Elasticsearch docs
		resp = helpers.bulk(client,error_doclist,index ="error",doc_type = "_doc")

		# print the response returned by Elasticsearch
		print ("helpers.bulk() RESPONSE:", resp)
		print ("helpers.bulk() RESPONSE:", json.dumps(resp, indent=4))




	except Exception as err:

		print("Elasticsearch helpers.bulk() ERROR:", err)

	
		

if __name__ == "__main__":
    read_logs_to_ELK()
	














	
	
	

# assuming 2 type of events: data,error
