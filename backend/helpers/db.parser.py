from db.postgresql.postgresql_manager import PostgresqlManager
from db.cloudant.cloudant_manager import CloudantManager
from db.postgresql.model import Patient

postgres_manager = PostgresqlManager()
cloud_manager = CloudantManager()

class DBP:
    def sync(self, my_db, cm):
        try:
            # Sincronizacion de las tablas
            patient_temp = postgres_manager.get_all(Patient)
            if patient_temp != []:
                for patient in patient_temp:
                    patient_nosql = {
                        'id_p': patient.id_p,
                        'name_p': patient.name_p,
                        'mail_p': patient.mail_p,
                        'password_p': patient.password_p,
                        'phone': patient.phone,
                        'age': patient.age,
                        'role_p': '2'
                    }
                    msg = cloud_manager.add_doc(my_db, patient_nosql)
                    client_del = postgres_manager.delete(patient)
            return 'ok'
        except:
            return 'error'