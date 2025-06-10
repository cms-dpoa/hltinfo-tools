import json
import os

import pandas as pd

def get_value(data, key):
    try:
        value = data[key]
        return value
    except KeyError as exc:
        return ''

json_in = open(
    'hltinfo_menus.json',
    'r'
)

menus = json.load(json_in)['menus']

output_dir = 'output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

file_out = open(
    os.path.join(
        output_dir,
        'summary_menus.txt'
    ), 'w'
)
        
for menu in menus:
 
    for mn in menus[menu]:

        cmssw_version = mn
        run_range = []
        era = ''
        
        for m in menus[menu][mn]:
            run_range.append(m['run_number'])
            era = m['era']
            
        run_range.sort()
        first_run = run_range[:1][0]
        last_run = run_range[-1:][0]
    
        file_out.write(
            f'{first_run}-{last_run} {menu} {cmssw_version} {era}\n'
        )
    
    
            
    
    
