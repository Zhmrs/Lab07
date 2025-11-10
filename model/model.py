from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        # TODO
        result=[]
        musei=self._museo_dao.read_all_museo()
        artefatti=self._artefatto_dao.read_all_artefatti()
        if musei is not None and artefatti is not None:
            for m in musei:
                for a in artefatti:
                    if museo=='Nessun filtro' and epoca == a.epoca:
                        if a not in result:
                            result.append(a)
                    elif epoca=='Nessun filtro' and museo == m.nome:
                        if m.id==a.id_museo:
                            if a not in result:
                                result.append(a)
                    elif m.nome==museo and a.epoca==epoca and m.id==a.id_museo:
                        result.append(a)
            return result
        else:
            return None

    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""
        # TODO
        lista_epoche=[]
        epoche=self._artefatto_dao.read_all_artefatti()
        if epoche is not None:
            for epoca in epoche:
                if epoca.epoca not in lista_epoche:
                    lista_epoche.append(epoca.epoca)
            return lista_epoche
        else:
            return None

    # --- MUSEI ---
    def get_musei(self):
        """ Restituisce la lista di tutti i musei."""
        # TODO
        lista_musei=[]
        musei = self._museo_dao.read_all_museo()
        if musei is not None:
            for Museo in musei:
                lista_musei.append(Museo.nome)
            return lista_musei
        else:
            return None

