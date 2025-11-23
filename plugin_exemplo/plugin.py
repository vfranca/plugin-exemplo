from plugin_exemplo.cli import exemplo


def register(cli):
    cli.add_command(exemplo, name="exemplo")
