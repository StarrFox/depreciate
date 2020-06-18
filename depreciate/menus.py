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
from discord.ext import commands, menus


class ConfirmationMenu(menus.Menu):
    def __init__(
        self,
        to_confirm: str = None,
        *,
        owner_id: int = None,
        send_kwargs=None,
        **kwargs,
    ):
        super().__init__(**kwargs)

        if send_kwargs is None:
            send_kwargs = {}

        self.owner_id = owner_id
        self.send_kwargs = send_kwargs
        self.to_confirm = to_confirm
        self.response = None

    async def send_initial_message(
        self, ctx: commands.Context, channel: discord.TextChannel
    ):
        return await ctx.send(self.to_confirm or "\u200b", **self.send_kwargs)

    def reaction_check(self, payload):
        if payload.message_id != self.message.id:
            return False

        if self.owner_id is not None:
            if not payload.user_id == self.owner_id:
                return False

        else:
            if payload.user_id not in (self.bot.owner_id, self._author_id):
                return False

        return payload.emoji in self.buttons

    @menus.button("\N{WHITE HEAVY CHECK MARK}")
    async def do_yes(self, _):
        self.response = True
        self.stop()

    @menus.button("\N{CROSS MARK}")
    async def do_no(self, _):
        self.response = False
        self.stop()

    async def get_response(self, ctx: commands.Context):
        await self.start(ctx, wait=True)
        return self.response
