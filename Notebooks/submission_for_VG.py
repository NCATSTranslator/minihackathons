## For Vicki

#To run this type below command line in the terminal where the script is hosted

#python3.9 submission_for_VG.py


import requests
import json
from collections import defaultdict
import os
import pandas as pd

def submit_to_ars(m,ars_url='https://ars.transltr.io/ars/api',arax_url='https://arax.ncats.io'):
    submit_url=f'{ars_url}/submit'
    response = requests.post(submit_url,json=m)
    try:
        message_id = response.json()['pk']
    except:
        print('fail')
        message_id = None
    print(f'{arax_url}/?source=ARS&id={message_id}')
    return message_id



def retrieve_ars_results(mid,ars_url='https://ars.transltr.io/ars/api'):
    pk = 'https://arax.ncats.io/?source=ARS&id=' + mid
    message_url = f'{ars_url}/messages/{mid}?trace=y'
    response = requests.get(message_url)
    j = response.json()
    print( j['status'] )
    results = {}
    dictionary = {}
    for child in j['children']:
        print(child['status'])
        if child['status']  == 'Done':
            childmessage_id = child['message']
            child_url = f'{ars_url}/messages/{childmessage_id}'
            try:
                child_response = requests.get(child_url).json()
                nresults = len(child_response['fields']['data']['message']['results'])
                if nresults > 0:
                    results[child['actor']['agent']] = {'message':child_response['fields']['data']['message']}
            except Exception as e:
                nresults=0
                child['status'] = 'ARS Error'
        elif child['status'] == 'Error':
            nresults=0
            childmessage_id = child['message']
            child_url = f'{ars_url}/messages/{childmessage_id}'
            try:
                child_response = requests.get(child_url).json()
                results[child['actor']['agent']] = {'message':child_response['fields']['data']['message']}
            except Exception as e:
                #print(e)
                child['status'] = 'ARS Error'
        else:
            nresults = 0
            
        dictionary['pk_id'] =  pk  
            
        if ((child['status'] == 'Done') & (nresults == 0)):
            dictionary[child['actor']['agent']] = 'No Results'
            #test =  [child['actor']['agent'], 'No Results']
        elif ((child['status'] == 'ARS Error') & (nresults == 0)):
            dictionary[child['actor']['agent']] = 'ARS Error'
        elif ((child['status'] == 'Error') & (nresults == 0)):
            dictionary[child['actor']['agent']] = 'Error'
            #test =  [child['actor']['agent'], 'ARS Error']
        elif ((child['status'] == 'Done') & (nresults != 0)):
            #test =  [child['actor']['agent'], 'Results']
            dictionary[child['actor']['agent']] = 'Results' 
        
        
        print(child['actor']['agent'], child['status'], nresults)
        #test =  [child['actor']['agent'], child['status'], nresults]
        #test2.append(test)
    return dictionary


def printjson(j):
    print(json.dumps(j,indent=4))



with open('/Users/priyash/Documents/GitHub/minihackathons/2021-12_demo/workflowB/B.2_DILI-fourth-one-hop-from-disease-or-phenotypic-feature_trapi.json') as inf:
    query1 = json.load(inf)


printjson(query1)


kcresult = submit_to_ars(query1)


#result_status = retrieve_ars_results(kcresult)



