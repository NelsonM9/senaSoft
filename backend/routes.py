from controllers.signin import Signin
from controllers.login import Login
from controllers.appointment import Appointment
from controllers.order import  Order
from controllers.authorization import Authorization


users = {
    "signin": "/signin", "view_func_signin": Signin.as_view("api_signin"),
    "login": "/login", "view_func_login": Login.as_view("api_login")
}

appointment = {
    "appointment": "/appointment", "view_func_appointment": Appointment.as_view("api_appointment")
}