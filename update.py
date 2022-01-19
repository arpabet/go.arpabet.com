import requests
import json

template = """---
permalink: $NAME
---


{% include golang.html %}
"""

def create_file(name):
    content = template.replace("$NAME", name)
    with open(name + '.md', 'w') as file:
        file.write(content)


response = requests.get('https://api.github.com/users/arpabet/repos')
resp = response.json()
for entry in resp:
    if entry['language'] == 'Go':
        create_file(entry['name'])
