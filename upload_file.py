import requests
import time
import hashlib
import argparse 

Opswat_Server = 'https://api.metadefender.com/v4/'
API_Key = ''     # Please input your API Key here

def get_file_hash(customer_file):
    """
    Generate hash# of user input file.

    @param customer_file: Customer input file
    @return: Tuple of file hash #
    """
    
    BUF_SIZE = 65536  # Read stuff in 64kb chunks!
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()

    with open(customer_file, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)
            sha1.update(data)
            sha256.update(data)
    
    md5_hash = md5.hexdigest()
    sha1_hash = sha1.hexdigest()
    sha256_hash = sha256.hexdigest()
    return (md5_hash, sha1_hash, sha256_hash)

def get_scan_results_from_hash(file_hash):
    """
    Retrieve scan reports using data hash.

    @param customer_hash: SHA1 or MD5 or SHA256	[REQUIRED]
    @return: scan results (JSON)
    """
    headers = dict(apikey = API_Key)
    
    for customer_hash in file_hash:
        url = Opswat_Server + 'hash/' + customer_hash
        response = requests.get(url=url, headers=headers)
    return response

def get_scan_results_from_data_id(data_id):
    """
    Retrieve scan results based on data_id

    @param data_id: Get from (Scanning a file)	[REQUIRED]
    @return: scan results (JSON)
    """
    url = Opswat_Server + 'file/' + data_id
    headers = dict(apikey = API_Key)
    return requests.get(url=url, headers=headers)

def scan_file(customer_file):
    """
    Initiate scan request

    On Metascan Online, scan is done asynchronously and each scan request is tracked by data id.

    @param customer_file: User input file	[REQUIRED]
    @return: data_id	Data ID used for retrieving scan results.
                        Since there are potentially multiple scans for same files when any engine has different
                        definition time or when there is an additional engine, this is identifier for per scan
                        other than per file. (JSON)
    """
    url = Opswat_Server  + 'file'
    headers = dict(apikey= API_Key)
    files = {"form_field_name": customer_file}
    return requests.post(url=url, files=files, headers=headers)

def scan_file_and_get_results(customer_file):
    """
    Retrieve scan results

    On Metascan Online, scan is done asynchronously and each scan request is tracked by data id.
    Initiating a file scan and retrieving the scan results needs to be done with two separate API calls.
    This request needs to be made multiple times until scan is complete.
    Scan progress can be traced using scan_results.progress_percentage value from the response.

    @param customer_file: User input file	[REQUIRED]
    @return: scan results (JSON)
    """
    
    response = scan_file(customer_file)
    data_id = response.json()['data_id']
    while True:
        response = get_scan_results_from_data_id(data_id=data_id)
        print('Current scan progress is: ', response.json()['scan_results']['progress_percentage'], '%') # Print scan progress. Wait 3s when the progress is less than 100%
        if response.status_code != requests.codes.ok:
            return response
        if response.json()['scan_results']['progress_percentage'] == 100:
            break
        else:
            time.sleep(3)     # Giving the engines enough time to scan and return results.

    return response

def outputData(response, customer_file):
    
    """
    Print out scan results

    Need to print filename, overall results and each engine scan results.

    @param customer_file: User input file	[REQUIRED]
    @param response: Scan results	[REQUIRED]
    @return: None
    """    
    print()                                                         # Blank line, format.
    print("OUTPUT:")
    found_occurence = False                                         # Makes sure there are results to be printed. 
    while not found_occurence:                                      
        scan_details = response.json()["scan_results"]["scan_details"] # Each engine scan results
        print('filename: ', customer_file)                             # File name
        if response.json()["scan_results"]["total_detected_avs"] == 0:
            status_code = 'Clean'
        else:
            status_code = 'Found ' + str(response.json()["scan_results"]["total_detected_avs"]) + ' Virus'      
        print('overall_status: ', status_code)                      # Over all status
        print("----------------------------") 
        found_occurence = True
        for i in scan_details:                                      # Grabs the headers of the results of the individual engines.
            print("Engine: ", i)                                    # Uses engine name as key to iterate through scan details.
            for k, v in scan_details[i].items():                    
                if k == "threat_found" and v == "":                 # Prints key-value pairs, or "Clean" if threat_found string is empty
                    v = "Clean"                                       
                print(k, ": ",v)
                if k == "def_time":
                    print("----------------------------")           # Horizontal bar at end of each engine results for visibility


def check_files(customer_file):
    
    """
    Main function, read file, check hash and upload file for checking if no file exsited in the cloud.

    @param customer_file: User input file	[REQUIRED]
    @return: None
    """   
    
    response = get_scan_results_from_hash(customer_file)            # Check file hash # and see if it exsits in the cloud
    
    while response.status_code != 200:                              # If no results from get_scan_results_from_hash(customer_file), upload and scanning the file, until it is available. 
        print("Upload file and scan.")                                                                   
        response = scan_file_and_get_results(customer_file)

    outputData(response, customer_file)                             # Output scan results

if __name__ == '__main__':
    # Instantiate the parser
    parser = argparse.ArgumentParser(description='OPSWAT API')
    # Required positional argument
    parser.add_argument('file_arg', help='A required path to the file needed to be scanned')   
    # Parse
    args = parser.parse_args()    
    # Access
    filename = args.file_arg

    check_files(filename)

        
        
    
    