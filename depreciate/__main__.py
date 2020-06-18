#  depreciate, discord bot to remove items after time
#  Copyright (C) 2020  StarrFox
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

import asyncio

import click
from click_default_group import DefaultGroup
from pathlib import Path
from box import ConfigBox

import depreciate

ROOT_DIR = Path(__file__).parent


@click.group(
    invoke_without_command=True,
    cls=DefaultGroup,
    default="run",
    default_if_no_args=True,
)
@click.option("--version", "-v", is_flag=True)
def main(version):
    if version:
        click.echo(depreciate.__version__)


@main.command()
@click.option(
    "--config",
    default="config.toml",
    type=click.Path(exists=True),
    show_default=True,
    help="Path to config file.",
)
def run(config):
    config = ConfigBox.from_toml(filename=config)

    bot = depreciate.Depreciate(config)
    bot.load_extension("jishaku")

    bot.run()


@main.command(help='"Install" the bot; general setup before running.')
@click.option(
    "--config",
    default="config.toml",
    type=click.Path(),
    show_default=True,
    help="Path to config file.",
)
@click.option("--interactive", is_flag=True, help="Interactive config file setup.")
def install(config, interactive):
    config_file = Path(config)

    if config_file.exists():
        overwrite = click.confirm("Config file already exists, overwrite?")

    else:
        overwrite = True

        try:
            config_file.touch()

        except Exception as e:
            exit(str(e))

    if overwrite:
        if not interactive:
            with open(ROOT_DIR / "data" / "default_config.toml") as fp:
                default_config = fp.read()

            config_file.write_text(default_config.strip())

        else:
            res = interactive_install()
            config_file.write_text(res)

        click.echo("Config file made/overwriten.")

    with open(ROOT_DIR / "data" / "schema.sql") as fp:
        sql_init = fp.read()

    async def init_db():
        async with depreciate.db.get_database() as connection:
            await connection.executescript(sql_init.strip())
            await connection.commit()

        print("Initalized DB.")

    asyncio.run(init_db())


def interactive_install() -> str:
    interactive_config = ConfigBox.from_toml(
        filename=ROOT_DIR / "data" / "default_config.toml"
    )

    click.echo("Starting interactive config...")
    click.echo("--general section--")

    interactive_config.general.prefix = click.prompt("Command prefix?")

    click.echo("--discord section--")

    interactive_config.discord.token = click.prompt("Discord bot token?")

    return interactive_config.to_toml()


if __name__ == "__main__":
    main()
