from unittest.mock import Mock, patch
import requests
from application.api import hamta_vader
import pytest

def test_api_timeout():
    with patch("application.api.requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.Timeout

        with pytest.raises(requests.exceptions.Timeout):
            hamta_vader()