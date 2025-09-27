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

from sphinxnotes.any.api import Schema, Field as F, by_year

from . import meta

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


def _config_inited(app: Sphinx, config: Config) -> None:
    version_schema = Schema(
        'version',
        name=F(uniq=True, ref=True, required=True, form=F.Forms.LINES),
        attrs={
            'date': F(ref=True, indexers=[by_year]),
        },
        content=F(form=F.Forms.LINES),
        description_template=_read_template_file('version'),
        reference_template='🏷️{{ title }}',
        missing_reference_template='🏷️{{ title }}',
        ambiguous_reference_template='🏷️{{ title }}',
    )
    confval_schema = Schema(
        'confval',
        name=F(uniq=True, ref=True, required=True, form=F.Forms.LINES),
        attrs={
            'type': F(),
            'default': F(),
            'choice': F(form=F.Forms.WORDS),
            'versionadded': F(),
            'versionchanged': F(form=F.Forms.LINES),
        },
        content=F(),
        description_template=_read_template_file('confval'),
        reference_template='⚙️{{ title }}',
        missing_reference_template='⚙️{{ title }}',
        ambiguous_reference_template='⚙️{{ title }}',
    )
    example_schema = Schema(
        'example',
        name=F(ref=True),
        attrs={'style': F()},
        content=F(form=F.Forms.LINES),
        description_template=_read_template_file('example'),
        reference_template='📝{{ title }}',
        missing_reference_template='📝{{ title }}',
        ambiguous_reference_template='📝{{ title }}',
    )

    config.any_schemas.extend(
        [
            version_schema,
            confval_schema,
            example_schema,
        ]
    )


def setup(app: Sphinx):
    meta.pre_setup(app)

    app.setup_extension('sphinxnotes.any')
    # Should have priority over sphinxnotes.any's "config-inited" callback.
    app.connect('config-inited', _config_inited, priority=400)

    return meta.post_setup(app)
