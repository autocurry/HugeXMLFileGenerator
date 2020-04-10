from mako.template import Template
from mako.runtime import Context 

tpl_xml = '''
<data>
<employeedatas>
<employeedata>
% for i in data:
<employee>
<id>${i}</id>
<name>name</name>
</employee>
% endfor
</employeedata>
</employeedatas>
</data>
'''

tpl = Template(tpl_xml)

with open('outputlarge.xml', 'w') as f:
    ctx = Context(f, data=range(10000000))
    tpl.render_context(ctx)