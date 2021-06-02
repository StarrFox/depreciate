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

import re
import sys

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open("depreciate/__init__.py") as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
    ).group(1)

try:
    from semantic_release import setup_hook

    setup_hook(sys.argv)
except ImportError:
    setup_hook = None

setup(
    name="depreciate",
    version=version,
    description="A depreciation bot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="StarrFox",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    entry_points={"console_scripts": ["depreciate = depreciate.__main__:main"]},
    python_requires=">=3.8",
    install_requires=[
        "aiohttp==3.6.2",
        "aiosqlite==0.12.0",
        "async-timeout==3.0.1",
        "attrs==19.3.0",
        "braceexpand==0.1.5",
        "chardet==3.0.4",
        "click==7.1.2",
        "click-default-group==1.2.2",
        "colorama==0.4.3; sys_platform == 'win32'",
        "discord.py @ git+https://github.com/Rapptz/discord.py@refs/pull/1849/merge#egg=discord.py",
        "humanize==2.4.0",
        "idna==2.9",
        "import-expression==1.0.0",
        "jishaku==1.18.2.188",
        "loguru==0.4.1",
        "multidict==4.7.5",
        "parsedatetime==2.5",
        "pathlib==1.0.1",
        "python-box==4.2.3",
        "ruamel.yaml==0.16.10",
        "ruamel.yaml.clib==0.2.0; platform_python_implementation == 'CPython' and python_version < '3.9'",
        "toml==0.10.0",
        "websockets==8.1",
        "win32-setctime==1.0.1; sys_platform == 'win32'",
        "yarl==1.4.2",
    ],
    extras_require={
        "dev": [
            "appdirs==1.4.3",
            "attrs==19.3.0",
            "black==19.10b0",
            "bleach==3.1.4",
            "cached-property==1.5.1",
            "cerberus==1.3.2",
            "certifi==2020.4.5.1",
            "chardet==3.0.4",
            "click==7.1.2",
            "click-log==0.3.2",
            "colorama==0.4.3; sys_platform == 'win32'",
            "distlib==0.3.0",
            "docutils==0.16",
            "gitdb==4.0.4",
            "gitpython==3.1.1",
            "idna==2.9",
            "invoke==1.4.1",
            "keyring==21.2.0",
            "orderedmultidict==1.0.1",
            "packaging==19.2",
            "pathspec==0.8.0",
            "pep517==0.8.2",
            "pip-shims==0.5.2",
            "pipenv-setup @ git+https://github.com/Madoshakalaka/pipenv-setup"
            "pipfile==0.0.2",
            "pkginfo==1.5.0.1",
            "plette[validation]==0.2.3",
            "pygments==2.6.1",
            "pyparsing==2.4.7",
            "python-dateutil==2.8.1",
            "python-gitlab==1.15.0",
            "python-semantic-release==6.1.0",
            "pywin32-ctypes==0.2.0; sys_platform == 'win32'",
            "readme-renderer==26.0",
            "regex==2020.4.4",
            "requests==2.23.0",
            "requests-toolbelt==0.9.1",
            "requirementslib==1.5.7",
            "semver==2.9.1",
            "six==1.14.0",
            "smmap==3.0.2",
            "toml==0.10.0",
            "tomlkit==0.6.0",
            "tqdm==4.45.0",
            "twine==3.1.1",
            "typed-ast==1.4.1",
            "typing==3.7.4.1",
            "urllib3==1.26.5",
            "vistir==0.5.0",
            "webencodings==0.5.1",
            "wheel==0.34.2",
        ]
    },
)
