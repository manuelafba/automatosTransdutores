
def verificar_cadeia(alfabeto_entrada, cadeia_entrada):
    """
    Função para verificar se a cadeia contém somente símbolos do alfabeto de entrada
    """
    for simbolo in cadeia_entrada:
        if simbolo not in alfabeto_entrada:
            print('A cadeia contém símbolos que não pertencem ao alfabeto de entrada.')
            return False # Caso tenha algum símbolo que não pertença ao alfabeto de entrada
    return True # Caso a verificação valide a cadeia 


def maquina_mealy(alfabeto_entrada, transicoes, transducoes, estado_inicial, cadeia_entrada):
    """
    Função que define a implementação de uma Máquina de Mealy em Python.  
    """
    cadeia_saida = ''
    estado_atual = estado_inicial
    # Verifica a validade da cadeia de entrada em relação ao pertencimento dos símbolos ao alfabeto de entrada
    if verificar_cadeia(alfabeto_entrada, cadeia_entrada):
        # Caso verdadeiro, a Máquina de Mealy irá realizar as transições e transduções
        for simbolo in cadeia_entrada:
            print('='*30)
            print(f'Estado atual:   \t{estado_atual}')
            print(f'Símbolo atual:  \t{simbolo}')
            print(f'Próximo estado: \t{transicoes[(estado_atual, simbolo)]}\n')
            
            # Atualiza a cadeia de saída com o resultado da função de transdução
            cadeia_saida += transducoes[(estado_atual, simbolo)]
            print(f'Cadeia de saída: \t{cadeia_saida}\n')
            
            # Atualiza o estado atual com o resultado da função de transição
            estado_atual = transicoes[(estado_atual, simbolo)]


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
