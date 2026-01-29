"""
sphinxnotes.project.schemas
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Useful object schemas for project management.

See also https://sphinx.silverrainz.me/any/.

:copyright: Copyright 2025 Shengyu Zhang
:license: BSD, see LICENSE for details.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
from os import path

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


ANY_OBJECT_TYPES = {
    'version': {
        'schema': {
            'attrs': {
                'date': 'date, required, ref, index by year',
            },
        },
        'templates': {
            'obj': _read_template_file('version'),
            'header': '🏷️ {{ name }}',
            'ref': '🏷️ ``{{ name }}``',
        },
    },
    'autoconfval': {
        'schema': {
            'name': 'str',
        },
        'templates': {
            'obj': _read_template_file('autoconfval'),
            'header': None,
        },
    },
    'autoobj': {
        'schema': {
            'name': 'list of str, sep by ":", ref',
        },
        'templates': {
            'obj': _read_template_file('autoobj'),
            'header': 'The ``{{ name[1] }}`` object in "{{ name[0] }}" domain'
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
    }
}

def _config_inited(app: Sphinx, config: Config) -> None:
    config.any_object_types.update(ANY_OBJECT_TYPES)


def setup(app: Sphinx):
    app.setup_extension('sphinxnotes.any')
    # Should have priority over sphinxnotes.any's "config-inited" callback.
    app.connect('config-inited', _config_inited, priority=400)
