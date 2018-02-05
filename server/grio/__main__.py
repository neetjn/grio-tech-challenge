from grio.db import drop_database, bootstrap
from grio.constants import APP_HOST, APP_PORT, BOOTSTRAP
from grio.api import app


if __name__ == '__main__':
    if BOOTSTRAP:
        drop_database()
        bootstrap()

    app.run(host=APP_HOST, port=int(APP_PORT), threaded=True, processes=1)
