
:Date: :version.date+by-year:`📅{{ date }} <{{ date }}>`
:Download: :tag:`{{ name }}`

{% if not date -%}
.. note:: This version is still under development and has not been released yet.
{%- endif%}

{% for line in content.split('\n') -%}
{{ line }}
{% endfor %}
