# grio-tech-challenge

## About

I took this project as an opportunity to familiarize myself with Pipenv workflow and the Peewee ORM. The challenge was to build a web application that takes a collection of users from a provided JSON document and loads them into a relational database such as MySQL or Postgres. The challenge also entails building an SPA to search for the given users.

I tried to build the CRUD api in a manner where it would very easily be converted into a microservice. I added prelim. support for resource href mapping/identification.

![https://i.gyazo.com/03a8220230a0bfe46ecd64571e2f8b99.png](https://i.gyazo.com/03a8220230a0bfe46ecd64571e2f8b99.png)

## Stack

Backend

- Python 3
- Flask (http server)
- Peewee (Orm for Postgres)
- pytest

Frontend

- Vue.js
- Webpack
- Bulma/Bulmaswatch
- Foundation Icons
- Sass
- Axios (content manager > fetch)

## Setting Up

The backend is using pipenv to manage Py packages.
Once the required packages are installed, the backend can be spun up fairly easily.
All database and app configurations can be found in the `grio/constants.py` module.

Use `python -m grio` to start the flask app. To bootstrap your environment for first time use, use `BOOTSTRAP=1 python -m grio`.


All frontend dependencies can be installed like so,

```bash
npm install
```

To lint our Vue components you may use,

```bash
npm run lint
```

Runnin the application in your dev environment is also as easy as,

```bash
npm run dev
```

## Testing

The backend tests *only* cover the application core, I didn't actually mock out requests because it wouldn't yield efficient or relevant results.

## Lacking

What I wasn't able to get to due to a lack of time was client sided test. I'd planned to write up a few simple tests using Jest, but I'd have to mock the Vue event dispatcher which I didn't have time to deal with prior to submission.

I also planned to add pagination to the frontend, it's already supported by the backend.

I'd planned to have the entire app dockerize and ship it with a docker compose / ansible playbook, though it seems Pipenv cannot currently (2/6/18) function properly in a dockerized environment.
