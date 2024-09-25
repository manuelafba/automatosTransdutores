def verificar_cadeia(alfabeto_entrada, cadeia_entrada):
    for simbolo in cadeia_entrada:
        if simbolo not in alfabeto_entrada:
            print('A cadeia contém símbolos que não pertencem ao alfabeto de entrada.')
            return False
    return True

def maquina_mealy(alfabeto_entrada, transicoes, transducoes, estado_inicial, cadeia_entrada):
    """
    Função que define a implementação de uma Máquina de Mealy em Python.  
    """
    cadeia_saida = ''
    estado_atual = estado_inicial
    for simbolo in cadeia_entrada:
        if verificar_cadeia(alfabeto_entrada, cadeia_entrada):
            print('='*30)
            print(f'Estado atual:   \t{estado_atual}')
            print(f'Símbolo atual:  \t{simbolo}')
            print(f'Próximo estado: \t{transicoes[(estado_atual, simbolo)]}\n')

            cadeia_saida += transducoes[(estado_atual, simbolo)]
            print(f'Cadeia de saída: \t{cadeia_saida}\n')

            estado_atual = transicoes[(estado_atual, simbolo)]


estados = ['q0', 'q1', 'q2', 'q3', 'q4']

alfa_entrada = ['25', '50', '100']
alfa_saida = ['0', '1']

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

estado_inicial = 'q0'

estados_finais = ['q0', 'q1', 'q2', 'q3', 'q4']



moeda = 0
print('Moedas aceita -> 25 ou 50 ou 100')
entrada = []
while True:
    moeda = input('Insira uma moeda (0 para sair): ')
    if moeda == '0':
        break
    entrada.append(moeda)


maquina_mealy(alfa_entrada, funcao_transicao, funcao_transducao, estado_inicial, entrada)


testes = [
    ['50', '50', '100', '100', '50', '25', '25', '100', '25', '25', '100', '50', '25', '100', '50'],
    ['100', '50', '100', '25', '25', '100', '25', '50', '25', '100', '50', '25', '25', '100', '50'],
    ['25', '100', '25', '50', '100', '25', '50', '100', '25', '50', '100', '50', '25', '100', '50'],
    ['50', '25', '25', '50', '25', '100', '100', '100', '25', '50', '25', '50', '100', '25', '50'],
    ['100', '100', '25', '50', '50', '25', '25', '50', '25', '100', '100', '50', '25', '50', '100'],
    ['50', '50', '25', '100', '100', '100', '50', '25', '25', '50', '25', '100', '25', '50', '100'],
    ['100', '25', '50', '25', '50', '100', '25', '100', '50', '100', '25', '25', '50', '100', '25'],
    ['25', '50', '100', '100', '25', '50', '25', '100', '50', '25', '100', '25', '50', '100', '25'],
    ['50', '100', '100', '25', '50', '25', '100', '50', '25', '25', '100', '25', '50', '50', '100'],
    ['25', '50', '25', '100', '25', '100', '100', '50', '50', '100', '50', '25', '100', '25', '25'],
    ['100', '100', '50', '25', '50', '100', '25', '25', '50', '100', '25', '100', '25', '50', '50'],
    ['50', '100', '25', '50', '25', '100', '50', '25', '100', '25', '50', '100', '100', '50', '25'],
    ['100', '25', '50', '25', '25', '100', '50', '100', '25', '100', '50', '25', '50', '25', '100'],
    ['25', '50', '100', '100', '25', '50', '100', '25', '50', '25', '100', '25', '50', '50', '100'],
    ['100', '50', '100', '25', '25', '50', '100', '25', '50', '25', '50', '100', '25', '100', '25'],
]

contador = 1
for entrada in testes:
    print(f'Entrada {contador}\n')
    maquina_mealy(alfa_entrada, funcao_transicao, funcao_transducao, estado_inicial, entrada)
    contador += 1
    print('x='*30)




























