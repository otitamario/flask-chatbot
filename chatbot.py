from chatterbot import ChatBot
#from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.comparisons import LevenshteinDistance
#from chatterbot.comparisons import SpacySimilarity
#from chatterbot.comparisons import JaccardSimilarity
#from chatterbot.conversation import Statement


from chatterbot.response_selection import get_most_frequent_response


class ENGSM:
    #ISO_639_1 = 'en_core_web_sm'
    ISO_639_1 ='pt_core_news_md'

class chatbot:
    bot = None
    conversa=None
    botname='MegaBot'
    file_training="./training.json"
    exit_conditions = (":q", "quit", "exit","-1","sair","tchau","bye")
    database_uri='sqlite:///chatbot.sqlite3'
    #training_data = open('training.txt').read().splitlines()
        
    def init(self):
        self.bot = ChatBot(
            self.botname,
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            database_uri=self.database_uri,
            tagger_language=ENGSM,
            
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'default_response': 'Desculpa, ainda não sei responder esta pergunta.',
                    'maximum_similarity_threshold': 0.90,
                    "statement_comparison_function": LevenshteinDistance,
                    "response_selection_method": get_most_frequent_response
                }
            ], input_adapter='chatterbot.input.TerminalAdapter',
            output_adapter='chatterbot.output.TerminalAdapter')

    def get_reply(self, data):
        return self.bot.get_response(data)

    def training(self):
        #self.conversa = ListTrainer(self.bot)
        #self.conversa.train(self.training_data)
        self.conversa = ChatterBotCorpusTrainer(self.bot)
        self.conversa.train(
            self.file_training
        )
        
        self.conversa.train("chatterbot.corpus.portuguese",
            "chatterbot.corpus.portuguese.greetings",
            "chatterbot.corpus.portuguese.conversations"
        )
    


        

    def run(self):
        print(f"{self.botname}: Olá tudo bem. Sou um Bot e estou aqui para responder sobre assuntos da Polícia Federal: passaporte, armas e migração")
        while True:
            try:
                pergunta = input("Usuário: ")
                if pergunta in self.exit_conditions:
                    break
                resposta = self.get_reply(pergunta)
                if float(resposta.confidence) > 0.5:
                    print(f"{self.botname}: {resposta}")
                else:
                    print(f"{self.botname} Não entendi")
            except Exception as err:
                print(err)
                pass
