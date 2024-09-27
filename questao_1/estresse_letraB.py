from questao_1.automato_questao_1 import AutomatoQ1b

# Lista contendo as cadeias para teste da expressão regular da máscara de validação de nome
cadeias_teste = [
    "aaa",       # Válido
    "aaabcbcbc",       # Válido 
    "aaab",       # Válido
    "ccbbcbcbcbaaa",       # Válido
    "baaa",       # Válido
 

    
    "aabcb",       # Inválido pois a sequência deve começar ou (exclusivo) terminar com aaa
    "aacabcaabcacb",       # Inválido pelo motivo de cima
    "bbcc",       # Inválido, a presença de 'aaa' antes ou (exclusivo) depois de (b|c)* é obrigatório
    "b",       # Invalido pelo motivo acima
    "c",          # Inválido pelo motivo acima
    
]

automato = AutomatoQ1b()
# Laço para iterar sobre a lista de cadeias e mostrar quais são válidas ou não
for cadeia in cadeias_teste:
    print(f'Cadeia: {cadeia} - Válido: {automato.processar_cadeia(cadeia)}')
print()