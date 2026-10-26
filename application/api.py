import requests

def hamta_vader():
    url = "https://archive-api.open-meteo.com/v1/archive"

    params = {  
        "latitude":59.3293,
        "longitude":18.0686,
        "start_date": "2025-01-01",
        "end_date": "2025-12-31",
        "timezone": "Europe/Stockholm",
        "daily": "temperature_2m_mean,precipitation_sum",
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    if not data.get("daily", {}).get("time"):
        raise ValueError("Ingen väderdata tillgänglig")
    return data



