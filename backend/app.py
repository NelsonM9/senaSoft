from flask import Flask
from flask_cors import CORS
<<<<<<< HEAD
from routes import users, appointment
=======
from routes import users, document
>>>>>>> 62e4b68d397d879fd9712d1a49c7658592a2b363
from db.postgresql.model import db

app = Flask(__name__)

CORS(app, support_credentials=True)
db.init_app(app)

# User routes
app.add_url_rule(users['signin'], view_func=users['view_func_signin'])
app.add_url_rule(users['login'], view_func=users['view_func_login'])

<<<<<<< HEAD
# Appointments route
app.add_url_rule(appointment['appointment'], view_func=appointment['view_func_appointment'])
=======
# Documents route
app.add_url_rule(document['authorization'],
                 view_func=document['view_func_authorization'])
app.add_url_rule(document['order'], view_func=document['view_func_order'])
>>>>>>> 62e4b68d397d879fd9712d1a49c7658592a2b363
