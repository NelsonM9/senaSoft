from controllers.signin import Signin
from controllers.login import Login
from controllers.appointment import Appointment
from controllers.order import Order
from controllers.authorization import Authorization


users = {
    "signin": "/signin", "view_func_signin": Signin.as_view("api_signin"),
    "login": "/login", "view_func_login": Login.as_view("api_login")
}

<<<<<<< HEAD
appointment = {
    "appointment": "/appointment", "view_func_appointment": Appointment.as_view("api_appointment")
}
=======
document = {
    "authorization": "/authorization/<id_p>", "view_func_authorization": Authorization.as_view("api_authorization"),
    "order": "/order/<id_p>", "view_func_order": Order.as_view("api_order"),
}
>>>>>>> 62e4b68d397d879fd9712d1a49c7658592a2b363
