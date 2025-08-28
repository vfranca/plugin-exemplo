import click
from . import conf
from mtcli.conecta import conectar, shutdown
from mtcli.logger import setup_logger


logger = setup_logger("plugin")


@click.command()
@click.version_option(package_name="plugin-exemplo")
def plugin():
    "Aqui vai uma ajuda do plugin." ""
    click.echo("plugin exemplo funcionando!")


if __name__ == "__main__":
    plugin()
