"""
Interface CLI do plugin exemplo

Comando:
    mt exemplo
"""

import click
from mtcli.logger import setup_logger
from .conf import (
    get_default_symbol,
    get_default_timeframe,
    get_default_bars,
)

log = setup_logger()


@click.command("exemplo")
@click.version_option(package_name="plugin-exemplo")
@click.option("-s", "--symbol", default=get_default_symbol(), show_default=True, help="Ativo.")
@click.option("-t", "--timeframe", default=get_default_timeframe(), show_default=True, help="Timeframe base.")
@click.option("-b", "--bars", default=get_default_bars(), show_default=True, help="Quantidade de candles base.")
def exemplo(symbol, timeframe, bars):
    """
    Exibe o comando exemplo no terminal.

    Exemplo:

        mt exemplo --symbol WIN$N --timeframe m5 --bars 20
    """
    click.echo(f"ativo {symbol} timeframe {timeframe} bars {bars}")
