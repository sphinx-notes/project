"""
sphinxnotes.project
~~~~~~~~~~~~~~~~~~~

Sphinx extension entrypoint.

:copyright: Copyright 2025 Shengyu Zhang
:license: BSD, see LICENSE for details.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
from importlib.metadata import version
from os import path

from sphinx.util import logging

if TYPE_CHECKING:
    from sphinx.application import Sphinx


logger = logging.getLogger(__name__)


def setup(app: Sphinx):
    from . import schemas

    schemas.setup(app)
