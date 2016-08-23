import report as rep
from report import get_temperature as get_temp

print(rep.get_description())

def feeling_cold():
    print (get_temp())

feeling_cold()

