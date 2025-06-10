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
    'hltinfo_pathsummary.json',
    'r'
)

ps = json.load(json_in)['result']

years = [
    '2024',
    '2023',
    '2022',
    '2018',
    '2017',
    '2016',
    '2015'
]

for year in years:

    data = []
    
    paths = ps[year]['paths']

    for path in paths:
        
        pathname = get_value(path, 'pathname')
        first_run = get_value(path, 'first_run')
        last_run = get_value(path, 'last_run')
        menu_version = ''
        
        active_lumi = get_value(path, 'active_lumi')        
        effective_lumi = get_value(path, 'effective_lumi')

        if active_lumi:
            active_lumi = float(active_lumi)/1e9

        if effective_lumi:
            effective_lumi = float(effective_lumi)/1e9
        
        datasets = path['datasets']

        for dataset in datasets:

            stream_type = dataset['stream_type']

            if stream_type in ('Physics', 'Scouting', 'Parking'):
                
                dataset_name = dataset['dataset']

                d = {
                    'path':pathname,
                    'act.lumi(fb-1)':active_lumi,
                    'eff.lumi(fb-1)':effective_lumi,
                    'first_run':first_run,
                    'last_run':last_run,
                    'menu_version':'',
                    'dataset':dataset_name,
                    'year':year
                }

                data.append(d)



    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    df = pd.DataFrame(data)
    df = df.sort_values(by='dataset', ascending=True)

    df.to_csv(
        os.path.join(
            output_dir,
            f'trigger_pathsummary_{year}.csv'
        ),
        index=False
    )

