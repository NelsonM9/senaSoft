from controllers.signin import Signin
from controllers.login import Login
from controllers.appointment import Appointment
from controllers.order import Order
from controllers.authorization import Authorization
<<<<<<< HEAD

=======
from controllers.check import Check
from controllers.result import Result
>>>>>>> 5b422e83c3aeb044af7121b13f9985c242a61d5c

users = {
    "signin": "/signin", "view_func_signin": Signin.as_view("api_signin"),
    "login": "/login", "view_func_login": Login.as_view("api_login")
}

appointment = {
<<<<<<< HEAD
    "appointment": "/appointment", "view_func_appointment": Appointment.as_view("api_appointment")
}
document = {
    "authorization": "/authorization/<id_p>", "view_func_authorization": Authorization.as_view("api_authorization"),
    "order": "/order/<id_p>", "view_func_order": Order.as_view("api_order"),
}
=======
    "appointment": "/appointment", "view_func_appointment": Appointment.as_view("api_appointment"),
}

document = {
    "authorization": "/authorization", "view_func_authorization": Authorization.as_view("api_authorization"),
    "order": "/order", "view_func_order": Order.as_view("api_order"),
    "result": "/result", "view_func_result": Result.as_view("api_result"),
}


token = {
    "check": "/check", "view_func_check": Check.as_view("api_check")
}

>>>>>>> 5b422e83c3aeb044af7121b13f9985c242a61d5c
