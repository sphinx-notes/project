{% set opt = load_extra('env').config.values[name] %}

.. role:: py(code)
   :language: Python

.. confval:: {{ name }}
   :type: {{ opt.valid_types | autoconfval_types | join(', ') }}
   :default: :py:`{{ opt.default | pprint }}`

   {%- for line in opt.description.split('\n') %}
   {{ line }}
   {% endfor %}

   {% for line in (content or '').split('\n') -%}
   {{ line }}
   {% endfor %}
