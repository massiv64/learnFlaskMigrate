from app import app,db # need the app and db to init migrations & command line scripts

from flask_script import Manager # this class handles command line script initialization

from flask_migrate import Migrate, MigrateCommand
# Migrate - handles migration initialization
# MigrateCommand - specifies what command line tak runs our migrations

# Initialize flask_migrate

migrate = Migrate(app,db)

# Initialize flask_script
manager = Manager(app)

# Specify what command gets attached to MigrateCommand
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
  manager.run() # start our command line script