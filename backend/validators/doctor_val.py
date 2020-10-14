from marshmallow import validate, fields, Schema, validates, ValidationError

class DoctorSignin(Schema):
    name_d = fields.String(required=True, validate=validate.Length(min = 3, max = 20))
    mail_d = fields.String(required=True, validate=validate.Length(min = 13, max = 20))
    specialty = fields.String(required=True, validate= validate.Length(min = 5, max = 50))
    phone = fields.String(required=True, validate=validate.Length(min = 7, max = 10))
    role_d = fields.String(required=True)

    @validates(role_d)
    def validate_role_p(self, value):
        if value == '1':
            return "ok"

