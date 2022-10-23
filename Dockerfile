FROM python:3.7.15-slim-buster

USER root
COPY . /megabot-hilca
WORKDIR /megabot-hilca



RUN apt-get update && apt-get install -y --no-install-recommends apt-utils \
    && apt-get -y install curl \
    && apt-get install libgomp1 \
    && apt-get install -y git



RUN chgrp -R 0 /megabot-hilca \
    && chmod -R g=u /megabot-hilca \
    && pip install pip --upgrade \
    && git clone https://github.com/gunthercox/ChatterBot.git \
    && pip install ./ChatterBot \
    && pip install -r requirements.txt \
    && pip install spacy \
    &&  python -m spacy download en_core_web_sm \\
    && pip install chatterbot_corpus

CMD ["gunicorn", "app:app","--preload"]