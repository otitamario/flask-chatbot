from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatbot import chatbot
from os import environ

app = Flask(__name__)
megabot=chatbot()
megabot.init()
megabot.training()
    

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(megabot.get_reply(userText))


if __name__ == "__main__":
    port = int(environ.get("PORT", 5000))
    app.run(debug = True, host = '0.0.0.0', port=port)