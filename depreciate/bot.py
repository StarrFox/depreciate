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

import discord
import pathlib
from discord.ext import commands
from box import ConfigBox
from typing import Union
from loguru import logger


class Depreciate(commands.Bot):
    def __init__(self, config: ConfigBox, **kwargs):
        super().__init__(
            command_prefix=kwargs.pop("command_prefix", config.general.prefix),
            case_insensitive=kwargs.pop("case_insensitive", True),
            max_messages=kwargs.pop("max_messages", 10_000),
            help_command=kwargs.pop("help_command", commands.MinimalHelpCommand()),
            allowed_mentions=kwargs.pop(
                "allowed_mentions",
                discord.AllowedMentions(everyone=False, roles=False, users=False),
            ),
            activity=discord.Activity(
                type=discord.ActivityType.listening,
                name=f"{config.general.prefix}help",
            ),
            **kwargs,
        )
        self.config: ConfigBox = config
        self.ready_once = False

    async def process_commands(self, message):
        if message.author.bot:
            return

        ctx = await self.get_context(message)  # cls=self.context)

        await self.invoke(ctx)

    async def on_message_edit(self, before, after):
        if before.content != after.content:
            await self.process_commands(after)

    async def on_ready(self):
        if self.ready_once:
            return

        self.ready_once = True

        self.load_extensions_from_dir("depreciate/commands")
        self.load_extensions_from_dir("depreciate/internals")

        logger.info(f"Bot ready with {len(self.extensions.keys())} extensions.")

    def load_extensions_from_dir(self, path: Union[str, pathlib.Path]) -> int:
        """
        Loads any python files in a directory and it's children
        as extensions

        :param path: Path to directory to load
        :return: Number of extensions loaded
        """
        if not isinstance(path, pathlib.Path):
            path = pathlib.Path(path)

        if not path.is_dir():
            return 0

        before = len(self.extensions.keys())

        extension_names = []

        for subpath in path.glob("**/[!_]*.py"):  # Ignore if starts with _

            parts = subpath.with_suffix("").parts
            if parts[0] == ".":
                parts = parts[1:]

            extension_names.append(".".join(parts))

        for ext in extension_names:
            try:
                self.load_extension(ext)
            except (commands.errors.ExtensionError, commands.errors.ExtensionFailed):
                logger.exception("Failed loading " + ext)

        return len(self.extensions.keys()) - before

    def run(self, *args, **kwargs):
        return super().run(self.config.discord.token, *args, **kwargs)

    # todo: Finish
    async def get_next_depreciation(self):
        pass
