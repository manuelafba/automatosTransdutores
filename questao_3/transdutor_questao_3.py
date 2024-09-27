
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
