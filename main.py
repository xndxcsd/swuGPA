import json

import requests

value = {"swuID": "222014321210033", "password": "7281542csd", "xnm": "2015", "xqm": "1"}
url = 'http://localhost:29527/openswu/grade/'
param = json.dumps(value).encode()
head = {
    "Authorization": "Basic %s" % ("b3BlbnNvdXJjZTpmcmVlZG9t"),
    "Content-Type": "application/json; charset=utf-8",
}

try:
    response = requests.post(url, data=param, headers=head)
except ValueError.Argument:
    print (1)
else:
    print (response.text)
