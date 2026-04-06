"""
sphinxnotes.project.sphinxnotes_render_ext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Useful sphinxnotes-render.ext config for project management.

See also https://sphinx.silverrainz.me/render/.

:copyright: Copyright 2025 Shengyu Zhang
:license: BSD, see LICENSE for details.
"""
from __future__ import annotations
from typing import TYPE_CHECKING

from .sphinxnotes_any import _read_template_file

if TYPE_CHECKING:
    from sphinx.application import Sphinx
    from sphinx.config import Config

DATA_DEFINE_DIRECTIVES = {
    'autoconfval': {
        'schema': {
            'name': 'str',
        },
        'template': {
            'text': _read_template_file('autoconfval'),
            'extra': ['env'],
        },
    },
    'autoobj': {
        'schema': {
            'name': 'list of str, sep by ":"',
        },
        'template': {
            'text': _read_template_file('autoobj'),
            'extra': ['app'],
        },
    },
    'internal-only': {
        'schema': {
            'name': None,
            'attrs': {},
            'content': None,
        },
        'template': {
            'text': _read_template_file('internal-only'),
        },
    },
}

def _config_inited(app: Sphinx, config: Config) -> None:
    if v := config.render_ext_data_define_directives:
        v.update(DATA_DEFINE_DIRECTIVES)
    else:
        # Prevent modifying the default value.
        config.render_ext_data_define_directives = DATA_DEFINE_DIRECTIVES.copy()


def setup(app: Sphinx):
    app.setup_extension('sphinxnotes.render.ext')
    # Should have priority over sphinxnotes.render.ext's
    # "config-inited" callback.
    app.connect('config-inited', _config_inited, priority=400)
