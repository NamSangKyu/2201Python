import json

with open('cctv.json','rt',encoding='UTF-8') as file:
    json_reader = file.read()
    dict_list = json.loads(json_reader)

    kind = set()
    #print(dict_list)
    for data in dict_list:
        #print(data['단속구분'])
        kind.add(data['단속구분'])
    print(kind)
