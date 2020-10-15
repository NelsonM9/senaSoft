from flask import Flask
from flask_cors import CORS
<<<<<<< HEAD
from routes import users, appointment, document, token

=======
>>>>>>> b9c97c87902ee5c262e1c7c8c2bb4b34719c04be
from db.postgresql.model import db
from routes import users, document

app = Flask(__name__)

CORS(app, support_credentials=True)
db.init_app(app)

# User routes
app.add_url_rule(users['signin'], view_func=users['view_func_signin'])
app.add_url_rule(users['login'], view_func=users['view_func_login'])

<<<<<<< HEAD
# Appointments route
app.add_url_rule(appointment['appointment'], view_func=appointment['view_func_appointment'])
app.add_url_rule(appointment['appointment_list'], view_func=appointment['view_func_appointment_list'])

=======
>>>>>>> b9c97c87902ee5c262e1c7c8c2bb4b34719c04be
# Documents route
app.add_url_rule(document['authorization'],
                 view_func=document['view_func_authorization'])
app.add_url_rule(document['order'], view_func=document['view_func_order'])
<<<<<<< HEAD

# Check route
app.add_url_rule(token['check'], view_func=token['view_func_check'])

=======
>>>>>>> b9c97c87902ee5c262e1c7c8c2bb4b34719c04be
