from gmail import GMail, Message
import random

gmail = GMail('notthumann96@gmail.com','minhngoc1996')
html_template = '''
<p><span style="text-decoration: underline;">Hello</span></p>
<p><span style="text-decoration: underline;">I am not Human</span></p>
<p><span style="text-decoration: underline;">Whatever<strong> {{ Whatever }}</strong></span></p>
'''
we = {'nah':'he he he','bah':'ha ha ha', 'hal':'hi hi hi'}

html_content = html_template.replace('{{ Whatever }}',random.choice(list(we.items())))
msg = Message('Hello',to='notthumann96@gmail.com',html=html_content)
gmail.send(msg)