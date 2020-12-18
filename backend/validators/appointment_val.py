from marshmallow import  validate, fields, Schema

class AppointmentVal(Schema):
<<<<<<< HEAD
    id_a = fields.Str(required=True, validator=validate.Length(min=10))
=======
    id_a = fields.Str(required=True, validator=validate.Length(max=10))
>>>>>>> 5b422e83c3aeb044af7121b13f9985c242a61d5c
    id_p = fields.Str(required=True, validator=validate.Length(min=8, max=20))
    id_d = fields.Str(required=True, validator=validate.Length(min=8, max=20))
    date_a = fields.Date(required=True)
    reason = fields.Str(required=True, validator=validate.Length(min=2, max=250))
