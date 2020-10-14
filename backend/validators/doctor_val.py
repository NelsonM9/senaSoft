from marshmallow import validate, fields, Schema, validates, ValidationError


class DoctorSignin(Schema):
    id_d = fields.Str(required=True, validate=validate.Length(min=6, max=20))
    name_d = fields.Str(required=True, validate=validate.Length(min=3, max=20))
    mail_d = fields.Str(
        required=True, validate=validate.Length(min=13, max=45))
    password_p = fields.Str(
        required=True, validate=validate.Length(min=8, max=20))
    specialty = fields.Str(
        required=True, validate=validate.Length(min=5, max=30))
    phone = fields.Str(required=True, validate=validate.Length(min=7, max=10))
    role_d = fields.Str(required=True, validate=validate.Equal('1'))
