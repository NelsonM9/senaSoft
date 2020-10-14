from flask.views import MethodView
from flask import  request, jsonify
from helpers.crypt import Crypt
from validators.patient_val import PatientSignin
from validators.doctor_val import DoctorSignin
from db.cloudant.cloudant_manager import CloudantManager

patient_schema = PatientSignin()
cm = CloudantManager()
crypt = Crypt()

class Signin(MethodView):
    def post(self):
        patient_signin = request.get_json()
        if patient_signin['role_p'] == patient_schema.validate(patient_signin):
            patient_signin['role_p']= "2"
            conn = cm.connect_service()
            my_db = cm.connect_db('health_db')
            if my_db == 'error':
                raise Exception
            docs = cm.get_query_by(my_db, patient_signin['email'], 'email')
            if docs != []:
                doc = docs[0]
                if patient_signin['email'] == doc['doc']['email']:
                    return jsonify({'st': "existe"})
            patient_signin['password_p'] = crypt.hash_string(patient_signin['password_p'])
            doc_msg = cm.add_doc(my_db, patient_signin)
            disconnect = cm.disconnect_db('health_db') 
            if doc_msg == "ok":
                return jsonify({'st': 'ok'}), 200
            elif doc_msg == "error":
                return jsonify({'st': 'error'}), 403
        elif patient_signin['role_d'] == patient_schema.validate(patient_signin):
            patient_signin['role_d'] = "1"
            conn = cm.connect_service()
            my_db = cm.connect_db('health_db')
            if my_db == 'error':
                raise Exception
            docs = cm.get_query_by(my_db, patient_signin['email'], 'email')
            if docs != []:
                doc = docs[0]
                if patient_signin['email'] == doc['doc']['email']:
                    return jsonify({'st': "existe"})
            patient_signin['password_p'] = crypt.hash_string(patient_signin['password_p'])
            doc_msg = cm.add_doc(my_db, patient_signin)
            disconnect = cm.disconnect_db('health_db') 
            if doc_msg == "ok":
                return jsonify({'st': 'ok'}), 200
            elif doc_msg == "error":
                return jsonify({'st': 'error'}), 403

