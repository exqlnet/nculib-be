from flask_script import Manager
from app.book.model.book import *
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db

app = create_app("dev")
manager = Manager(app=app)
migrate = Migrate(db=db, app=app)
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()
