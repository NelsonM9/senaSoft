from flask.views import MethodView
from flask import request, jsonify
from helpers.crypt import Crypt
from validators.patient_val import PatientSignin
from validators.doctor_val import DoctorSignin
from db.cloudant.cloudant_manager import CloudantManager


patient_schema = PatientSignin()
doctor_schema = DoctorSignin()
cm = CloudantManager()

crypt = Crypt()


class Signin(MethodView):
    def post(self):
        try:
            user_signin = request.get_json()
            conn = cm.connect_service()
            my_db = cm.connect_db('health-db')
            if my_db == "error":
                raise Exception
            try:
                if user_signin['role_d'] == '1':
                    errors = doctor_schema.validate(user_signin)
                    if errors:
                        return jsonify({'st': errors})
                    docs = cm.get_query_by(
                        my_db, user_signin['mail_d'], 'mail_d')
                    if docs == []:
                        user_signin['password_d'] = crypt.hash_string(
                            user_signin['password_d'])
                        doc_msg = cm.add_doc(my_db, user_signin)
                        if doc_msg == "ok":
                            return jsonify({'st': 'ok'}), 200
                        elif doc_msg == "error":
                            return jsonify({'st': 'add error'}), 403
                    else:
                        return jsonify({'st': 'exists'}),  403
            except:
                try:
                    if user_signin['role_p'] == '2':
                        errors = patient_schema.validate(user_signin)
                        if errors:
                            return jsonify({'st': errors})
                        docs = cm.get_query_by(
                            my_db, user_signin['mail_p'], 'mail_p')
                        if docs == []:
                            user_signin['password_p'] = crypt.hash_string(
                                user_signin['password_p'])
                            doc_msg = cm.add_doc(my_db, user_signin)
                            if doc_msg == "ok":
                                return jsonify({'st': 'ok'}), 200
                            elif doc_msg == "error":
                                return jsonify({'st': 'add error'}), 403
                        else:
                            return jsonify({'st': 'exists'}), 403
                except:
                    return jsonify({'st': 'incorrect data'}), 403
        except:
            return jsonify({"st": "register"}), 403
