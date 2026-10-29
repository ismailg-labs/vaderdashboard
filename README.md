
# Väderdashboard – Stockholm 2025

Hej Dennis!

Detta är våran grupprojekt. Vi har byggt en Flask-app som visar historisk väderstatistik för Stockholm under förra året 2025 :)

Vi hämtar data från Open-Meteo och analyserar den med Pandas och visar temperatur och nederbörd i två interaktiva Plotly-diagram.

Vår app besvarar tre frågor:
- Vilken månad var varmast?
- Vilken månad var kallast?
- Vilken månad hade mest nederbörd?

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

** För Mac:** Använd `python3` istället för `python` i kommandona.

## API och källa

Vi använder Open-Meteo Historical Weather API.

Dokumentation: https://open-meteo.com/en/docs/historical-weather-api

Datakälla: https://open-meteo.com/
