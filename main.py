from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)
app.config.from_pyfile('config.py')
api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
  app.run(debug=True)