# hltinfo-tools
Tools for extracting HLT information for open data from [HLT Info](https://cmshltinfo.app.cern.ch/)

## Install
```
virtualenv dpoa
source dpoa/bin/activate
pip install -r requirements.txt
```

## Run

Use the [HLTInfo API](https://gitlab.cern.ch/cms-tsg/steam/hltinfo/-/blob/main/hltinfoapi/app.py?ref_type=heads) to dump the summary information
for the HLT paths to a file `hltinfo_pathsummary.json`:
```
python3 dump_hltinfo_pathsummary.py
```

Then parse the json file and output csv summary files for each year:
```
python3 dump_hltinfo_pathsummary_csv.py
```
