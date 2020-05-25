import click
import paramiko

from settings import \
    HOST, USER, PASSWORD, PORT, KEY_FILENAME, \
    SECRET_DIR


SSH_CLIENT = paramiko.SSHClient()

SSH_CLIENT.set_missing_host_key_policy(
    paramiko.AutoAddPolicy())

SSH_CLIENT.connect(
    hostname=HOST, username=USER,
    port=PORT, key_filename=KEY_FILENAME
)

SFTP = SSH_CLIENT.open_sftp()


@click.group()
def ssh_secret_cli():
    """CLI for SSH_Secret web-application"""
    pass


@ssh_secret_cli.group()
def secret():
    """Manage secrets"""
    pass


@secret.command()
@click.argument('filename')
def push(filename):
    """Send a secret to the remote server"""
    click.echo('Pushed secret')
    # todo доделать название файла
    SFTP.put(filename, SECRET_DIR + 'secret2')
    SSH_CLIENT.close()


@secret.command()
@click.argument('path')
def pull(path):
    """Fetch a secret from the remote server"""
    click.echo('Pulled secret')
    # todo доделать название файла
    SFTP.get(SECRET_DIR + 'secret2', path)
    SSH_CLIENT.close()


if __name__ == '__main__':
    ssh_secret_cli()
