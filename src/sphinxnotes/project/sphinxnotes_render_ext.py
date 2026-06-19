"""
sphinxnotes.project.sphinxnotes_render_ext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Useful sphinxnotes-render.ext config for project management.

See also https://sphinx.silverrainz.me/render/.

:copyright: Copyright 2025 Shengyu Zhang
:license: BSD, see LICENSE for details.
"""

from __future__ import annotations
from typing import TYPE_CHECKING, get_args, get_origin
import types as pytypes

from sphinx.config import ENUM
from sphinxnotes.render import filter

from .sphinxnotes_any import _read_template_file

if TYPE_CHECKING:
    from collections.abc import Iterable
    from sphinx.application import Sphinx
    from sphinx.config import Config


def _fmt_type(t) -> str:
    origin = get_origin(t)
    args = get_args(t)
    if origin is pytypes.UnionType:
        return ' | '.join(_fmt_type(a) for a in args)
    if t is type(None):
        return 'None'
    if origin is not None:
        args_str = ', '.join(_fmt_type(a) for a in args)
        return f'{_fmt_type(origin)}[{args_str}]'
    return t.__name__


def _format_autoconfval_types(valid_types) -> list[str]:
    if isinstance(valid_types, ENUM):
        reprs = [repr(c) for c in valid_types._candidates]  # pyright: ignore[reportPrivateUsage]
        return [f':py:`{r}`' for r in sorted(reprs)]
    return [f':py:`{_fmt_type(t)}`' for t in valid_types]


@filter('autoconfval_types')
def autoconfval_types(valid_types) -> Iterable[str]:
    return _format_autoconfval_types(valid_types)


DATA_DEFINE_DIRECTIVES = {
    'autoconfval': {
        'schema': {
            'name': 'str',
        },
        'template': {
            'text': _read_template_file('autoconfval'),
        },
    },
    'autoobj': {
        'schema': {
            'name': 'list of str, sep by ":"',
        },
        'template': {
            'text': _read_template_file('autoobj'),
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
