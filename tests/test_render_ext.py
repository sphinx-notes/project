"""Tests for sphinxnotes_render_ext."""

from sphinxnotes.project.sphinxnotes_render_ext import (
    _fmt_type,
    _format_autoconfval_types,
)
from sphinx.config import ENUM


class TestFmtType:
    def test_simple_type(self):
        assert _fmt_type(str) == 'str'
        assert _fmt_type(int) == 'int'
        assert _fmt_type(float) == 'float'
        assert _fmt_type(bool) == 'bool'

    def test_none_type(self):
        assert _fmt_type(type(None)) == 'None'

    def test_bare_generic(self):
        assert _fmt_type(list) == 'list'
        assert _fmt_type(dict) == 'dict'

    def test_generic_alias(self):
        assert _fmt_type(list[str]) == 'list[str]'
        assert _fmt_type(dict[str, int]) == 'dict[str, int]'
        assert _fmt_type(set[int]) == 'set[int]'

    def test_nested_generic(self):
        assert _fmt_type(dict[str, list[int]]) == 'dict[str, list[int]]'

    def test_union_type(self):
        assert _fmt_type(str | None) == 'str | None'
        assert _fmt_type(int | str) == 'int | str'


class TestFormatAutoconfvalTypes:
    def test_enum(self):
        result = _format_autoconfval_types(ENUM('tab', 'grid'))
        assert result == [":py:`'grid'`", ":py:`'tab'`"]

    def test_enum_with_none(self):
        result = _format_autoconfval_types(ENUM(None, 'day', 'month', 'year'))
        assert result == [":py:`'day'`", ":py:`'month'`", ":py:`'year'`", ':py:`None`']

    def test_simple_types(self):
        result = _format_autoconfval_types(frozenset({str, int}))
        assert set(result) == {':py:`str`', ':py:`int`'}

    def test_generic_alias(self):
        result = _format_autoconfval_types(frozenset({list[str]}))
        assert result == [':py:`list[str]`']

    def test_mixed_types(self):
        result = _format_autoconfval_types(frozenset({list[str], str}))
        assert set(result) == {':py:`list[str]`', ':py:`str`'}
