import csv

villains = [
['Doctor', 'No'],
['Rosa', 'Klebb'],
['Mister', 'Big'],
['Auric', 'Goldfinger'],
['Ernst', 'Blofeld'],
]

with open("villians.csv", "wt") as fout:
    csvout = csv.writer(fout)
    csvout.writerows(villains)


