import json

with open('sw_templates.json') as f:
    templates = json.load(f)
print(templates)
