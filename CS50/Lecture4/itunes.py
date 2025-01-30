#https://itunes.apple.com/search?entity=%20song&limit=1&term=weezer

import json
import requests
import sys

"""if len(sys.argv) != 2:
  sys.exit()"""

response = requests.get("https://itunes.apple.com/search?entity=%20song&limit=20&term=" + "weezer") #sys.argv[1]

#print(json.dumps(response.json(), indent = 2))

Sname = response.json()

for results in Sname["results"]:
    print(results["trackName"])