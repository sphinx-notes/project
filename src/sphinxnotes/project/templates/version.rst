{% if date -%}
:Date: :version.date+by-year:`📅{{ date }} <{{ date }}>`
:Download: :tag:`{{ name }}`
{% else -%}
.. note:: This version is still under development and has not been released yet.
{%- endif%}

{% if break -%}
.. warning:: **This version contains INCOMPATIBLE changes.**
{%- endif%}

{% for line in content.split('\n') -%}
{{ line }}
{% endfor %}
