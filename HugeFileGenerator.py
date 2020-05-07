from mako.template import Template
from mako.runtime import Context 

tpl_xml = '''
<data>
<employeedatas>
<employeedata>
% for i in data:
<employee>
<id>${i}</id>
<name1>name1</name1>
<name2>name2</name2>
<name3>name3</name3>
<name4>name4</name4>
<name5>name5</name5>
<name6>name6</name6>
<name7>name7</name7>
<name8>name8</name8>
<name9>name9</name9>
<name10>name10</name10>
<name11>name11</name11>
<name12>name12</name12>
<name13>name13</name13>
<name14>name14</name14>
<name15>name15</name15>
</employee>
% endfor
</employeedata>
</employeedatas>
</data>
'''

tpl = Template(tpl_xml)

with open('output300.xml', 'w') as f:
    ctx = Context(f, data=range(300))
    tpl.render_context(ctx)