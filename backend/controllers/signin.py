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
        
        user_signin = request.get_json()
        errors = doctor_schema.validate(user_signin)
        if errors:
            return jsonify({"st":errors}), 403
        try:
            conn = cm.connect_service()
            my_db = cm.connect_db('health-db')
            if my_db == 'error':
                raise Exception
            docs = cm.get_query_by(my_db, user_signin['mail_d'], 'mail_d')
            if docs != []:
                return jsonify({'st': "existe"})
            user_signin['password_d'] = crypt.hash_string(user_signin['password_d'])
            doc_msg = cm.add_doc(my_db, user_signin)
            disconnect = cm.disconnect_db('health-db')
            if doc_msg == "ok":
                return jsonify({'st': 'ok'}), 200
            elif doc_msg == "error":
                return jsonify({'st': 'error'}), 403
            
        except:
            return jsonify({'st': "bobo hpta"}), 403
