from flask_script import Manager, Shell
from app.book.model.book import *
from app.user.model.user import User
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db


def make_shell_context():
    return dict(app=app, db=db, Book=Book)


app = create_app("dev")
manager = Manager(app=app)
migrate = Migrate(db=db, app=app)
manager.add_command("db", MigrateCommand)

manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == "__main__":
    manager.run()
