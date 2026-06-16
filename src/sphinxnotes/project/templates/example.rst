{% macro render_source(content) %}
      .. code:: rst

         {% for line in content.split('\n') -%}
         {{ line }}
         {% endfor %}
{% endmacro %}

{% macro render_result(content) %}
      {% for line in content.split('\n') -%}
      {{ line }}
      {% endfor %}
{% endmacro %}

{% set _style = style or load_extra('env').config.project_example_style %}

{% if _style == 'tab' %}
.. tab-set::

   .. tab-item:: Result

      {{ render_result(content) }}

   .. tab-item:: Source

      {{ render_source(content) }}

{% elif _style in ['grid', 'split'] %}
.. grid:: 1 1 2 2
   :gutter: 1
   :margin: 0
   :padding: 0

   .. grid-item-card:: Source
      :margin: 0

      {{ render_source(content) }}

   .. grid-item-card:: Result
      :margin: 0

      {{ render_result(content) }}

{% endif %}
