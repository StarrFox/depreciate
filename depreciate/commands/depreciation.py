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

from typing import Optional

import discord
from discord.ext import commands
from discord.ext.commands.default import Author, CurrentChannel

from depreciate import GuildChannelConverter, HumanTimeConverter


class Depreciation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    @commands.command(name="channel")
    async def depreciate_channel(
        self,
        ctx: commands.Context,
        channel: Optional[GuildChannelConverter] = CurrentChannel,
        *,
        when: HumanTimeConverter,
    ):
        """Depreciate a channel"""
        await ctx.send(f"{channel=}, {when=}")

    @commands.has_permissions(manage_emojis=True)
    @commands.bot_has_permissions(manage_emojis=True)
    @commands.command(name="emoji")
    async def depreciate_emoji(
        self, ctx: commands.Context, emoji: discord.Emoji, *, when: HumanTimeConverter
    ):
        """Depreciate an emoji"""
        pass

    # Todo: allow if the message is theirs
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    @commands.command(name="message")
    async def depreciate_message(
        self,
        ctx: commands.Context,
        message: discord.Message,
        *,
        when: HumanTimeConverter,
    ):
        """Depreciate a message"""
        pass

    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    @commands.command(name="role")
    async def depreciate_role(
        self, ctx: commands.Context, role: discord.Role, *, when: HumanTimeConverter
    ):
        """Depreciate a role"""
        pass

    @commands.has_permissions(manage_nicknames=True)
    @commands.bot_has_permissions(manage_nicknames=True)
    @commands.command(name="nick", aliases=["nickname"])
    async def depreciate_nick(
        self, ctx: commands.Context, member: discord.Member, *, when: HumanTimeConverter
    ):
        """Depreciate a nickname"""
        pass

    @commands.command()
    async def when(self, ctx: commands.Context):
        """See when a channel, custom emoji, message or role depreciates"""
        pass


def setup(bot: commands.Bot):
    bot.add_cog(Depreciation(bot))
