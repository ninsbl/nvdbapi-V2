# Last ned datakatalogen og legg i riktig fil 

import json
import requests

rotdakat = 'https://www.vegvesen.no/nvdb/api/v2/vegobjekttyper'
r = requests.get( rotdakat + '.json' ) 
dakat = r.json()
for objtype in dakat: 
    r = requests.get( rotdakat + '/' + str(objtype['id'] ) + '.json')
    b = r.json()
    with open( str(objtype['id'])+'.json', 'w', encoding='utf-8') as f: 
        json.dump( b, f, ensure_ascii=False) 


