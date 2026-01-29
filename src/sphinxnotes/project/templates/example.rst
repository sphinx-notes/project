{% if style is not defined or style == 'tab' %}
.. tab-set::

   .. tab-item:: Result

      {% for line in content.split('\n') -%}
      {{ line }}
      {% endfor %}

   .. tab-item:: Source

      .. code:: rst

         {% for line in content.split('\n') -%}
         {{ line }}
         {% endfor %}
{% elif style == 'grid'  %}
.. grid:: 2
   :gutter: 1

   .. grid-item-card:: Source

      .. code:: rst

         {% for line in content.split('\n') -%}
         {{ line }}
         {% endfor %}

   .. grid-item-card:: Result

      {% for line in content.split('\n') -%}
      {{ line }}
      {% endfor %}
{% endif %}
