# This example shows how you can take a json string and convert it to a Python data structure
import simplejson
import _json as json

# JSON data structure
menu = \
    {
        "breakfast": {
            "hours": "7-11",
            "items": {
                "breakfast burritos": "$6.00",
                "pancakes": "$4.00"
            }
        },
        "lunch": {
            "hours": "11-3",
            "items": {
                "hamburger": "$5.00"
            }
        },
        "dinner": {
            "hours": "3-10",
            "items": {
                "spaghetti": "$8.00"
            }
        }
    }

menu_json = simplejson.dumps(menu)
print(menu_json)

# Now convert the json string back to a data structure
json_data = simplejson.loads(menu_json)
print(json_data)
