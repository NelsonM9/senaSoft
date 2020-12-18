from flask import jsonify, request
from flask.views import MethodView
from helpers.crypt import Crypt
from validators.login_val import LoginValidator
from db.cloudant.cloudant_manager import CloudantManager
from db.postgresql.postgresql_manager import PostgresqlManager
from config.config import KEY_TOKEN_AUTH
import jwt
import datetime

cloud_manager = CloudantManager()
postgres_manager = PostgresqlManager()
login_schema = LoginValidator()
crypt = Crypt()


class Login(MethodView):
    def post(self):
        try:
            # Se recuperan los datos y se validan
            login_user = request.get_json()
            errors = login_schema.validate(login_user)
            if errors:
<<<<<<< HEAD
                return jsonify({'st': errors})
=======
                return jsonify({'st': errors}), 403
>>>>>>> 5b422e83c3aeb044af7121b13f9985c242a61d5c
            # Conexion al servicio Cloudant
            cloud_manager.connect_service()
            # Conexion y validacion a la db
            my_db = cloud_manager.connect_db('health-db')
<<<<<<< HEAD
            print(my_db)
=======
>>>>>>> 5b422e83c3aeb044af7121b13f9985c242a61d5c
            if my_db == 'error':
                raise Exception
            # Se realiza la autenticacion de credenciales
            # Inicio de sesion para el correo de un paciente
            user_db = cloud_manager.get_query_by(
<<<<<<< HEAD
                my_db, login_user['mail'], 'mail_p')
            if user_db != []:
                user = user_db[0]
                password_result = crypt.check_hash(
                    login_user['password'], user['doc']['password_p'])
                if password_result:
                    # Construccion y envio del token
                    exp = datetime.datetime.utcnow() + datetime.timedelta(seconds=600)
                    name = user['doc']['name_p']
                    encoded_token = str(jwt.encode(
                        {'exp': exp, 'name': name}, KEY_TOKEN_AUTH, algorithm='HS256'))
                    return jsonify({'st': 'ok', 'token': encoded_token}), 200
                else:
                    return jsonify({'st': 'pass'}), 403
            # Inicio de sesion para el correo de un doctor
            user_db = cloud_manager.get_query_by(
                my_db, login_user['mail'], 'mail_d')
            if user_db != []:
                user = user_db[0]
                password_result = crypt.check_hash(
                    login_user['password'], user['doc']['password_d'])
                if password_result:
                    # Construccion y envio del token
                    exp = datetime.datetime.utcnow() + datetime.timedelta(seconds=600)
                    name = user['doc']['name_d']
                    encoded_token = str(jwt.encode(
                        {'exp': exp, 'name': name}, KEY_TOKEN_AUTH, algorithm='HS256'))
=======
                my_db, login_user['mail'], 'mail')
            if user_db != []:
                user = user_db[0]
                password_result = crypt.check_hash(
                    login_user['password'], user['doc']['password'])
                if password_result:
                    # Construccion y envio del token
                    exp = datetime.datetime.utcnow() + datetime.timedelta(seconds=600)
                    name = user['doc']['name']
                    encoded_token = jwt.encode({'exp': exp, 'name': name}, KEY_TOKEN_AUTH, algorithm='HS256')
>>>>>>> 5b422e83c3aeb044af7121b13f9985c242a61d5c
                    return jsonify({'st': 'ok', 'token': encoded_token}), 200
                else:
                    return jsonify({'st': 'pass'}), 403
            return jsonify({'st': 'email'}), 403
        except:
            return jsonify({'st': 'error'}), 403
