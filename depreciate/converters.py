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

from datetime import datetime

from discord.ext import commands
from parsedatetime import Calendar
from pytz import timezone


class GuildChannelConverter(commands.Converter):
    async def convert(self, ctx: commands.Context, argument: str):
        try:
            channel = await commands.TextChannelConverter().convert(ctx, argument)
        except commands.BadArgument:
            try:
                channel = await commands.VoiceChannelConverter().convert(ctx, argument)
            except commands.BadArgument:
                try:
                    channel = await commands.CategoryChannelConverter().convert(
                        ctx, argument
                    )
                except commands.BadArgument:
                    channel = None

        if channel:
            return channel

        else:
            raise commands.BadArgument(f"{argument} was not a channel in this guild.")


class HumanTimeConverter(commands.Converter):
    async def convert(self, ctx: commands.Context, argument: str):
        cal = Calendar()
        utc = timezone("UTC")

        utcnow = datetime.utcnow().replace(microsecond=0, tzinfo=utc)
        parsed = cal.parseDT(argument, sourceTime=utcnow, tzinfo=utc)[0]

        if parsed == utcnow:
            raise commands.BadArgument(f'"{argument}" is not a valid time.')

        elif parsed < utcnow:
            raise commands.BadArgument(f'"{argument}" is in the past.')

        return parsed
