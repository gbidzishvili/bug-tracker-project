from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app, origins=["http://127.0.0.1:3000/*"], supports_credentials=True)
bcrypt = Bcrypt(app)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
  from app.api.routes.user_routes import user_bp
  from app.api.routes.role_routes import role_bp
  from app.api.routes.project_routes import project_bp
  app.register_blueprint(role_bp)
  app.register_blueprint(user_bp)
  app.register_blueprint(project_bp)
  
  app.run(debug=True)