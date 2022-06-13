from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_migrate import upgrade as upgrade_database
from glogic import app, db, prepare_app, parser, models

prepare_app(environment='ms')
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def dbseed():

    with open('dbseeding/registration.json') as survey_file:
        for i in parser.questions_parse(survey_file.read(), models.RegistrationQuestions):
            db.save(i)

if __name__ == "__main__":
    app.jinja_env.cache = {}
    manager.run()
