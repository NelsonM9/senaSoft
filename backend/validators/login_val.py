from marshmallow import fields, Schema, validate, ValidationError

class LoginValidator(Schema):
<<<<<<< HEAD
    mail = fields.String(required=True, validate=validate.Length(min=13, max=45))
=======
    mail = fields.String(required=True, validate=validate.Length(min=13, max=50))
>>>>>>> 5b422e83c3aeb044af7121b13f9985c242a61d5c
    password = fields.String(required=True, validate=validate.Length(min=8, max=20))
