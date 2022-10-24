from chatbot import chatbot
import json
import os

class TestStatements:

    def setup_class(self):
        self.bot=chatbot()
        self.bot.init()
        self.bot.training()
        self.database=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'training.json')
        self.file = open(self.database,'r')
        self.data_json = json.load(self.file)
        self.file.close()
        self.output_file=os.path.join(os.path.dirname(__file__), 'resultados_base.json')
        self.resultado_json={}
        self.resultado_json["erros"]=[]
    def test_questions(self):
        for i in range(5):
            for talk in self.data_json['conversations']:
                resposta_bot=str(self.bot.get_reply(talk[0].strip())).strip()
                resposta=talk[1].strip()
                assert resposta_bot==resposta,  f"Pergunta: {talk[0]}"
