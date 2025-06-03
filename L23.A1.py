dict_ = {'flowers':'dandelion','cars':['lamboghini','porsche'],'color':'red','games':'fornite'}
print(dict_)
print(dict_['cars'])
print(dict_.values())
print(dict_.keys())
print(dict_['cars'][1])
studentData = {'id1':{'name':'sarah','class':'6'},
               'id2':{'name':'david','class':'6'},
                'id3':{'name':'sarah','class':'6'}
}
result = {}
for key, value in studentData.items():
    if value not in result.values():
        result[key] = value
print(result)