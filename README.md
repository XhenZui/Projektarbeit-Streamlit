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
Travel Log ist eine App zur erstellung eines Logbuches von Reisen.
Dabei 
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