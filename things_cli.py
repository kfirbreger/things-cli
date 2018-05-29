import click
import os




@click.group()
def cli():
    pass

@cli.command()
def show():
    command = 'show'
    params = {'id': 'upcoming'}
    params_str = '&'.join([f'{k}={v}' for k, v in params.items()])
    url = f"things:///{command}?{params_str}"
    print(url)

