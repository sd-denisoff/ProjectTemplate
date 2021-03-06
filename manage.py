import os
import shutil

from app import application, db, manager
from app.api import routes


@manager.command
def runserver():
    if not os.path.exists('database.db'):
        db_reset()
    application.config['HOST'] = 'localhost:5000/'
    application.register_blueprint(routes.api, url_prefix='/')
    application.run(host='localhost', port=5000, debug=True)


@manager.command
def db_delete():
    if os.path.exists('migrations'):
        shutil.rmtree('migrations')
    if os.path.exists('database.db'):
        os.remove('database.db')


@manager.command
def db_reset():
    db.drop_all()
    db.create_all()


if __name__ == '__main__':
    manager.run()
