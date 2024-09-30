# Classe AutomatoQ1a
class AutomatoQ1a:

    

    def __init__(self):
        # Define o conjunto de estados do autômato
        self.estados = {0, 1, 2, 3}
        
        # Define o alfabeto aceito pelo autômato
        self.alfabeto = {'a', 'b', 'c'}
        
        # Define as transições do autômato, onde a chave é (estado_atual, símbolo) e o valor é o próximo estado
        self.transicoes = {
            (0, 'a'): 1,  # Do estado 0, com 'a', vai para o estado 1

            (1, 'a'): 1,  # Do estado 1, com 'a', permanece no estado 1
            (1, 'b'): 2,  # Do estado 1, com 'b', vai para o estado 2
            (1, 'c'): 3,  # Do estado 1, com 'c', vai para o estado 3

            (2, 'a'): 1,  # Do estado 2, com 'a', vai para o estado 1
            (2, 'b'): 2,  # Do estado 2, com 'b', permanece no estado 2
            (2, 'c'): 3,  # Do estado 2, com 'c', vai para o estado 3

            (3, 'a'): 1,  # Do estado 1, com 'a', vai para o estado 1
            (3, 'c'): 3,  # Do estado 3, com 'c', permanece no estado 3
        }

        # Define o estado inicial do autômato
        self.estado_inicial = 0
        
        # Define o conjunto de estados finais
        self.estados_finais = {0, 1, 2,3}

        # O automato deve aceitar valida a linguagem (ab*c*)*

    # Função que processa uma cadeia de entrada
    def processar_cadeia(self, cadeia):
        estado_atual = self.estado_inicial  # Inicializa no estado inicial
        cont = 0  # Contador para iterar sobre a cadeia de entrada
        
        # Loop sobre os símbolos da cadeia
        while cont <= (len(cadeia) - 1):
            # Verifica se a transição existe para o estado atual e o símbolo corrente
            if (estado_atual, cadeia[cont]) in self.transicoes:
                # Atualiza o estado atual para o próximo estado
                estado_atual = self.transicoes[(estado_atual, cadeia[cont])]
                cont += 1  # Avança para o próximo símbolo
            else:
                # Se não houver transição, retorna False (cadeia não aceita)
                return False
        
        # Retorna True se o estado final for um dos estados de aceitação
        return estado_atual in self.estados_finais


# Cria uma instância do autômato e processa uma cadeia
automato1 = AutomatoQ1a()
# print(automato1.processar_cadeia("abaacabbbccabcacaaabbbccabacacabcb"))  # Exemplo de cadeia

# Classe AutomatoQ1b
class AutomatoQ1b:

    def __init__(self):
        # Define o conjunto de estados do autômato
        self.estados = {0, 1, 2, 3, 4, 5, 6, 7}
        
        # Define o alfabeto aceito pelo autômato
        self.alfabeto = {'a', 'b', 'c'}
        
        # Define as transições do autômato
        self.transicoes = {
            (0, 'a'): 1,
            (0, 'b'): 4,
            (0, 'c'): 4,
            (1, 'a'): 2,
            (2, 'a'): 3,
            (3, 'b'): 3,
            (3, 'c'): 3,
            (4, 'b'): 4,
            (4, 'c'): 4,
            (4, 'a'): 5,
            (5, 'a'): 6,
            (6, 'a'): 7,
        }

        # Define o estado inicial
        self.estado_inicial = 0
        
        # Define o conjunto de estados finais
        self.estados_finais = {3, 7}


        # A lingaugem aceita é aaa(b | c)* | (b | c)* aaa


    # Função que processa uma cadeia de entrada
    def processar_cadeia(self, cadeia):
        estado_atual = self.estado_inicial  # Estado inicial
        cont = 0  # Contador para iterar sobre a cadeia
        
        # Itera sobre a cadeia
        while cont <= (len(cadeia) - 1):
            # Verifica se a transição existe para o estado atual e símbolo corrente
            if (estado_atual, cadeia[cont]) in self.transicoes:
                # Atualiza o estado atual
                estado_atual = self.transicoes[(estado_atual, cadeia[cont])]
                cont += 1  # Próximo símbolo
            else:
                # Retorna False se não houver transição
                return False
        
        # Verifica se terminou em um estado final
        return estado_atual in self.estados_finais


# Instancia o automato e processa uma cadeia
automato2 = AutomatoQ1b()
# print(automato2.processar_cadeia("bcbcbcbcbbbbbccccbcbcbbccbaaaa"))  # Exemplo de cadeia

# Classe AutomatoQ1c
class AutomatoQ1c:

    def __init__(self):
        # Conjunto de estados do autômato
        self.estados = {0, 1, 2, 3, 4, 5}
        
        # Alfabeto aceito
        self.alfabeto = {'a', 'b'}
        
        # Transições
        self.transicoes = {
            (0, 'a'): 1,
            (0, 'b'): 5,

            (1, 'a'): 2,
            (1, 'b'): 4,

            (2, 'a'): 2,
            (2, 'b'): 3,

            (4, 'b'): 4,


            
        }

        # Estado inicial
        self.estado_inicial = 0
        
        # Estados finais
        self.estados_finais = {1,3,4}

        # A linguagem aceita é a*b | ab*

    # Função que processa a cadeia
    def processar_cadeia(self, cadeia):
        estado_atual = self.estado_inicial
        cont = 0
        
        # Iteração sobre a cadeia
        while cont <= (len(cadeia) - 1):
            # Verifica transição
            if (estado_atual, cadeia[cont]) in self.transicoes:
                estado_atual = self.transicoes[(estado_atual, cadeia[cont])]
                cont += 1
            else:
                return False
        
        # Verifica estado final
        return estado_atual in self.estados_finais


# Instancia o automato e processa uma cadeia
automato3 = AutomatoQ1c()
# print(automato3.processar_cadeia("ab"))  # Exemplo de cadeia

# Classe AutomatoQ1d
class AutomatoQ1d:

    def __init__(self):
        # Conjunto de estados
        self.estados = {0, 1, 2, 3, 4}
        
        # Alfabeto aceito
        self.alfabeto = {'a', 'b', 'c'}
        
        # Transições
        self.transicoes = {
            (0, 'a'): 1,
            (0, 'b'): 3,

            (1, 'a'): 1,
            (1, 'b'): 3,
            (1, 'c'): 2,

            (2, 'c'): 2,

            (3, 'a'): 2,
            (3, 'b'): 3,
            

            
        }

        # Estado inicial
        self.estado_inicial = 0
        
        # Estados finais
        self.estados_finais = {1, 2}

         # A linguagem aceita é a*b* (a | ac*)


    # Função que processa a cadeia
    def processar_cadeia(self, cadeia):
        estado_atual = self.estado_inicial
        cont = 0
        
        # Iteração sobre a cadeia
        while cont <= (len(cadeia) - 1):
            # Verifica transição
            if (estado_atual, cadeia[cont]) in self.transicoes:
                estado_atual = self.transicoes[(estado_atual, cadeia[cont])]
                cont += 1
            else:
                return False
        
        # Verifica se terminou em um estado final
        return estado_atual in self.estados_finais


# Instancia o automato e processa uma cadeia
automato4 = AutomatoQ1d()
# print(automato4.processar_cadeia("aaaaabbbbaa"))  # Exemplo de cadeia
