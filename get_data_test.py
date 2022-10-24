import json

in_armas='./tests/armas_teste.txt'
in_migracao='./tests/migracao_teste.txt'
in_passaporte='./tests/passaporte_teste.txt'

out_file='./tests/data_teste_tag.json'
ask=[]
answer=[]
tag=[]
conversas={}
conversas["conversations"]=[]
cont=0
with open(in_armas,'r',encoding='utf-8') as file:
    for line in file:
        cont+=1
        if(cont%2==1):
            ask.append(line.strip())
            tag.append('armas')
        else:
            answer.append(line.strip())

with open(in_migracao,'r',encoding='utf-8') as file:
    for line in file:
        cont+=1
        if(cont%2==1):
            ask.append(line.strip())
            tag.append('migracao')
        else:
            answer.append(line.strip())
            
with open(in_passaporte,'r',encoding='utf-8') as file:
    for line in file:
        cont+=1
        if(cont%2==1):
            ask.append(line.strip())
            tag.append('passaporte')
        else:
            answer.append(line.strip())

for i in range(len(ask)):
    valor={"id":i,"tag":tag[i],"pergunta: ":ask[i],"resposta":answer[i],"erros":0}
    conversas["conversations"].append(valor)

print(conversas)

with open(out_file, 'w', encoding='utf-8') as f:
    json.dump(conversas, f, ensure_ascii=False, indent=4)
