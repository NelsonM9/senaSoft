from flask.views import MethodView
from flask import request, jsonify
from helpers.crypt import Crypt
<<<<<<< HEAD
from validators.patient_val import PatientSignin
from validators.doctor_val import DoctorSignin
from db.cloudant.cloudant_manager import CloudantManager

=======
from helpers.email_confirmation import EmailConfirmation
from validators.patient_val import PatientSignin
from validators.doctor_val import DoctorSignin
from db.cloudant.cloudant_manager import CloudantManager
from db.postgresql.postgresql_manager import PostgresqlManager
from db.postgresql.model import Doctor, Patient, Family, Medicalrecord
>>>>>>> 5b422e83c3aeb044af7121b13f9985c242a61d5c

patient_schema = PatientSignin()
doctor_schema = DoctorSignin()
cm = CloudantManager()
<<<<<<< HEAD

crypt = Crypt()


class Signin(MethodView):
    def post(self):

        try:
            user_signin = request.get_json()
            if user_signin['role_d'] == "1":
                conn = cm.connect_service()
                my_db = cm.connect_db('health-db')
                if my_db == "error":
                    raise Exception
                docs = cm.get_query_by(my_db, user_signin['mail_d'], 'mail_d')
                if docs != []:
                    doc = docs[0]
                    return jsonify({'st': doc['doc']['mail_d']}), 403
                user_signin['password_d'] = crypt.hash_string(user_signin['password_d'])
                doc_msg = cm.add_doc(my_db, user_signin)

                if doc_msg == "ok":
                    return jsonify({'st': 'ok'}), 200
                elif doc_msg == "error":
                    return jsonify({'st': 'error'}), 403
            
            if user_signin['role_p'] == "2":

                conn = cm.connect_service()
                my_db = cm.connect_db('health-db')
                if my_db == "error":
                    raise Exception
                docs = cm.get_query_by(my_db, user_signin['mail_p'], 'mail_p')
                if docs != []:
                    doc = docs[0]
                    return jsonify({'st': doc['doc']['mail_p']}), 403

                user_signin['password_p'] = crypt.hash_string(user_signin['password_p'])
                doc_msg = cm.add_doc(my_db, user_signin)
                if doc_msg == "ok":
                    return jsonify({'st': 'ok'}), 200
                elif doc_msg == "error":
                    return jsonify({'st': 'error'}), 403
            
        except:
            return jsonify({"st": "error en registro"}), 403

=======
pm = PostgresqlManager()
crypt = Crypt()
mail_tool = EmailConfirmation()

class Signin(MethodView):
    def post(self):
        user_signin = request.get_json()
        try:
            conn = cm.connect_service()
            my_db = cm.connect_db('health-db')
            if my_db == "error":
                raise Exception
            try:
                if user_signin['role'] == '1':
                    errors = doctor_schema.validate(user_signin)
                    if errors:
                        return jsonify({'st': errors}), 403
                    docs = cm.get_query_by(
                        my_db, user_signin['mail'], 'mail')
                    if docs == []:
                        user_signin['password'] = crypt.hash_string(
                            user_signin['password'])
                        doc_msg = cm.add_doc(my_db, user_signin)
                        if doc_msg == "ok":
                            status = mail_tool.send_msg(user_signin['mail'])
                            return jsonify({'st': 'ok'}), 200
                        elif doc_msg == "error":
                            return jsonify({'st': 'add error'}), 403
                    else:
                        return jsonify({'st': 'exists'}),  403
                else:
                    raise Exception
            except:
                try:
                    if user_signin['role'] == '2':
                        errors = patient_schema.validate(user_signin)
                        if errors:
                            return jsonify({'st': errors}), 403
                        docs = cm.get_query_by(
                            my_db, user_signin['mail'], 'mail')
                        if docs == []:
                            user_signin['password'] = crypt.hash_string(
                                user_signin['password'])
                            doc_msg = cm.add_doc(my_db, user_signin)
                            if doc_msg == "ok":
                                status = mail_tool.send_msg(user_signin['mail'])
                                return jsonify({'st': 'ok'}), 200
                            elif doc_msg == "error":
                                return jsonify({'st': 'add error'}), 403
                        else:
                            return jsonify({'st': 'exists'}), 403
                    else:
                        raise Exception
                except:
                    return jsonify({'st': 'incorrect data'}), 403
        except:
            try:
                if user_signin['role'] == '1':
                    errors = doctor_schema.validate(user_signin)
                    if errors:
                        return jsonify({'st': errors}), 403
                    new_doctor = Doctor(
                            id_d = user_signin['id_u'],
                            name_d = user_signin['name'],
                            last_d = user_signin['last'],
                            mail_d = user_signin['mail'],
                            password_d = crypt.hash_string(user_signin['password']),
                            specialty = user_signin['specialty'],
                            phone = user_signin['phone'],
                            role_d = user_signin['role'])
                    doc_msg = pm.add(new_doctor)
                    if doc_msg == "ok":
                        return jsonify({'st': 'ok'}), 200
                    elif doc_msg == "error":
                        return jsonify({'st': 'add error'}), 403
                else:
                    raise Exception
            except:
                try:
                    if user_signin['role'] == '2':
                        errors = patient_schema.validate(user_signin)
                        if errors:
                            return jsonify({'st': errors}), 403
                        new_family = Family(
                                id_f = user_signin['id_family'],
                                id_d = None)
                        new_mrecord =  Medicalrecord(
                                id_m = user_signin['id_m'],
                                pathologies = "")
                        new_patient = Patient(
                                id_p = user_signin['id_u'],
                                name_p = user_signin['name'],
                                last_p = user_signin['last'],
                                mail_p = user_signin['mail'],
                                password_p = crypt.hash_string(user_signin['password']),
                                phone = user_signin['phone'],
                                age = user_signin['age'],
                                id_family = user_signin['id_family'],
                                role_p = user_signin['role'],
                                id_m = user_signin['id_m'])
                        doc_msg = pm.add(new_family, new_mrecord, new_patient)
                        if doc_msg == "ok":
                            return jsonify({'st': 'ok'}), 200
                        elif doc_msg == "error":
                            return jsonify({'st': 'add error'}), 403
                        else:
                            return jsonify({'st': 'nothing'}), 403
                    else:
                        return jsonify({'st', 'Incorrect local data'}), 403
                except:
                    return jsonify('st', 'Other exception'), 403
>>>>>>> 5b422e83c3aeb044af7121b13f9985c242a61d5c
