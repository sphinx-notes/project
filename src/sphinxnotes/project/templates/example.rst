{% if not style or style == 'tab' %}
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
.. grid:: 1 1 2 2
   :gutter: 1
   :margin: 0
   :padding: 0

   .. grid-item-card:: Source
      :margin: 0

      .. code:: rst

         {% for line in content.split('\n') -%}
         {{ line }}
         {% endfor %}

   .. grid-item-card:: Result
      :margin: 0

      {% for line in content.split('\n') -%}
      {{ line }}
      {% endfor %}
{% endif %}
