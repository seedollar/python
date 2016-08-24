import csv, pprint

with open("villians.csv", "rt") as fin:
    cin = csv.reader(fin)
    villans = [row for row in cin]

pprint.pprint(villans)
