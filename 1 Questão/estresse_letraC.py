from AutomatosQ1 import AutomatoQ1c

# Lista contendo as cadeias para teste da expressão regular da máscara de validação de nome
cadeias_teste = [
    "aaab",       # Válido
    "abbb",       # Válido 
    "ab",       # Válido
    "abbbb",       # Válido
    "aaaaab",       # Válido
 

    
    "",       # Inválido pois a sequência deve começar com a ou b e ser seguido pelo 0 ou mais repetições do simbolo faltante
    "aaabb",       # Inválido pois a cadeia deve ser ab, onde um dos simbolos pode se repetir, mas o outro não
    "baaab",       # Inválido, a cadeia deve começar com ao menos um 'a'
    "aaaabbbaa",       # Invalido pois a cadeia deve ser o formato ab, pois se começar com mais de 1 'a', deve haver 0 ou 1 'b'
    "abbbba",          # Inválido pois não pode ocorrer novos 'a' depois de 'b'
    
]

automato = AutomatoQ1c()
# Laço para iterar sobre a lista de cadeias e mostrar quais são válidas ou não
for cadeia in cadeias_teste:
    print(f'Cadeia: {cadeia} - Válido: {automato.processar_cadeia(cadeia)}')
print()