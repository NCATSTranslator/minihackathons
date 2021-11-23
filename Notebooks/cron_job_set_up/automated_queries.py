#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 18:56:45 2021

@author: priyash
"""
'''
Here the codes start calling the above functions and submits the queries to ARS

The below code reads each JSON files from the Workflows A through D (subdirectories). 
The queries are submitted to ARAX and output is saved in a dictionary, where the key is the file name of 
the JSON to denote which query is being run and the values assigned to the key is the query id

'''


PATH = r'/Users/priyash/Documents/GitHub/minihackathons/2021-12_demo'
EXT = "*.json"
dict_workflows = {}
for root, dirs, files in os.walk(PATH): # step 1: accessing file
    #print(root)
    for name in files:
        
        if name.endswith((".json")):
            file_read = path.join(root, name)
            dir_name = (os.path.splitext(os.path.basename(root))[0])
            print(file_read)
            
            filename = (os.path.splitext(os.path.basename(file_read))[0])
            print(filename)
            with open(file_read,'r') as inf:
                query = json.load(inf)
                
                kcresult = submit_to_ars(query)
                
                sleep(600)
                
                result_status = retrieve_ars_results(kcresult)
                
        
                dict_workflows[filename] = kcresult

                sleep(100)
                            
                
                
## Grap all the message status     
        
                
workflow_result_messages = {}
for keys, val in dict_workflows.items():
    print(keys, val)
    
    result_status = retrieve_ars_results(val)
    
    workflow_result_messages[keys] = result_status
    
     

## Convert mesages to a dataframe
col = []
final_dict = defaultdict(list)
for k in sorted(workflow_result_messages):
    print(k)
    col.append(k)
    
    for key, value in workflow_result_messages[k].items():
#         if key.startswith('kp-'):
#             key_mod = key.replace('kp-','')
#         else:
#             key_mod = key
        
        final_dict[key].append(value)

    final_dict = dict(final_dict)
    
df = pd.DataFrame(final_dict).T
df.rename(columns=dict(zip(df.columns, col)), inplace=True)


# Converting the Pk's to hyperlink

df.replace('ARS Error', 'No Results', regex=True,inplace=True)

df.loc['pk'] = df.loc['pk'].apply(lambda x: make_hyperlink(x))




### Creating second table with edge attribute source


final_dict2 = defaultdict(dict)
for k in sorted(workflow_result_messages):
    print(k)
    col.append(k)
    
    count = 0
    
    for key, value in workflow_result_messages[k][1].items():
        final_dict2[k][key] = value


final_dictassemble = []
for k, vs in final_dict2.items():
    #print(k,vs)
    for kv, v in vs.items():
        for t in v:
            final_dictassemble.append([k,kv,t])



column_names = ['Workflow', 'ARS-KPs', 'Values']
df2 = pd.DataFrame(final_dictassemble, columns=column_names)
df2 = df2.astype(str)
df2.Values = df2.Values.apply(lambda x: x[2:-2] if ('[' in x) else x)
df2test = df2.groupby(['Workflow','Values'])['ARS-KPs'].agg(list)

df2test = pd.DataFrame(df2test.unstack().T)
df2test = df2test.rename_axis(None)

df2test.columns.name = None

# Highlight the cells

def highlight(v):
    if v=='Results':
        return 'background-color: %s' % 'green'
    elif v=='Error':
        return 'background-color: %s' % 'red'
    elif v == 'No Results':
        return 'background-color: %s' % 'yellow'
    elif v == 'ARS Error':
        return 'background-color: %s' % 'blue'
    elif v == 'Unknown':
        return 'background-color: %s' % 'magneta'
    else:
        return


styled = df.style.applymap(highlight)


date = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
wks_name = 'Workflow Progress Tracker_' + date


styled.to_excel('/Users/priyash/Documents/GitHub/minihackathons/Notebooks/' + wks_name + '_' + '.xlsx')


''' 

Pushing dataframe to excel sheet on google drive

Here I am using the google drive API to push the daatframe into an axcel sheet 
Every individula has the unique credential file that they need to create for google drive API -- 
"araxworkflowprogresstesting-2632632db8be.json" -- is the credential used from my drive. place this json file where
the ReadAndRunAllWorkFLows.ipynb will be. NB: i have removed my credntial file for privacy reasons. Always remove
the json file before making committs to the repo. To use googe Drive API follow: https://towardsdatascience.com/how-to-manage-files-in-google-drive-with-python-d26471d91ecd



Push the dataframe to a google sheet via google drive API and 
then format the google spread sheet to add hyperlink to pk's and color the cells

Note you have to enable the google drive API for the folder/project you need, if you are using this method to save output as google sheet

'''

# setting up creditions. Whoever running this will need to set up their google credentials with json file following the above example

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'araxworkflowprogresstesting-2632632db8be.json', scope)
gc = gspread.authorize(credentials)

'''

In the begining i had manually set up th google prject and file and now this script daily adds a sheet to the same file
if the process needs to be changed/ or completed automated to create new sheets everyday, then follow the gspread tool's manual online 
to set up to create new sheets and then pull out the key to use to push th dataframe.


'''

spreadsheet_key = '1O1cMmYGxoIqP6xbzj6FG5owiKQVg57wx2O_XIA_hN_A'
#wks_name = 'Workflow Progress Tracker' + date
d2g.upload(df, spreadsheet_key, wks_name, credentials=credentials, row_names=True)

gc = gspread.service_account(filename='/Users/priyash/Documents/GitHub/minihackathons/Notebooks/araxworkflowprogresstesting-2632632db8be.json')

gc = gspread.service_account(filename='/Users/priyash/Documents/GitHub/minihackathons/Notebooks/araxworkflowprogresstesting-2632632db8be.json')
wksh = gc.open("workflow_progress_tracker")
sh = wksh.worksheet(wks_name)




### Formating all the cells as required. 


rule = ConditionalFormatRule(
    ranges=[GridRange.from_a1_range('B2:{}18', sh)],
    booleanRule=BooleanRule(
        condition=BooleanCondition('TEXT_EQ', ['Error']),
        format=CellFormat(textFormat=textFormat(bold=True), backgroundColor=Color(1,0,0))
    )
)
rules = get_conditional_format_rules(sh)
rules.append(rule)
rules.save()


rule = ConditionalFormatRule(
    ranges=[GridRange.from_a1_range('B2:{}18', sh)],
    booleanRule=BooleanRule(
        condition=BooleanCondition('TEXT_EQ', ['Results']),
        format=CellFormat(textFormat=textFormat(bold=True), backgroundColor=Color(0.0, 0.5, 0.0))
    )
)
rules = get_conditional_format_rules(sh)
rules.append(rule)
rules.save()

rule = ConditionalFormatRule(
    ranges=[GridRange.from_a1_range('B2:{}18', sh)],
    booleanRule=BooleanRule(
        condition=BooleanCondition('TEXT_EQ', ['No Results']),
        format=CellFormat(textFormat=textFormat(bold=True), backgroundColor=Color(0.75, 0.75, 0))
    )
)
rules = get_conditional_format_rules(sh)
rules.append(rule)
rules.save()

rule = ConditionalFormatRule(
    ranges=[GridRange.from_a1_range('B2:{}18', sh)],
    booleanRule=BooleanRule(
        condition=BooleanCondition('TEXT_EQ', ['ARS Error']),
        format=CellFormat(textFormat=textFormat(bold=True), backgroundColor=Color(0.0, 0.75, 0.75))
    )
)
rules = get_conditional_format_rules(sh)
rules.append(rule)
rules.save()


# Select a range
cell_list = sh.range('B17:Y19')

# Update in batch
# Here I am updating the cells to appear as a hyperlink
sh.update_cells(cell_list,value_input_option='USER_ENTERED')



### Push second Dataframe


wks2 = 'edge_attribute_source_' + date
spreadsheet_key = '1O1cMmYGxoIqP6xbzj6FG5owiKQVg57wx2O_XIA_hN_A'
#spreadsheet_key = '1sPpBIkxrHbQNiTm5oPs9-5KrjsyXcgaVAxknJj-u8pY'
#wks_name = 'Workflow Progress Tracker_' + date
d2g.upload(df2test, spreadsheet_key, wks2, credentials=credentials, row_names=True

