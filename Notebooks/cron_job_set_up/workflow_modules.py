#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 09:45:19 2021

@author: priyash


Read and Save Query Status in CSV for all Workflows.
Read all the JSON files for all the workflows and print out the messages and query status to a CSV file


"""
# import all the modules. NB: submit_run_ars_modules contains all the modules to submit job to ARAX


## Pending setup up the cron job for sync and async...also clean the codes 

from datetime import datetime
import json
import requests
#from submit_run_ars_modules import submit_to_ars, submit_to_devars, printjson, retrieve_devars_results 
import os
from collections import defaultdict
import pandas as pd
from time import sleep
from os import path

import gspread
from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials
from gspread_dataframe import set_with_dataframe
from gspread_formatting import *


'''
Main funtions to submit queries to ARS. Note this can be converted at 

'''

def flatten_list(_2d_list):
    flat_list = []
    # Iterate through the outer list
    for element in _2d_list:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list

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

##https://ars.ci.transltr.io/ars/api

def retrieve_ars_results(mid, name, check_sheet, ars_url='https://ars.transltr.io/ars/api'):
    pk = 'https://arax.ncats.io/?source=ARS&id=' + mid
    message_url = f'{ars_url}/messages/{mid}?trace=y'
    response = requests.get(message_url)
    j = response.json()
    print( j['status'] )
    results = {}
    dictionary = {}
    dictionary_2 = {}
    dict3 = {}
    for child in j['children']:
        print(child['status'])
        error_code = child['code']
        
        if child['status']  == 'Done':
            childmessage_id = child['message']
            child_url = f'{ars_url}/messages/{childmessage_id}'
            try:
                child_response = requests.get(child_url).json()
                nresults = len(child_response['fields']['data']['message']['results'])
                if nresults > 0:
                    results[child['actor']['agent']] = {'message':child_response['fields']['data']['message']}
                    
                    if name in list(check_sheet.Workflow):
                        print(name)
                        dfy = check_sheet[check_sheet['Workflow']== name]

                        dfy.reset_index(drop=True)

                        for index,curie_id in enumerate(dfy.Curie):
                            print(index,curie_id)
                            node_num = dfy.iloc[index][3]
                            query_id = curie_id
                            if np.isnan(dfy.iloc[index][2]) == True:
                                len_check = len(child_response['fields']['data']['message']['results'])
                            else:
                                len_check = dfy.iloc[index][2]

                            #print(node_num, query_id, len_check)

                            locs = []
                            for x, val in enumerate(child_response['fields']['data']['message']['results']):
                                #print(val)

                                if x < len_check:

                                    if query_id in val['node_bindings'][node_num][0]['id']:
                                        locs.append(x)
                            if not locs:
                                check_result = f'False'
                                print(check_result)
                                #pass
                            else:
                                check_result = f'True'
                                print('curie id:', query_id, ': INCLUDED at postion N ==', locs, 'on', node_num)

                            dict3[curie_id] = check_result    

                if child_response['fields']['data']['message']['knowledge_graph']['edges']:
                    if child_response['fields']['data']['message']['knowledge_graph']['edges'].keys():
                            edge_ex = child_response['fields']['data']['message']['knowledge_graph']['edges']
                            test_att_values =[]
                            for val in child_response['fields']['data']['message']['knowledge_graph']['edges'].keys():
                                #print(val)
                                
                                for tx in edge_ex[val]['attributes']:
                                    if (tx['attribute_type_id'] == 'biolink:primary_knowledge_source') or (tx['attribute_type_id'] == 'biolink:original_knowledge_source') or (tx['attribute_type_id'] == 'biolink:aggregator_knowledge_source') :
                                        
                                        
                                        value_att = tx['value']
                        
                                        test_att_values.append(value_att)
                                        test_att = set(flatten_list(test_att_values))
                                        
                                        
                                        dictionary_2[child['actor']['agent']] = test_att
                    #else:
                        #dictionary_2[child['actor']['agent']] = [] 
                #else:
                   # dictionary_2[child['actor']['agent']] = []
            
            except Exception as e:
                nresults=0
                child['status'] = 'ARS Error'
                #dictionary_2[child['actor']['agent']] = []
                
            
        
        elif child['status'] == 'Error':
            nresults=0
            childmessage_id = child['message']
            child_url = f'{ars_url}/messages/{childmessage_id}'
            try:
                child_response = requests.get(child_url).json()
                results[child['actor']['agent']] = {'message':child_response['fields']['data']['message']}
                #dictionary_2[child['actor']['agent']] = []
            except Exception as e:
                #print(e)
                child['status'] = 'ARS Error'
                #dictionary_2[child['actor']['agent']] = []
        
        
        else:
            nresults = 0
            #dictionary_2[child['actor']['agent']] = []
            
        dictionary['pk_id'] =  pk  
            
        if ((child['status'] == 'Done') & (nresults == 0)):
            dictionary[child['actor']['agent']] = 'No Results' ': ' + str(error_code)
            #test =  [child['actor']['agent'], 'No Results']
        elif ((child['status'] == 'ARS Error') & (nresults == 0)):
            dictionary[child['actor']['agent']] = 'ARS Error' ': ' + str(error_code)
        elif ((child['status'] == 'Error') & (nresults == 0)):
            dictionary[child['actor']['agent']] = 'Error' ': ' + str(error_code)
            #test =  [child['actor']['agent'], 'ARS Error']
        elif ((child['status'] == 'Done') & (nresults != 0)):
            #test =  [child['actor']['agent'], 'Results']
            dictionary[child['actor']['agent']] = 'Results' ': ' + str(error_code) + ' ' + str(dict3)
        elif ((child['status'] == 'Unknown') & (nresults == 0)):
            #test =  [child['actor']['agent'], 'Results']
            dictionary[child['actor']['agent']] = 'Unknown' ': ' + str(error_code)
        
        
        print(child['actor']['agent'], child['status'], nresults)
        #test =  [child['actor']['agent'], child['status'], nresults]
        #test2.append(test)
    return [dictionary, dictionary_2]


#def submit_to_devars(m):
#    return submit_to_ars(m,ars_url='https://ars-dev.transltr.io/ars/api',arax_url='https://arax.ncats.io')

#def retrieve_devars_results(m):
#     return retrieve_ars_results(m,ars_url='https://ars-dev.transltr.io/ars/api')

def printjson(j):
    print(json.dumps(j,indent=4))
    
def make_hyperlink(value):
    return '=HYPERLINK("%s", "%s")' % (value.format(value), value)



