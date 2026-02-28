"""
Registro do plugin plugin-exemplo no mtcli principal.
"""

from .cli import exemplo


def register(cli):
    """
    Registra o comando 'exemplo' no mtcli principal.
    """
    cli.add_command(exemplo, name="exemplo")
    cli.add_command(exemplo, name="ex")
