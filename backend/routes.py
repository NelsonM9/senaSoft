from controllers.signin import Signin
from controllers.login import Login
from controllers.appointment import Appointment
from controllers.order import Order
from controllers.authorization import Authorization
from controllers.appointment_list import Appointment_list
from controllers.check import  Check


users = {
    "signin": "/signin", "view_func_signin": Signin.as_view("api_signin"),
    "login": "/login", "view_func_login": Login.as_view("api_login")
}

<<<<<<< HEAD
appointment = {
    "appointment": "/appointment", "view_func_appointment": Appointment.as_view("api_appointment"),
    "appointment_list": "/appointment_list/<id_p>", "view_func_appointment_list": Appointment_list.as_view("api_appointment_list")
}

=======
>>>>>>> b9c97c87902ee5c262e1c7c8c2bb4b34719c04be
document = {
    "authorization": "/authorization/<id_p>", "view_func_authorization": Authorization.as_view("api_authorization"),
    "order": "/order/<id_p>", "view_func_order": Order.as_view("api_order"),
}

<<<<<<< HEAD
token = {
    "check": "/check", "view_func_check": Check.as_view("api_check")
}
=======
>>>>>>> b9c97c87902ee5c262e1c7c8c2bb4b34719c04be
