FROM python:2.7.12
LABEL authors="John Nolette <john@neetgroup.net>"

ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    PIPENV_HIDE_EMOJIS=1

# install and update pipenv
RUN set -ex && pip install pipenv --upgrade
# create working directory
RUN set -ex && mkdir /opt/app
WORKDIR /opt/app
ADD . /opt/app
# install pipenv deps on system
RUN set -ex && pipenv install --system
# move app to working directory and start
CMD python -m grio
