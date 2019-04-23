from flask_script import Manager
from app.book.model.book import *
from app import create_app, db

app = create_app("dev")
manager = Manager(app=app)

if __name__ == "__main__":
    manager.run()
