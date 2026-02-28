"""
Configuração do plugin plugin-exemplo.

Lê parâmetros do arquivo mtcli.ini na seção [exemplo].
"""

import configparser
import os


CONFIG_PATH = os.path.join(os.getcwd(), "mtcli.ini")

config = configparser.ConfigParser()
config.read(CONFIG_PATH)

SECTION = "exemplo"


def get_default_symbol() -> str:
    return config.get(SECTION, "symbol", fallback="WIN$N")


def get_default_timeframe() -> str:
    return config.get(SECTION, "timeframe", fallback="m5")


def get_default_bars() -> int:
    return config.getint(SECTION, "bars", fallback=500)
