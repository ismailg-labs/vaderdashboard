# Väderdashboard – Stockholm 2025

**OBS:** Denna README är en tillfällig guide för att hjälpa gruppmedlemmarna att komma igång med projektet.

Vi kommer att uppdatera och komplettera den under arbetets gång innan den slutliga inlämningen till Dennis.

Grupparbete i Programmering 2.

En Flask-app som hämtar historisk väderdata från Open-Meteo, analyserar den med Pandas och visar diagram med Plotly.

## Projektstruktur

```text
vaderdashboard/
├── application/
│   ├── __init__.py
│   ├── app.py
│   ├── api.py
│   ├── analysis.py
│   └── charts.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── dashboard.html
│   └── about.html
├── tests/
│   └── test_project.py
├── .gitignore
├── requirements.txt
├── requirements-dev.txt
├── pyproject.toml
└── README.md
```

### Vad gör filerna?

| Fil/mapp | Funktion |
|---|---|
| `application/app.py` | Flask-appen och dess routes. |
| `application/api.py` | Hämtar väderdata från API:et. |
| `application/analysis.py` | Bearbetar data med Pandas. |
| `application/charts.py` | Skapar diagram med Plotly. |
| `application/__init__.py` | Gör `application` till ett Python-paket. |
| `templates/` | HTML-sidor. `base.html` är gemensam mall. |
| `tests/` | Automatiska tester med Pytest. |
| `.gitignore` | Filer och mappar som Git ska ignorera. |
| `requirements.txt` | Appens bibliotek. |
| `requirements-dev.txt` | Test- och utvecklingsverktyg samt appens bibliotek. |
| `pyproject.toml` | Konfiguration för Pytest. |
| `README.md` | Projektinformation och installation. |

## Kom igång

### 1. Klona projektet

Kopiera repo-adressen från GitHub och kör:

```bash
git clone REPO-ADRESS
cd vaderdashboard
code .
```

### 2. Skapa och aktivera venv

**Windows – PowerShell**

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows – Git Bash**

```bash
py -m venv venv
source venv/Scripts/activate
```

**macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Installera alla beroenden

Kör med aktiverad venv:

```bash
python -m pip install -r requirements-dev.txt
```

Det installerar både appens bibliotek och utvecklingsverktygen.

**Klart! Nu kan du börja arbeta i projektet.**

När du är färdig kan du avsluta miljön med `deactivate`.

Nästa gång behöver du bara aktivera din befintliga venv igen.