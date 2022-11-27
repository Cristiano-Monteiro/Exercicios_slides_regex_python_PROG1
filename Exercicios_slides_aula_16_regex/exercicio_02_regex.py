"""
2) Faça uma função que recebe um string e retorna o string com os números de telefones transformados 
   para um único formato: (91) 91234 5678
"""
import re

def tratamento_string(string):
    lista_numeros = string.split(',')
    numero_novo_formato(lista_numeros)

def numero_novo_formato(lista_numeros):
    regex = re.compile(r'(\d{2})[ -]?(\d{5})[ -]?(\d{4})')
    for numero in lista_numeros:
        novo_formato = regex.search(numero)
        novo_numero = '({}) {} {}'.format(novo_formato.group(1), novo_formato.group(2), novo_formato.group(3))
        print(novo_numero)

numeros_telefone = """91912345678,
56782456857,
78386842756,
12345678901,
91-11223-4455,
11 55533-0101,
55 99498 9876
"""

tratamento_string(numeros_telefone)