import MetaTrader5 as mt5
from mtcli.conecta import conectar, shutdown
from mtcli.logger import setup_logger
from plugin_exemplo.conf import CHAVE

def calcular():
    return f"O comando esta {CHAVE}!"
