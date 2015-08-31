import json


def find(obj, value):
    for k,v in enumerate(obj) if isinstance(obj, list) else obj.items():
        if v==value:
            return str(k)
        elif isinstance(v, (list, dict)):
            found = find(v, value)
            if found:
                return str(k) + ' -> ' + found
    

in_file = 'input/in1.json'

obj = json.loads(open(in_file).read())
print(find(obj, 'dailyprogrammer'))