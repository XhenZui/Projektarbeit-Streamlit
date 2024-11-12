# Projekt-Arbeit-Streamlit
Diese Arbeit wurde im Rahmen der Projektarbeit mit dem Titel "Webentwicklung mit Streamlit und Python" im Wintersemester 24/25 an der Hochschule Karlsruhe erstellt. 

# Stack
- streamlit.io https://docs.streamlit.io/
- pixi https://pixi.sh/latest/basic_usage/
- streamlit-folium https://folium.streamlit.app/
- pickle https://docs.python.org/3/library/pickle.html


# Setup & Ausführung
Für die Installation wird pixi von prefix dev benötigt (siehe stack).
- Installieren der dependencies mit: `pixi install`
- Ausführen mit vscode launch configs oder mit: `pixi run streamlit run travel_log.py`
- Streamlit installation prüfen mit: `pixi run streamlit hello`
# Datenspeicherung
Der aktuelle Zustand der App (Inhalt der log liste) wird als Datei mithilfe der pickle library gespeichert. Bei einem neustart wird der letzte Stand aus der Datei ausgelesen.
# Travel Log
Travel Log ist eine App zur erstellung eines Logbuches von Reisen. Dieses Logbuch kann nicht nur Text einträge speichern sondern auch bilder sowie die Position auf einer Karte.

__Benutzeroberfläche__

Auf der Linken seite der Beenutzeroberfläche wird die Karte angezeigt, diese zeigt je Log eintrag einen Nummerierenten Marker an. Auf der Rechten seite sieht man die Buttons zum erstellen neuer Einträge, zum Löschen aller einträge und zum erstellen eines zufälligen eintrags. Darunter sieht man die Log List, diese hat je logeintrag eine auffaltbare kachel. Im nicht aufgefalteten zustand wird die Nummer sowie der Titel angezeigt. Die Nummer des eintrags entspricht der Nummer der marker auf der Karte sodass man die Marker den einträgen zuordnen kann.

![plot](mainpage.png)

__Log Liste__

Die Log Liste zeigt wie bereits erwähnt je Log eintrag eine aufklapbare Kachel an. Wird die Kachel aufgeklappt so werden alle informationen zu diesem Log eintrag angezeigt wie z.b. das Bild oder die Beschreibung. Zudem befindet sich am unteren ende der aufgeklappten Kachel der Button zum editieren des eintrags.

![plot](log_list.png)

__Neuen Eintrag erstellen__

Möchte der Anwender einen neuen Eintrag erstellen kann er den Create log entry Button drücken. Sobald er dies tut erscheinen zwei Eingabefelder zum eingeben des Namens so wie einer beschreibung. Zustäzlich hat der Anwender die Möglichkeit auf die Karte zu Klicken um den Marker zu Platzieren, dieser erscheint dann zunächst als Blauer Marker auf der Karte. Bestätigt der Anwender das erstellen mit dem Confirm create button dann wird der Eintrag ins log gespeichert und wird in der Log List angezeigt. Alternativ kann er mit Cancel das Anlegen abbrechen. 

![plot](create.png)

__Eintrag Bearbeiten__

Zum Bearbeiten von bestehenden Einträgen hat jeder eintrag in der Log liste einen edit Button. Drückt man diesen erscheint ein Modaler Dialog zum Bearbeiten des Eintrags. In diesem kann der Name, die Beschreibung eine Addresse sowie die Koordinaten des Markers Bearbeitet werden. Zusätzlich kann auch noch ein Bild hochgeladen werden. Um die Änderungen zu Speichern muss der Submit Button gedrückt werden.

![plot](edit_dialog.png)

# Fazit zu Streamlit
Positiv:
- Anlegen einer neuen App ist sehr einfach und unproblematisch
- Einfaches anzeigen von Markdown
- layouts konzept simpel und praktisch
- keine tiefen python kenntnisse notwendig

Negativ:
- state ist nicht ganz einfach
- konzept bei welchen aktionen der python code erneut ausgeführt führt anfangs zu verwirrung
- Standard komponenten teilweise nicht sehr umfangreich, z.b. können st.expander nicht verschachtelt werden
- Beim dynamisches erstellen von Elementen dürfen zwei Elemente nicht denselben Namen haben