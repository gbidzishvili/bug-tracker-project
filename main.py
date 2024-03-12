from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

load_dotenv()

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
  from app.api.routes.user_routes import user_bp
  app.register_blueprint(user_bp)
  app.run(debug=True)