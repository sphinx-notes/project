"""
sphinxnotes.project.sphinxnotes_any
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Useful sphinxnotes-any config for project management.

See also https://sphinx.silverrainz.me/any/.

:copyright: Copyright 2025 Shengyu Zhang
:license: BSD, see LICENSE for details.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
from os import path

from sphinx.config import ENUM
from sphinx.errors import ConfigError

if TYPE_CHECKING:
    from sphinx.application import Sphinx
    from sphinx.config import Config


def _get_template_file(name: str) -> str:
    """
    Get file path of template file.

    .. seealso::

       see ``[tool.setuptools.package-data]`` section of pyproject.toml to know
       how files are included.
    """
    prefix = path.abspath(path.dirname(__file__))
    # TODO: Various parser (md, rst, and ect..) support.
    return path.join(prefix, 'templates', name + '.rst')


def _read_template_file(name: str) -> str:
    return open(_get_template_file(name), 'r').read()


def _validate_project_example_style(style: str) -> str:
    if style not in {'tab', 'grid'}:
        raise ConfigError(
            'The "project_example_style" config value must be "tab" or "grid".'
        )
    return style


ANY_OBJECT_TYPES = {
    'version': {
        'schema': {
            'attrs': {
                'date': 'date, ref, index by year',
                'break': 'flag',
            },
        },
        'templates': {
            'obj': _read_template_file('version'),
            'header': '🏷️ {{ name }}',
            'ref': '🏷️ ``{{ name }}``',
        },
    },
    'example': {
        'schema': {
            'name': 'str, ref',
            'attrs': {
                'style': 'str',
            },
        },
        'templates': {
            'obj': _read_template_file('example'),
        },
    },
}


def _config_inited(app: Sphinx, config: Config) -> None:
    config.project_example_style = _validate_project_example_style(
        config.project_example_style
    )

    if v := config.any_object_types:
        v.update(ANY_OBJECT_TYPES)
    else:
        # Prevent modifying the default value.
        config.any_object_types = ANY_OBJECT_TYPES


def setup(app: Sphinx):
    app.setup_extension('sphinxnotes.any')
    app.add_config_value(
        'project_example_style',
        'grid',
        'env',
        types=ENUM('tab', 'grid'),
    )
    # Should have priority over sphinxnotes.any's "config-inited" callback.
    app.connect('config-inited', _config_inited, priority=400)
