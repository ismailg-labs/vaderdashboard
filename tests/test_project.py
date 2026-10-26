from unittest.mock import Mock, patch
import requests
from application.api import hamta_vader
from application.analysis import bearbeta_manader
import pytest

def test_api_timeout():
    with patch("application.api.requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.Timeout

        with pytest.raises(requests.exceptions.Timeout):
            hamta_vader()

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