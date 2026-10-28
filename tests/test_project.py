from unittest.mock import Mock, patch

import pandas as pd
import pytest
import requests

from application.analysis import bearbeta_manader, sammanfatta
from application.api import hamta_vader
from application.app import app


# Testet kontrollerar att hamta_vader skickar ett felmeddelande vid timeout.
def test_api_timeout():
    with patch("application.api.requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.Timeout

        with pytest.raises(requests.exceptions.Timeout):
            hamta_vader()


# Testet använder egen testdata med två dagar i januari och en dag i februari, där värdena är valda så att det förväntade resultatet kan räknas fram för hand.
def test_bearbeta_manader():

    fake_data = {
        "daily": {
            "time": ["2025-01-01", "2025-01-02", "2025-02-01"],
            "temperature_2m_mean": [2, 4, 10],
            "precipitation_sum": [1, 3, 5],
        }
    }

    resultat = bearbeta_manader(fake_data)

    assert resultat.iloc[0]["month"] == 1
    assert resultat.iloc[0]["medeltemp"] == 3
    assert resultat.iloc[0]["nederbord"] == 4

    assert resultat.iloc[1]["month"] == 2
    assert resultat.iloc[1]["medeltemp"] == 10
    assert resultat.iloc[1]["nederbord"] == 5


# Testet kollar om den hittar varmaste kallaste och blötaste månaden.
def test_sammanfatta():
    manader = pd.DataFrame(
        {"month": [3, 6, 12], "medeltemp": [5, 18, -4], "nederbord": [40, 20, 90]}
    )

    resultat = sammanfatta(manader)

    assert resultat["varmast"] == 6
    assert resultat["kallast"] == 12
    assert resultat["blotast"] == 12


# Testar att API anropet hanterar http fel korrekt som den ska
def test_api_httpfel():
    with patch("application.api.requests.get") as mock_get:
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError
        mock_get.return_value = mock_response

        with pytest.raises(requests.exceptions.HTTPError):
            hamta_vader()


# Testar att api anrop funktionen ger ValueError när datan är tom.
def test_api_tomt_svar():
    with patch("application.api.requests.get") as mock_get:
        mock_response = Mock()
        mock_response.json.return_value = {"daily": {"time": []}}
        mock_get.return_value = mock_response

        with pytest.raises(ValueError):
            hamta_vader()


# Testar att dashboarden visar fel och ger statuskod 503 vid timeout.
def test_dashboard_timeout():
    with patch("application.app.hamta_vader", side_effect=requests.exceptions.Timeout):
        client = app.test_client()
        response = client.get("/dashboard")

    assert response.status_code == 503
    assert "Väderdata kunde inte hämtas" in response.get_data(as_text=True)
