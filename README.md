
# Väderdashboard – Stockholm 2025

Hej Dennis!

Detta är våran grupprojekt. Vi har byggt en Flask-app som visar historisk väderstatistik för Stockholm under förra året 2025 :)

Vi hämtar data från Open-Meteo och analyserar den med Pandas och visar temperatur och nederbörd i två interaktiva Plotly-diagram.

Vår app besvarar tre frågor:
- Vilken månad var varmast?
- Vilken månad var kallast?
- Vilken månad hade mest nederbörd?

## Projektstruktur
Vår project är uppdelad i följande filer och mappar (se nedan):

```text
vaderdashboard/
├── application/
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── dashboard.html
│   │   └── about.html
│   ├── __init__.py
│   ├── app.py
│   ├── api.py
│   ├── analysis.py
│   └── charts.py
├── tests/
│   └── test_project.py
├── .gitignore
├── requirements.txt
├── requirements-dev.txt
├── pyproject.toml
└── README.md
```

## Liten förklaring gällande vad de viktigaste filerna och mapparna gör
- `app.py` - Hanterar våra Flask routes och kopplar ihop modulerna med varandra.
- `api.py` - Skickar själva api anropet och hämtar datan från Open-Meteo.
- `analysis.py` - Bearbetar api datan med pandas.
- `charts.py` - Skapar diagrammen med hjälp av Plotly.
- `templates/` - Inehåller html mallarna.
- `tests/` - Inehåller våra 6 tester.

## Installation

Börja med att clone projektet och öppna projektmappen:

```bash
git clone https://github.com/ismailg-labs/vaderdashboard.git
cd vaderdashboard
```

**Windows:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Mac:**

```bash
python3 -m venv venv
source venv/bin/activate
```

Installera sedan beroenden:

Filen requirements-dev.txt installerar även allt från requirements.txt så man behöver köra bara ett installationskommando

```bash
python -m pip install -r requirements-dev.txt
```

## Starta appen

```bash
python -m flask --app application.app run
```

Öppna http://127.0.0.1:5000 i webbläsaren. Klicka sedan på **Dashboard** i navigeringsmenyn för att se statestiken och diagrammen.

## Tester och Ruff

Kör testerna:

```bash
python -m pytest
```

Kontrollera kod och formatering:

```bash
python -m ruff check .
python -m ruff format --check .
```

**För Mac:** Använd `python3` istället för `python` i kommandona.

## API och källa

Vi använder Open-Meteo Historical Weather API.

Dokumentation: https://open-meteo.com/en/docs/historical-weather-api

Datakälla: https://open-meteo.com/
