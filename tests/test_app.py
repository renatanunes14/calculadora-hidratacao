import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.app import adicionar_consumo, total_consumido

def test_adicionar_consumo():
    adicionar_consumo(500)
    assert total_consumido() >= 500

def test_valor_invalido():
    try:
        adicionar_consumo(-100)
        assert False
    except ValueError:
        assert True