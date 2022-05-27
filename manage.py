from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_migrate import upgrade as upgrade_database
from glogic import app, db, prepare_app, parser

prepare_app(environment='ms')
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def dbseed():

    with open('survey.json') as survey_file:
        db.save(parser.survey_from_json(survey_file.read()))

if __name__ == "__main__":
    manager.run()
