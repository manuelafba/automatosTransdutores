from  automato_questao_1 import AutomatoQ1b

# Lista contendo as cadeias para teste da expressão regular da máscara de validação de nome
cadeias_teste = [
    "aaa",              # Válido
    "aaabcbcbc",        # Válido 
    "aaab",             # Válido
    "ccbbcbcbcbaaa",    # Válido
    "baaa",             # Válido
    "aabcb",            # Inválido pois a sequência deve começar ou (exclusivo) terminar com aaa
    "aacabcaabcacb",    # Inválido pois a sequência deve começar ou (exclusivo) terminar com aaa
    "bbcc",             # Inválido a presença de 'aaa' antes ou (exclusivo) depois de (b|c)* é obrigatório
    "b",                # Invalido a presença de 'aaa' antes ou (exclusivo) depois de (b|c)* é obrigatório
    "c",                # Inválido a presença de 'aaa' antes ou (exclusivo) depois de (b|c)* é obrigatório
]

automato = AutomatoQ1b()
# Laço para iterar sobre a lista de cadeias e mostrar quais são válidas ou não
for cadeia in cadeias_teste:
    print(f'Cadeia: {cadeia.ljust(30)} - Válido: {automato.processar_cadeia(cadeia)}')
print()
