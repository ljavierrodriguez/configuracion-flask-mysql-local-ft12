from flask import Flask, render_template
from flask_migrate import Migrate
from flask_cors import CORS
from models import db

app = Flask(__name__)
app.url_map.slashes = False
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'dialect+driver://user:pass@ip-server:port/database'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/test'
db.init_app(app)
Migrate(app, db)
CORS(app)

@app.route('/')
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()