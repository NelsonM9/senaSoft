from flask.views import MethodView
from flask import request, jsonify
<<<<<<< HEAD
from db.cloudant.cloudant_manager import CloudantManager 
=======
from db.cloudant.cloudant_manager import CloudantManager
>>>>>>> 5b422e83c3aeb044af7121b13f9985c242a61d5c
from validators.appointment_val import AppointmentVal

cm = CloudantManager()
appointment_schema = AppointmentVal()

<<<<<<< HEAD
class Appointment(MethodView):
=======

class Appointment(MethodView):
    def get(self):
        try:
            id_u = request.args.get('idu')
            cm.connect_service()
            my_db = cm.connect_db('health-db')
            if my_db == 'error':
                raise Exception
            user_docs = cm.get_query_by(my_db, id_u, 'id_p')
            list_appointments = []
            for result in user_docs:
                try:
                    appointment_id = result['doc']['id_a']
                    appointments = cm.get_query_by(
                        my_db, appointment_id, 'id_a')
                    for result_app in appointments:
                        try:
                            new_appointment = {
                                'id_a': appointment_id,
                                'id_d': result_app['doc']['id_d'],
                                'id_p': result_app['doc']['id_p'],
                                'date_a': result_app['doc']['date_a'],
                                'reason': result_app['doc']['reason']
                            }
                            list_appointments.append(new_appointment)
                        except:
                            pass
                except:
                    pass
            return jsonify({'appointments': list_appointments}), 200
        except:
            return jsonify({'st': "error"}), 403

>>>>>>> 5b422e83c3aeb044af7121b13f9985c242a61d5c
    def post(self):
        try:
            appointment = request.get_json()
            errors = appointment_schema.validate(appointment)
            if errors:
<<<<<<< HEAD
                return jsonify({'st':errors})
            conn = cm.connect_service()
            my_db = cm.connect_db('health-db')
            print("aaa")
=======
                return jsonify({'st': errors}), 403
            conn = cm.connect_service()
            my_db = cm.connect_db('health-db')
>>>>>>> 5b422e83c3aeb044af7121b13f9985c242a61d5c
            if my_db == 'error':
                raise Exception
            doc_msg = cm.add_doc(my_db, appointment)
            if doc_msg == "ok":
<<<<<<< HEAD
                return jsonify({'st': 'ok'})
            elif doc_msg == "error":
                return jsonify({'st': 'error'})

        except:
            return jsonify({'st':"error en todo"}), 403
            
=======
                return jsonify({'st': 'ok'}), 200
            elif doc_msg == "error":
                return jsonify({'st': 'error'}), 403
            else:
                return jsonify({'st': 'nothing'}), 403 
        except:
            return jsonify({'st': "bad"}), 403
>>>>>>> 5b422e83c3aeb044af7121b13f9985c242a61d5c
