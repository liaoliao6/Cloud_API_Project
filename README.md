# OPSWAT_Interview_Project
Generate a simple program to scan a file against our metadefender.opswat.com API.

Opswat coding assessment in python

## Files in the folder:
1. upload_file.py: python code for scanning file using cloud API
2. sampletxt.txt: Sample input file. You can use any file you need.

## How to use this program:

1. Download the OPSWAT_Interview_Project directory and input API key in line 7 of the upload_file.py
For example: API_Key = '543hug897w4hp9gaseara'

2. Put the file you want to scan with the upload_file.py in the same folder.

3. Install python 3 and related package: requests, hashlib.

## How to run program:
python upload_file.py [User_input_file]
for example: python upload_file.py sampletxt.txt

## You will expect the sample output like:

$ python upload_file.py sampletxt.txt

Upload file and scan.
Current scan progress is:  0 %
Current scan progress is:  100 %

OUTPUT:
filename:  sampletxt.txt
overall_status:  Clean

Engine:  AegisLab
scan_result_i :  0
scan_time :  0
threat_found :  Clean
def_time :  2022-08-28T01:05:36.000Z

Engine:  AhnLab
scan_result_i :  0
scan_time :  1
threat_found :  Clean
def_time :  2022-08-23T00:00:00.000Z

Engine:  Antiy
scan_result_i :  0
scan_time :  1
threat_found :  Clean
def_time :  2022-08-22T15:30:00.000Z

Engine:  Avira
scan_result_i :  0
scan_time :  1
threat_found :  Clean
def_time :  2022-08-22T09:55:00.000Z

Engine:  Bitdefender
scan_result_i :  0
scan_time :  1
threat_found :  Clean
def_time :  2022-08-22T08:52:06.000Z

Engine:  ClamAV
scan_result_i :  0
scan_time :  1
threat_found :  Clean
def_time :  2022-08-22T09:19:51.000Z

Engine:  CrowdStrike Falcon ML
scan_result_i :  23
scan_time :  1
threat_found :  Clean
def_time :  2022-08-22T00:00:00.000Z

Engine:  Cyren
scan_result_i :  0
scan_time :  12
threat_found :  Clean
def_time :  2022-08-22T09:49:00.000Z

Engine:  ESET
scan_result_i :  0
scan_time :  0
threat_found :  Clean
def_time :  2022-08-22T08:40:58.000Z

Engine:  Emsisoft
scan_result_i :  0
scan_time :  7
threat_found :  Clean
def_time :  2022-08-22T03:35:00.000Z

Engine:  HAURI
scan_result_i :  0
scan_time :  2
threat_found :  Clean
def_time :  2022-08-21T22:57:36.000Z

Engine:  Huorong
scan_result_i :  0
scan_time :  1
threat_found :  Clean
def_time :  2022-08-22T10:20:37.000Z

Engine:  IKARUS
scan_result_i :  0
scan_time :  0
threat_found :  Clean
def_time :  2022-08-22T08:50:16.000Z

Engine:  Jiangmin
scan_result_i :  0
scan_time :  1599
threat_found :  Clean
def_time :  2022-08-21T05:34:24.000Z

Engine:  K7
scan_result_i :  0
scan_time :  1
threat_found :  Clean
def_time :  2022-08-22T01:20:00.000Z

Engine:  Kaspersky
scan_result_i :  0
scan_time :  2
threat_found :  Clean
def_time :  2022-08-22T09:39:00.000Z

Engine:  McAfee
scan_result_i :  0
scan_time :  1
threat_found :  Clean
def_time :  2022-08-28T00:00:00.000Z

Engine:  NANOAV
scan_result_i :  0
scan_time :  3
threat_found :  Clean
def_time :  2022-08-22T04:26:00.000Z

Engine:  Scrutiny
scan_result_i :  23
scan_time :  49
threat_found :  Clean
def_time :  2022-08-22T15:30:00.000Z

Engine:  Sophos
scan_result_i :  0
scan_time :  13
threat_found :  Clean
def_time :  2022-08-22T00:46:24.000Z

Engine:  TACHYON
scan_result_i :  0
scan_time :  15
threat_found :  Clean
def_time :  2022-08-22T00:00:00.000Z

Engine:  OnAV
scan_result_i :  23
scan_time :  1
threat_found :  Clean
def_time :  2022-08-22T04:26:00.000Z

Engine:  Webroot SMD
scan_result_i :  23
scan_time :  1
threat_found :  Clean
def_time :  2022-08-21T21:00:16.000Z

Engine:  Xvirus Anti-Malware
scan_result_i :  0
scan_time :  46
threat_found :  Clean
def_time :  2022-08-21T19:35:03.000Z

Engine:  Zillya!
scan_result_i :  0
scan_time :  2
threat_found :  Clean
def_time :  2022-08-26T21:09:00.000Z

Engine:  Vir.IT ML
scan_result_i :  0
scan_time :  1
threat_found :  Clean
def_time :  2022-08-26T12:45:00.000Z


