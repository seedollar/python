# Pretty printing
import pprint
import collections

result = collections.OrderedDict([('Moe', 'A wise guy, huh?'), ('Larry', 'Ow!'), ('Curly', 'Nyuk nyuk!')])
print(result)

pprint.pprint(result)
