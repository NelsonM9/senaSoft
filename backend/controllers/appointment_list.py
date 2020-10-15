from flask.views import MethodView
from flask import request, jsonify
from db.cloudant.cloudant_manager import CloudantManager

cm = CloudantManager()


class Appointment_list(MethodView):
    def get(self, id_p):
        try:
            cm.connect_service()
            my_db = cm.connect_db('health-db')
            if my_db == 'error':
                raise Exception
            user_docs = cm.get_query_by(my_db, id_p, 'id_p')
            list_appointments = []
            for result in user_docs:
                try:
                    appointment_id = result['doc']['id_a']
                    appointments = cm.get_query_by(
                        my_db, appointment_id, 'id_a')
                    for result_app in appointments:
                        try:
                            user_app = result_app['doc']['id_p']
                            new_appointment = {
                                'id_a': appointment_id,
                                'id_d': result_app['doc']['id_d'],
                                'id_p': user_app,
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
