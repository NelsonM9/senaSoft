from controllers.signin import Signin
from controllers.login import Login
from controllers.appointment import Appointment
from controllers.orderauth import  OrderAuth

users = {
    "signin": "/signin", "view_func_signin": Signin.as_view("api_signin"),
    "login": "/login", "view_func_login": Login.as_view("api_login")
}

appointment = {
    "appointment": "/appointment", "view_func_appointment": Appointment.as_view("api_appointment")
}

orderauth = {
    "orderauth": "/orderauth", "view_func_orderauth": OrderAuth.as_view("api_orderauth")
}