from transdutor_questao_3 import maquina_mealy

# Definição dos estados do transdutor
estados = ['q0', 'q1', 'q2', 'q3', 'q4']

# Definição alfabeto de entrada
alfa_entrada = ['25', '50', '100']

# Definição alfabeto de saída
alfa_saida = ['0', '1']

# Definição da função de transição no padrão: estado atual, símbolo -> próximo estado
funcao_transicao = {
    ('q0', '25'):'q1',
    ('q0', '50'):'q2',
    ('q0', '100'):'q4',
    ('q1', '25'):'q2',
    ('q1', '50'):'q3',
    ('q1', '100'):'q1',
    ('q2', '25'):'q3',
    ('q2', '50'):'q4',
    ('q2', '100'):'q2',
    ('q3', '25'):'q4',
    ('q3', '50'):'q1',
    ('q3', '100'):'q3',
    ('q4', '25'):'q1',
    ('q4', '50'):'q2',
    ('q4', '100'):'q4',
}

# Definição da função de transdução no padrão: estado atual, símbolo -> símbolo para a cadeia de saída
funcao_transducao = {
    ('q0', '25'):'0',
    ('q0', '50'):'0',
    ('q0', '100'):'1',
    ('q1', '25'):'0',
    ('q1', '50'):'0',
    ('q1', '100'):'1',
    ('q2', '25'):'0',
    ('q2', '50'):'1',
    ('q2', '100'):'1',
    ('q3', '25'):'1',
    ('q3', '50'):'1',
    ('q3', '100'):'1',
    ('q4', '25'):'0',
    ('q4', '50'):'0',
    ('q4', '100'):'1',
}

# Definição do estado inicial
estado_inicial = 'q0'

# Definição dos estados finais
estados_finais = ['q0', 'q1', 'q2', 'q3', 'q4']

# Testes arbitrários, basta descomentar o código abaixo para rodá-lo

# moeda = 0
# print('Moedas aceita -> 25 ou 50 ou 100')
# entrada = []
# while True:
#     moeda = input('Insira uma moeda (0 para sair): ')
#     if moeda == '0':
#         break
#     entrada.append(moeda)


# maquina_mealy(alfa_entrada, funcao_transicao, funcao_transducao, estado_inicial, entrada)

# Bateria de testes com cadeias válidas e inválidas
testes = [
    ['50', '50', '100', '100', '50', '25', '25', '100', '25', '25', '100', '50', '25', '100', '50'],    # Cadeia de saída: 011100110011010
    ['100', '50', '100', '25', '25', '100', '25', '50', '25', '100', '50', '25', '25', '100', '50'],    # Cadeia de saída: 101011001100110
    ['25', '100', '25', '50', '100', '25', '50', '100', '25', '50', '100', '50', '25', '100', '50'],    # Cadeia de saída: 010110011011010
    ['50', '25', '25', '50', '25', '100', '100', '100', '25', '50', '25', '50', '100', '25', '50'],     # Cadeia de saída: 001001111001101
    ['100', '100', '25', '50', '50', '25', '25', '50', '25', '100', '100', '50', '25', '50', '100'],    # Cadeia de saída: 110010010111001
    ['50', '50', '25', '100', '100', '100', '50', '25', '25', '50', '25', '100', '25', '50', '100'],    # Cadeia de saída: 010111010011001
    ['100', '25', '50', '25', '50', '100', '25', '100', '50', '100', '25', '25', '55', '100', '25'],    # Cadeia inválida, 55 não está no alfabeto
    ['100', '25', '50', '25', '25', '100', '5', '100', '25', '100', '50', '25', '50', '25', '100'],     # Cadeia inválida, 5 não está no alfabeto
    ['25', '50', '100', '100', '25', '50', '10', '25', '50', '25', '100', '25', '50', '50', '100'],     # Cadeia inválida, 10 não está no alfabeto
    ['100', '50', '100', '25', '25', '50', '100', '25', '50', '25', '75', '100', '25', '100', '25'],    # Cadeia inválida, 75 não está no alfabeto
]

# Laço para testar todas as cadeias acima
contador = 1
for entrada in testes:
    print(f'Entrada {contador}\n')
    maquina_mealy(alfa_entrada, funcao_transicao, funcao_transducao, estado_inicial, entrada)
    contador += 1
    print('x='*30)
