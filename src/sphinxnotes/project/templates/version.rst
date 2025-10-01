
{% if date -%}
:Date: :ref:`📅{{ date }} <any-version.date+by-year>`
:Download: :tag:`{{ title }}`
{%- endif %}

{% if not date -%}
.. note:: This version is still under development and has not been released yet.
{%- endif%}

{% for line in content %}
{{ line }}
{% endfor %}

