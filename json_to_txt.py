# strings = '\u0421\u043e\u0432\u0435\u0449\u0430\u043d\u0438\u0435 \u043f\u043e \u0432\u043e\u043f\u0440\u043e\u0441\u0430\u043c \u043a\u0430\u0437\u0430\u0447\u044c\u0435\u0433\u043e \u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u044f \u0432 \u0413\u043e\u0440\u044f\u0447\u0435\u043c \u041a\u043b\u044e\u0447\u0435'
# store = strings.encode().decode()

import json,os
emp = ''
file_name = 'Irkutsk 1.json'
path = os.path.abspath(file_name)
with open(path ,'r',encoding="utf8") as file:
    get_file = file.read()
    convet_dict = eval(get_file)
    store =convet_dict.get('Title')
    for i in store:
        get_content_list = i.get('Content')
        if get_content_list != None:
            st = get_content_list
            with open('content.txt', 'a',encoding="utf8") as f:
                f.write("\n")
                f.write(st)
             

