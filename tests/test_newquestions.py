from unittest import TestCase
from chatbot import chatbot

class StatementTests(TestCase):

    def setUp(self):
        self.bot=chatbot()
        self.bot.init()
        self.bot.training()
        

    def test_newquestions(self):
        #self.assertEqual(self.statement.text, data['text'])
        pass