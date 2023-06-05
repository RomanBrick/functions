# from mylib.bot import scrape
# import click


# @click.command()
# @click.option("--name", help="Web page we want to scrape")
# def cli(name="Microsoft", lenght=1):
#     result = scrape(name)
#     click.echo(click.style(f"{result}:",bg="blue", fg="white", bold=True))

# if __name__ == "__main__":
#     cli()

import click
from mylib.bot import scrape


@click.command()
@click.option("--name", help="Web page we want to scrape")
def cli(name):
    result = scrape(name)
    click.echo(click.style(f"{result}:", fg="blue"))


if __name__ == "__main__":
    cli()
