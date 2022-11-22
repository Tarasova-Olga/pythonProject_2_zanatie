import json

with open('sw_templates.json') as f:
    content = f.read()
    templates = json.loads(content)
print(templates)
