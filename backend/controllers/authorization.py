from flask import request, jsonify
from flask.views import MethodView
from db.cloudant.cloudant_manager import CloudantManager
<<<<<<< HEAD

cloud_manager = CloudantManager()


class Authorization(MethodView):
    def get(self, id_p):
        try:
            # Conexion a Cloudant
            cloud_manager.connect_service()
            my_db = cloud_manager.connect_db('health-db')
=======
from validators.authorization_val import AuthorizationVal

cm = CloudantManager()
authorization_schema = AuthorizationVal()

class Authorization(MethodView):
    def get(self):
        try:
            id_u = request.args.get('idu')
            # Conexion a Cloudant
            cm.connect_service()
            my_db = cm.connect_db('health-db')
>>>>>>> 5b422e83c3aeb044af7121b13f9985c242a61d5c
            if my_db == 'error':
                raise Exception
            # Falta agregar sincronizacion de las db
            # Ajustarlo para el paciente
<<<<<<< HEAD
            user_result = cloud_manager.get_query_by(
                my_db, id_p, 'id_p')
=======
            user_result = cm.get_query_by(
                my_db, id_u, 'id_p')
>>>>>>> 5b422e83c3aeb044af7121b13f9985c242a61d5c
            list_auth = []
            for result in user_result:
                try:
                    appointment_id = result['doc']['id_a']
<<<<<<< HEAD
                    orders = cloud_manager.get_query_by(
=======
                    orders = cm.get_query_by(
>>>>>>> 5b422e83c3aeb044af7121b13f9985c242a61d5c
                        my_db, appointment_id, 'id_a')
                    for order in orders:
                        try:
                            order_id = order['doc']['id_o']
<<<<<<< HEAD
                            authorizations = cloud_manager.get_query_by(
=======
                            authorizations = cm.get_query_by(
>>>>>>> 5b422e83c3aeb044af7121b13f9985c242a61d5c
                                my_db, order_id, 'id_o')
                            for auth in authorizations:
                                try:
                                    authorization_doc = auth['doc']['id_auth']
                                    new_auth = {
                                        'id_auth': authorization_doc,
                                        'id_o': order_id,
                                        'file_a': auth['doc']['file_a']}
                                    list_auth.append(new_auth)
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
            return jsonify({'st': 'ok', "authorizations": list_auth}), 200
        except:
            return jsonify({'st': 'error'}), 403
<<<<<<< HEAD
=======

    def post(self):
        try:
            authorization = request.get_json()
            errors = authorization_schema.validate(authorization)
            if errors:
                return jsonify({'st': errors}), 403
            conn = cm.connect_service()
            my_db = cm.connect_db('health-db')
            if my_db == 'error':
                raise Exception
            doc_msg = cm.add_doc(my_db, authorization)
            if doc_msg == 'ok':
                return jsonify({'st': 'ok'}), 200
            elif doc_msg == 'error':
                return jsonify({'st': 'error'}), 403
            else:
                return jsonify({'st': 'nothing'}), 403
        except:
            return jsonify({'st': 'bad'}), 403  
>>>>>>> 5b422e83c3aeb044af7121b13f9985c242a61d5c
