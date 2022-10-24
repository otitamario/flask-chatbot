# flask-chatbot
Use this on Docker running the Dockerfile <br>
If you don't use Docker, follow these steps:
<ul>
<li>git clone git@github.com:feignbird/ChatterBot-spacy_fixed.git</li>
<li>pip install ./ChatterBot-spacy_fixed</li>
<li>pip install chatterbot-corpus \ <br>
&& pip uninstall -y pyYAML \ <br>
&& pip install pyYAML==5.3.1 \ <br>
&& python -m spacy download en_core_web_sm \ <br>
&& pip install -r requirements.txt </li>
</ul>