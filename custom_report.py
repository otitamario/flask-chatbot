from chatbot import chatbot
import json
import os
import logging 

class Custom:

    def __init__(self):
        self.bot=chatbot()
        self.bot.init()
        self.bot.training()
        self.database_teste=os.path.join(os.path.dirname(__file__), './tests/data_teste.json')
        self.file_teste = open(self.database_teste,'r')
        self.data_json_teste = json.load(self.file_teste)
        self.file_teste.close()
        self.database=os.path.join(os.path.dirname(__file__), 'training.json')
        self.file = open(self.database,'r')
        self.data_json = json.load(self.file)
        self.file.close()
        self.file_report=os.path.join(os.path.dirname(__file__), 'relatorio.txt')
        self.output_file_teste=os.path.join(os.path.dirname(__file__), 'resultados_teste.json')
        self.output_file_base=os.path.join(os.path.dirname(__file__), 'resultados_base.json')
        self.resultado_json_teste={}
        self.resultado_json_teste["erros"]=[]
        self.resultado_json={}
        self.resultado_json["erros"]=[]
        self.total_testes=0
        self.total_testes_erro=0
        self.total_testes_base=0
        self.total_testes_erro_base=0
        self.total_testes_testes=0
        self.total_testes_erro_testes=0
        
        
        self.len_teste=0
        self.len_base=0

    def test_newquestions(self):
        self.len_teste=len(self.data_json_teste['conversations'])
        print("Total perguntas Teste: ",self.len_teste)
        for i in range(5):
            for talk in self.data_json_teste['conversations']:
                self.total_testes+=1
                self.total_testes_testes+=1
                resposta_bot=str(self.bot.get_reply(talk[0].strip())).strip()
                resposta=talk[1].strip()
                try:
                    assert resposta_bot==resposta,  f"Pergunta: {talk[0]}"
                except AssertionError:
                    self.resultado_json_teste["erros"].append({"Pergunta:":talk[0],"resp_bot":resposta_bot,"resp_correta":resposta})
                    print(f"Pergunta Teste falhou: {talk[0]}")
                    self.total_testes_erro+=1
                    self.total_testes_erro_testes+=1
        with open(self.output_file_teste, 'w', encoding='utf-8') as f:
            json.dump(self.resultado_json_teste, f, ensure_ascii=False, indent=4)

    def test_questions(self):
        self.len_base=len(self.data_json['conversations'])
        print("Total perguntas: ",self.len_base)
        for i in range(5):
            for talk in self.data_json['conversations']:
                self.total_testes+=1
                self.total_testes_base+=1
                resposta_bot=str(self.bot.get_reply(talk[0].strip())).strip()
                resposta=talk[1].strip()
                try:
                    assert resposta_bot==resposta,  f"Pergunta: {talk[0]}"
                except AssertionError:
                    self.resultado_json["erros"].append({"Pergunta:":talk[0],"resp_bot":resposta_bot,"resp_correta":resposta})
                    print(f"Pergunta falhou: {talk[0]}")
                    self.total_testes_erro+=1
                    self.total_testes_erro_base+=1
        with open(self.output_file_base, 'w', encoding='utf-8') as f:
            json.dump(self.resultado_json, f, ensure_ascii=False, indent=4)


if __name__=='__main__':
    logger = logging.getLogger() 
    logger.setLevel(logging.CRITICAL)
    Test=Custom()
    Test.test_questions()
    Test.test_newquestions()
    taxa_acerto=round(100-float(Test.total_testes_erro/Test.total_testes)*100,2)
    taxa_acerto_teste=round(100-float(Test.total_testes_erro_testes/Test.total_testes_testes)*100,2)
    taxa_acerto_base=round(100-float(Test.total_testes_erro_base/Test.total_testes_base)*100,2)
    msg='RELATÓRIO \n'
    print("Total perguntas: {} \n Total perguntas Teste: {} \n".format(Test.len_base,Test.len_teste))
    print("Total de Testes: {} \n  Total Erros: {}".format(Test.total_testes,Test.total_testes_erro))
    print("Taxa de acertos Total: ",taxa_acerto)
    print('------------------BASE ORIGINAL---------------------------------------------')
    print("Total de Testes da Base Original: {} \n  Total Erros: {}".format(Test.total_testes_base,Test.total_testes_erro_base))
    print("Taxa de acertos Total Base Original: ",taxa_acerto_base)
    print('-----------------BASE TESTE----------------------------------------------')
    print("Total de Testes da Base Teste : {} \n  Total Erros: {}".format(Test.total_testes_testes,Test.total_testes_erro_testes))
    print("Taxa de acertos Total Base Teste: ",taxa_acerto_teste)
    msg+="Total perguntas: {} \n Total perguntas Teste: {} \n".format(Test.len_base,Test.len_teste)
    msg+="Total de Testes: {} \n  Total Erros: {} \n".format(Test.total_testes,Test.total_testes_erro)
    msg+="Taxa de acertos Total: "+str(taxa_acerto)+'\n'
    msg+='------------------BASE ORIGINAL---------------------------------------------\n'
    msg+="Total de Testes da Base Original: {} \n  Total Erros: {} \n".format(Test.total_testes_base,Test.total_testes_erro_base)+'\n'
    msg+="Taxa de acertos Total Base Original: "+str(taxa_acerto_base)+'\n'
    msg+='-----------------BASE TESTE----------------------------------------------\n'
    msg+="Total de Testes da Base Teste : {} \n  Total Erros: {} \n".format(Test.total_testes_testes,Test.total_testes_erro_testes)+'\n'
    msg+="Taxa de acertos Total Base Teste: "+str(taxa_acerto_teste)
    with open(Test.file_report, 'w', encoding='utf-8') as f:
            f.write(msg)
    


