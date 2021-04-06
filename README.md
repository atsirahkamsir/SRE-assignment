# SRE-assignment
***
This is my submission for the SRE Assignment given to me by Credit Suisse. Author: Nur Atsirah Binte Kamsir. The assignment requires to create a script to scrape event logs and 
Perform a data dump into ELK stack. Language used for script: Python 3. Project Status: Completed.
## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [Challenges Faced](#challenges)

### General Info
***
A python script was developed to scrape event logs to be dumped into ELK. For the purpose of assignment, artificial data is being generated and loaded into ‘logs_Apr_2021.txt’. This can be done by running ‘random_logsgenerator.py’. Logs are in json format with each json object containing 4 fields ie ID/CLIENTID,timestamp,log_level and thread. Generation of this artificial data takes in the assumptions 
1) timestamp format is of form yyyy-mm-ddTHH:MM:SS
2) 2 log levels: ERROR/INFO
3) each log files, contain logs for that particular Month-Year
If json object contains ‘CLIENT ID’ field, it is an error index
Else , it is a data index
For each client ID, an encryption is done to the id before being sent to Elasticsearch. This is done by generating a key. This key is stored in a file in the secretkeys folder. Eg. logs_2021_Apr.txt, refer to 2021_April.key for its corresponding key. Key needs to be kept in a secured folder so that CLIENT ID can be decrypted to its original value in the future.

## Technologies
***
A list of technologies used within the project:
* Python 3
* Elasticsearch
## Installation
***
Refer to requirements.txt folder to install all packages needed to run jsondump.py
```
$ pip install -r requirements.txt 
```
## Challenges Fced
***
It was a challenging yet rewarding assignment for me because all the concepts tested were fairly new to me.Biggest challenge faced was figuring out how to configure Elasticsearch on my localhost and how to have my python script establish a succesful connection to an Elasticsearch instance. I also had to readup on the syntax used in elasticsearch so that I am able to convert json to an acceptable index format in Elastic.
For the 2nd question, it was slightly confusing as to what a trigger is. However after reading  up on Task Scheduler and how it can be used to run python scripts automatically, it gave me a rough idea on how to answer the 2nd part of the question. My intepretation might be wrong but I gave a thorough explanation of my answers.

