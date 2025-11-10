import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dropdown(self):
        lista_musei=self._model.get_musei()
        lista_epoche=self._model.get_epoche()
        if lista_epoche is not None and lista_epoche is not None:
            musei=['Nessun filtro']+lista_musei
            epoche=['Nessun filtro']+lista_epoche

            self._view.filtraggio_musei.options.clear()
            self._view.filtraggio_epoca.options.clear()
            for m in musei:
                self._view.filtraggio_musei.options.append(ft.dropdown.Option(m))

            for e in epoche:
                self._view.filtraggio_epoca.options.append(ft.dropdown.Option(e))

            # Aggiorno la pagina
            self._view.update()
        else:
            self._view.show_alert('Non connesso al database')


    # CALLBACKS DROPDOWN
    # TODO
    # Tengo traccia del valore impostato dall'utente
    def on_museo_change(self, e):
        self.museo_selezionato = self._view.filtraggio_musei.value

    def on_epoca_change(self, e):
        self.epoca_selezionata = self._view.filtraggio_epoca.value


    # AZIONE: MOSTRA ARTEFATTI
    # TODO
    def mostra_artefatti(self,e):
        museo = self.museo_selezionato
        epoca = self.epoca_selezionata

        if museo is None or epoca is None:
            self._view.show_alert('Nessun valore selezionato per museo/epoca')
        else:
            # Ottengo gli artefatti filtrati dal Model
            artefatti = self._model.get_artefatti_filtrati(museo, epoca)

            # Pulisco la lista prima di riempirla
            self._view.lista_artefatti.controls.clear()

            # Mostro i risultati oppure un messaggio
            if artefatti is not None:
                if len(artefatti) > 0:
                    for a in artefatti:
                        self._view.lista_artefatti.controls.append(ft.Text(str(a)))
                else:
                    self._view.show_alert("Nessun artefatto trovato.")
            else:
                self._view.show_alert('Non connesso al database')

        # Aggiorno la pagina
        self._view.update()

