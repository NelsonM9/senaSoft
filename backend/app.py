from flask import Flask
from flask_cors import CORS
from routes import users, appointment, document, token

from db.postgresql.model import db

app = Flask(__name__)

CORS(app, support_credentials=True)
db.init_app(app)

# User routes
app.add_url_rule(users['signin'], view_func=users['view_func_signin'])
app.add_url_rule(users['login'], view_func=users['view_func_login'])

# Appointments route
app.add_url_rule(appointment['appointment'], view_func=appointment['view_func_appointment'])
app.add_url_rule(appointment['appointment_list'], view_func=appointment['view_func_appointment_list'])

# Documents route
app.add_url_rule(document['authorization'],
                 view_func=document['view_func_authorization'])
app.add_url_rule(document['order'], view_func=document['view_func_order'])

# Check route
app.add_url_rule(token['check'], view_func=token['view_func_check'])

