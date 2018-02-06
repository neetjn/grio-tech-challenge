FROM python:3.6.4
LABEL authors="John Nolette <john@neetgroup.net>"

ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    PIPENV_HIDE_EMOJIS=1

# install and update pipenv
RUN set -ex && pip3 install pipenv --upgrade
# create working directory
RUN set -ex && mkdir /opt/app
WORKDIR /opt/app
# copy pipfile to working directory
ONBUILD COPY Pipfile Pipfile
ONBUILD COPY Pipfile.lock Pipfile.lock
# install pipenv deps on system
ONBUILD RUN set -ex && pipenv install --deploy --system
# move app to working directory and start
ADD . /opt/app
CMD ls -al
CMD .venv/bin/python -m grio
