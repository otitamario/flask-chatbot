# flask-chatbot
Use this on Docker running the Dockerfile
If you don't use Docker, follow these steps:
<ul>
<li>git clone git@github.com:feignbird/ChatterBot-spacy_fixed.git</li>
<li>pip install ./ChatterBot-spacy_fixed</li>
<li>pip install chatterbot-corpus \
&& pip uninstall -y pyYAML \
&& pip install pyYAML==5.3.1 \
&& python -m spacy download en_core_web_sm \
&& pip install -r requirements.txt </li>
</ul>