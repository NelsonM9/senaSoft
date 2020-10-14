from marshmallow import validate, fields, Schema, validates, ValidationError


class PatientSignin(Schema):
    name_p = fields.String(
        required=True, validate=validate.Length(min=3, max=20))
    mail_p = fields.String(
        required=True, validate=validate.Length(min=10, max=45))
    phone = fields.String(
        required=True, validate=validate.Length(min=7, max=10))
    age = fields.Integer(required=True)

    @validates(age)
    def validate_age(self, value):
        if value < 18:
            raise ValidationError("Debe vincularse un tutor a su grupo familiar")
    
    role_p = fields.Integer(required=True)

    @validates(role_p)
    def validate_role_p(self, value):
        if value >= 2:
            return "ok"
    
    