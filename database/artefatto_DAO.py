from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    # TODO

    @staticmethod
    def read_all_artefatti():
        results = []
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("Connessione fallita")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT *
                        FROM artefatto """

            cursor.execute(query)
            for row in cursor:
                # Posso creare oggetti di tipo Artefatto
                artefatti = Artefatto(row["id"], row["nome"], row["tipologia"], row["epoca"], row["id_museo"])
                results.append(artefatti)
            cursor.close()
            cnx.close()
            return results

