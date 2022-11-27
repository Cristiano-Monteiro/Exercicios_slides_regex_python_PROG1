"""
1) Escreva uma RE para encontrar números de telefone do tipo:
(091)91234 5678
91 91234 5678
91-91234-5678
(91) 91234-5678
"""
import re

regex1 = re.compile(r'\(\d{3}\)\d{5} \d{4}')
padrao1 = regex1.search('(091)91234 5678')
print(padrao1)

regex2 = re.compile(r'\d{2} \d{5} \d{4}')
padrao2 = regex2.search('91 91234 5678')
print(padrao2)

regex3 = re.compile(r'\d{2}-\d{5}-\d{4}')
padrao3 = regex3.search('91-91234-5678')
print(padrao3)

regex4 = re.compile(r'\(\d{2}\) \d{5}-\d{4}')
padrao4 = regex4.search('(91) 91234-5678')
print(padrao4)