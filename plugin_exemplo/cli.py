"""
Interface CLI do plugin exemplo

Comando:
    mt exemplo
"""

import click
from mtcli.domain.timeframe import Timeframe
from .conf import (
    SYMBOL,
    TIMEFRAME,
    BARS,
)

@click.command("exemplo")
@click.version_option(package_name="plugin-exemplo")
@click.option("-s", "--symbol", default=SYMBOL, show_default=True, help="Ativo.")
@click.option("-t", "--timeframe", default=TIMEFRAME, show_default=True, help="Timeframe base.")
@click.option("-b", "--bars", default=BARS, show_default=True, help="Quantidade de candles base.")
def exemplo(symbol, timeframe, bars):
    """
    Exibe o comando exemplo no terminal.

    Exemplo:

        mt exemplo --symbol WIN$N --timeframe m5 --bars 20
    """
    try:
        tf_enum = Timeframe.from_string(timeframe)
    except ValueError as e:
        raise click.BadParameter(str(e))

    click.echo(f"ativo {symbol} timeframe {timeframe} bars {bars}")
