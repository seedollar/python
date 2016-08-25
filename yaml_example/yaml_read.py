import yaml
with open('mcintyre.yml', 'rt') as yin:
     text = yin.read()

data = yaml.load(text)
print(data)

print(data['poems'][1]['title'])
