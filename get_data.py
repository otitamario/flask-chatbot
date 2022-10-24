import json

# Opening JSON file
#f = open('training.json','r')
#w= open("result_data.txt", "w")
# returns JSON object as
# a dictionary
#data = json.load(f)

# Iterating through the json
# list
'''for i in data['conversations']:
    w.write("{0} \n".format(i[0]))
    w.write("{0} \n".format(i[1]))
   
# Closing file
f.close()
w.close()'''
in_armas='./tests/armas_teste.txt'
in_migracao='./tests/migracao_teste.txt'
in_passaporte='./tests/passaporte_teste.txt'

out_file='./tests/data_teste.json'
ask=[]
answer=[]
conversas={}
conversas["conversations"]=[]
cont=0
with open(in_armas,'r',encoding='utf-8') as file:
    for line in file:
        cont+=1
        if(cont%2==1):
            ask.append(line.strip())
        else:
            answer.append(line.strip())

with open(in_migracao,'r',encoding='utf-8') as file:
    for line in file:
        cont+=1
        if(cont%2==1):
            ask.append(line.strip())
        else:
            answer.append(line.strip())
            
with open(in_passaporte,'r',encoding='utf-8') as file:
    for line in file:
        cont+=1
        if(cont%2==1):
            ask.append(line.strip())
        else:
            answer.append(line.strip())

for i in range(len(ask)):
    conversas["conversations"].append([ask[i],answer[i]])

print(conversas)

with open(out_file, 'w', encoding='utf-8') as f:
    json.dump(conversas, f, ensure_ascii=False, indent=4)
