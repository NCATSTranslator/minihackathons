#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 16:47:51 2021

@author: priyash
"""

import requests
import json


def submit_to_ars(m,ars_url='https://ars.transltr.io/ars/api',arax_url='https://arax.ncats.io/legacy'):
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
    message_url = f'{ars_url}/messages/{mid}?trace=y'
    response = requests.get(message_url)
    j = response.json()
    #print( j['status'] )
    results = {}
    dictionary = {}
    for child in j['children']:
        #print(child['status'])
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


def submit_to_devars(m):
    return submit_to_ars(m,ars_url='https://ars-dev.transltr.io/ars/api',arax_url='https://arax.ncats.io')

def retrieve_devars_results(m):
     return retrieve_ars_results(m,ars_url='https://ars-dev.transltr.io/ars/api')

def printjson(j):
    print(json.dumps(j,indent=4))
    
    
if __name__ == "__main__": 
    submit_to_ars()
    retrieve_ars_results() 
    submit_to_devars()
    retrieve_devars_results()
    printjson()
    
    




