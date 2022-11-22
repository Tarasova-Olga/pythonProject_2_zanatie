import json

with open('sw_templates.json') as f:
    templates = json.load(f)
print(templates)

for section, command in templates.items():
    print(section)
    print('\n'.join(command))
