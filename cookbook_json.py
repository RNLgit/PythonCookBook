"""
Description: example use of json communications

the cb_json structure

| widget
| |- debug
| |- window
|    |- title
|    |- name
|    |- width
|    L- height
| |- image
|    |- src
|    |- name
|    |- hOffset
|    |- vOffset
|    L- alignment
| |- text
|    |- data
|    |- size
|    |- style
|    |- name
|    |- hOffset
|    |- vOffset
|    |- alignment
L    L- onMouseUp
"""

import json

hd = open('cb_json.json')
js_hd = json.loads(hd.read())
for key in js_hd:
    print(key)

print(js_hd['widget']['window']['title'])

hd_sae = open('sae2847_json_base/InitialRequest.json')
sae_js_hd = json.loads(hd_sae.read())
print(sae_js_hd["properties"]["InitialRequest"]["properties"]["VACoilType"]["enum"][1])