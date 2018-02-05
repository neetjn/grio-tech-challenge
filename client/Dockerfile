FROM node:8.9.4
LABEL authors="John Nolette <john@neetgroup.net>"

WORKDIR /opt/app
ADD . /opt/app
ONBUILD RUN npm install

EXPOSE 8080

CMD npm start
