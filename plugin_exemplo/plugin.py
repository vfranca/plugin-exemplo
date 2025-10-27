from plugin_exemplo.comando import comando


def register(cli):
    cli.add_command(comando, name="comando")
