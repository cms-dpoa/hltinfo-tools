import json
import tsgauth
import requests

auth = tsgauth.oidcauth.DeviceAuth("cms-tsg-frontend-client")
#auth = tsgauth.oidcauth.KerbSessionAuth()

result = requests.get(
    f'https://cmshltinfo.app.cern.ch/api/v0/pathsummary',
    **auth.authparams()
)

json_out = open(
    'hltinfo_pathsummary.json',
    'w'
)

json_out.write(
    json.dumps(
        result.json(),
        indent=3,
        sort_keys=True,
        separators=(',',':')
    )
)

json_out.close()



