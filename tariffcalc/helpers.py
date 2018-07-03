import click
from flask.cli import with_appcontext


# TODO: добавить регистрацию в приложении 


@click.command('help-me')
@with_appcontext
def help_me():
    click.echo('''
    Дружище, всё будет хорошо.
    ''')

def init_app(app):
    app.cli.add_command(help_me)