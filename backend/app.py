from flask import Flask
from flask_cors import CORS
from db.postgresql.model import db
from routes import users, document

app = Flask(__name__)

CORS(app, support_credentials=True)
db.init_app(app)

# User routes
app.add_url_rule(users['signin'], view_func=users['view_func_signin'])
app.add_url_rule(users['login'], view_func=users['view_func_login'])

# Documents route
app.add_url_rule(document['authorization'],
                 view_func=document['view_func_authorization'])
app.add_url_rule(document['order'], view_func=document['view_func_order'])
