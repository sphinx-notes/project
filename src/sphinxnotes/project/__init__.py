"""
sphinxnotes.project
~~~~~~~~~~~~~~~~~~~

Common sphinx extension for sphinxnotes project.

:copyright: Copyright 2025 Shengyu Zhang
:license: BSD, see LICENSE for details.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sphinx.application import Sphinx

from . import meta


def setup(app: Sphinx):
    meta.pre_setup(app)

    from . import schemas

    schemas.setup(app)

    return meta.post_setup(app)
