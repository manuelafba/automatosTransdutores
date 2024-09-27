from  automato_questao_1 import AutomatoQ1a

# Lista contendo as cadeias para teste da expressão regular da máscara de validação de nome
cadeias_teste = [
    "a",                # Válido
    "",                 # Válido 
    "aaabbb",           # Válido
    "aaaccc",           # Válido
    "aaabbbcc",         # Válido
    "aaabcaabacabc",    # Válido   
    "aabcb",            # Inválido pois a sequência b*c* só pode repetir de um novo 'a' aparecer
    "aacabcaabcacb",    # Inválido pois a sequência b*c* só pode repetir de um novo 'a' aparecer
    "bbcc",             # Inválido a presença de 'a' antes de b*c* é obrigatório
    "b",                # Invalido a presença de 'a' antes de b*c* é obrigatório
    "c",                # Inválido a presença de 'a' antes de b*c* é obrigatório
]

automato = AutomatoQ1a()
# Laço para iterar sobre a lista de cadeias e mostrar quais são válidas ou não
for cadeia in cadeias_teste:
    print(f'Cadeia: {cadeia.ljust(20)} - Válido: {automato.processar_cadeia(cadeia)}')
print()
