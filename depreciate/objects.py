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

from enum import Enum
from typing import Type, TypeVar, Union


T = TypeVar("T", bound="DepreciateObject")


class DepreciateType(Enum):
    """
    Note that this is the same order as conversion
    """

    channel = 0
    message = 1
    emoji = 2
    role = 3
    nick = 4


class DepreciateObject:
    def __init__(self):
        pass

    @classmethod
    def from_data(cls: Type[T], data: Union[dict, tuple]) -> T:
        if isinstance(data, dict):
            pass
