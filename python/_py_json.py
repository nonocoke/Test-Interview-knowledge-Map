import json
from pprint import pprint

data = {
    'name' : 'ACME',
    'shares' : 100,
    'price' : 542.23
}
pprint(data)
json_str = json.dumps(data)
pprint(json_str)
data = json.loads(json_str)
pprint(data)