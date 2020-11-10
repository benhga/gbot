from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_migrate import upgrade as upgrade_database
from glogic import app, db, prepare_app, parsers, models



prepare_app(environment='ms')
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def dbseed():
    with open('products.json') as f:
        for i in parsers.products_parse(f.read()):
            db.save(i)
        print("Products seeded")


if __name__ == "__main__":
    manager.run()
