{% set opt = load_extra('env').config.values[name] %}
{% set default = opt.default | string %}

.. role:: py(code)
   :language: Python

.. confval:: {{ name }}
   :type: {{ opt.valid_types | autoconfval_types | join(', ') }}
   {% if '\n' not in default %}:default: :py:`{{ opt.default | pprint }}`{% endif %}

   ..

   {% if '\n' in default %}
   :default:
      .. code-block::

         {% for _line in default.split('\n') -%}
         {{ _line }}
         {% endfor %}
   {% endif %}

   {%- for line in opt.description.split('\n') %}
   {{ line }}
   {% endfor %}

   {% for line in (content or '').split('\n') -%}
   {{ line }}
   {% endfor %}
