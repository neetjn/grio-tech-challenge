FROM python:3.6.4
LABEL authors="John Nolette <john@neetgroup.net>"

# install and update pipenv
RUN set -ex && pip install pipenv --upgrade
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
CMD python -m grio
