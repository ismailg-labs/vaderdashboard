import requests

#Funktion som hämtar data från den öppna API:n som defineras i url med parametrarna som defineras här under.
def hamta_vader():
    url = "https://archive-api.open-meteo.com/v1/archive"

    params = {
        "latitude": 59.3293,
        "longitude": 18.0686,
        "start_date": "2025-01-01",
        "end_date": "2025-12-31",
        "timezone": "Europe/Stockholm",
        "daily": "temperature_2m_mean,precipitation_sum",
    }

    #Skickar en GET förfrågan till väder-APIN och sparar svaret i response variabeln, raise_for_status fångar HTTP fel om det uppstår.
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    #Gör om svaret från väder-APIN som kommer som jsonfil till en dictionary. Svaret sparas sen i variabeln data.
    data = response.json()
    #if satsen kollar så raden under "daily" inte är tom, är den tom så lyfts felmeddelandet "Ingen väderdata tillgänglig" och läggs in i variabeln data.
    if not data.get("daily", {}).get("time"):
        raise ValueError("Ingen väderdata tillgänglig")
    return data
