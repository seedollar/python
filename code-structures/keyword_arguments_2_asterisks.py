# An illustration of a keyword argument that uses 2 asterisks, which then translates the parameters into a dictionary. The keyword will become
# the key, and it's assigned value the dictionary value. Common idiom is to call the parameter *kwargs

def capture_phones(**kwargs):
    print(kwargs)

capture_phones(samsung=868.23, nokia=124.42, asus=586.34)