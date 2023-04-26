from config import app
from resources.database.database import db

db.set_flask_app(app)
db.add_database('main', f"sqlite:///{app.config['FOLDER']}/databases/main.db")
db.init_SQLAlchemy()

