import time
import json
import requests
import domain

#moneyscammatters_db = [ "https://usapus.top",
#                    "https://lihi3.cc/wvfsR",
#                    "https://www.google.com/",
#                    "https://updsps.com/"
#                        ]

api_key = '1ae5d624c2cfddb1480b3cfbff440f2c2396221481d523cec18272ee0c694bfd'

total_virus_url = 'https://www.virustotal.com/vtapi/v2/url/report'



def call_the_VT(website):
    params = {'apikey': api_key, 'resource': website}
    response = requests.get(total_virus_url, params=params)

    if response.status_code == 200:
        json_response = json.loads(response.content)
        if 'positives' in json_response:
            if json_response['positives'] <= 0:
                with open('moneyscammatters_db', 'a') as potential_scams:
                    potential_scams.write(website + " [NON-SCAM!]\n")
                    print(website + " " + "[NON-SCAM!]\n")
            elif json_response['positives'] > 0:
                with open('moneyscammatters_db', 'a') as potential_scams:
                    potential_scams.write(website + " [SCAM!]\n")
                    print(website + " " + "[SCAM!]\n")
        else:
            print('WEBSITE NOT FOUND! Moving on to layer 3...')
            domain.compareDomain(r'/Users/diembui/hacktx/HackTX2023/app/badDomain.json', r'/Users/diembui/hacktx/HackTX2023/app/goodDomain.json')


        time.sleep(15)