def retrieve_ars_results(mid,ars_url='https://ars.transltr.io/ars/api'):
    pk = 'https://arax.ncats.io/?source=ARS&id=' + mid
    message_url = f'{ars_url}/messages/{mid}?trace=y'
    response = requests.get(message_url)
    j = response.json()
    print( j['status'] )
    results = {}
    dictionary = {}
    dictionary_2 = {}
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
            dictionary[child['actor']['agent']] = 'Results' ': ' + str(error_code)
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