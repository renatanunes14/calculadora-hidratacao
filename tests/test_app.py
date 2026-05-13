import sys
import os
from unittest.mock import patch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.app import adicionar_consumo, total_consumido, obter_clima


def test_adicionar_consumo():
    adicionar_consumo(500)
    assert total_consumido() >= 500


def test_valor_invalido():
    try:
        adicionar_consumo(-100)
        assert False
    except ValueError:
        assert True


@patch("src.app.requests.get")
def test_obter_clima(mock_get):

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "current_condition": [
            {
                "temp_C": "30"
            }
        ]
    }

    temperatura = obter_clima("Sao Paulo")

    assert temperatura == "30"