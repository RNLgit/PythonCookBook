"""
Title : cookbook_json.py

Description: example use of json communications

Author: Runnan Li

**Revision History:**

+---------+------------+------------+-----------------------------------------------------+
| Version |     Date   |   Author   |                  Change Description                 |
+---------+------------+------------+-----------------------------------------------------+
|   0.1   | 24/02/2021 | Runnan Li  |                   Initial Version                   |
+---------+------------+------------+-----------------------------------------------------+

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