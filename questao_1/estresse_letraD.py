from  automato_questao_1 import AutomatoQ1d

# Lista contendo as cadeias para teste da expressão regular da máscara de validação de nome
cadeias_teste = [
    "aaabbba",          # Válido
    "baccc",            # Válido 
    "aaaaccc",          # Válido
    "aaabbbbacccc",     # Válido
    "a",                # Válido
    "",                 # Inválido pois a sequência deve conter ao menos um a
    "aaabbb",           # Inválido pois a cadeia pode começar com a*b*, mas vew terminar com ac*
    "c",                # Inválido, a cadeia deve conter ao menos um 'a'
    "aabbbbccc",        # Invalido pois a cadeia deve terminar com ac**, nesse caso termina com c*
    "aabbaac",          # Inválido pois a cadeia deve terminar com ac* e não a+c*
]

automato = AutomatoQ1d()
# Laço para iterar sobre a lista de cadeias e mostrar quais são válidas ou não
for cadeia in cadeias_teste:
    print(f'Cadeia: {cadeia.ljust(30)} - Válido: {automato.processar_cadeia(cadeia)}')
print()
