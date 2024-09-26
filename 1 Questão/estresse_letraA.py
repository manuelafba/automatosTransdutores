from AutomatosQ1 import AutomatoQ1a

# Lista contendo as cadeias para teste da expressão regular da máscara de validação de nome
cadeias_teste = [
    "a",       # Válido
    "",       # Válido 
    "aaabbb",       # Válido
    "aaaccc",       # Válido
    "aaabbbcc",       # Válido
    "aaabcaabacabc",       # Válido 

    
    "aabcb",       # Inválido pois a sequência b*c* só pode repetir de um novo 'a' aparecer
    "aacabcaabcacb",       # Inválido pelo motivo de cima
    "bbcc",       # Inválido, a presença de 'a' antes de b*c* é obrigatório
    "b",       # Invalido pelo motivo acima
    "c",          # Inválido pelo motivo acima
    
]

automato = AutomatoQ1a()
# Laço para iterar sobre a lista de cadeias e mostrar quais são válidas ou não
for cadeia in cadeias_teste:
    print(f'Cadeia: {cadeia} - Válido: {automato.processar_cadeia(cadeia)}')
print()