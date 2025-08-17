student_data = {'Id 1':{'name':['sara'],'class':['V'],'subject_integration':['English,math,science']},'Id 2':{'name':['john'],'class':['IV'],'subject_integration':['history,social,science']},'Id 3':{'name':['jame'],'class':['X'],'subject_integration':['English,math,science']},'Id 4':{'name':['sara'],'class':['V'],'subject_integration':['English,math,science']},}
result = {}
for key,value in student_data.items():
    if value not in result.values():
        result[key] = value
print(result)