class AutomatoQ1a:

    def __init__(self):

        self.estados = {0,1,2}
        self.alfabeto = {'a','b','c'}
        self.transiçoes = {
            (0, 'a'): 1,
            (1, 'a'): 0,
            (1, 'b'): 1,
            (1, 'c'): 2,
            (2, 'a'): 1,
            (2, 'c'): 2,
        }

        self.estado_inicial = 0
        self.estados_finais = {0,1,2}

    def processar_cadeia(self, cadeia):
        estado_atual = self.estado_inicial

        cont =0
        while(cont<= (len(cadeia) -1) ):
            if((estado_atual, cadeia[cont]) in self.transiçoes):
                estado_atual = self.transiçoes[(estado_atual, cadeia[cont])]
                cont+=1
                

            else:
                return False

        return estado_atual in self.estados_finais


automato1 = AutomatoQ1a()
print(automato1.processar_cadeia("abaacabbbccabcacaaabbbccabacacabcb"))


class AutomatoQ1b:

    def __init__(self):

        self.estados = {0,1,2,3,4,5,6,7}
        self.alfabeto = {'a','b','c'}
        self.transiçoes = {
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

        
        self.estado_inicial = 0
        self.estados_finais = {3,7}

    def processar_cadeia(self, cadeia):
        estado_atual = self.estado_inicial
        

        cont =0
        while(cont<= (len(cadeia) -1) ):
            if((estado_atual, cadeia[cont]) in self.transiçoes):
                estado_atual = self.transiçoes[(estado_atual, cadeia[cont])]
                cont+=1
                

            else:
                return False

        return estado_atual in self.estados_finais


automato2 = AutomatoQ1b()
print(automato2.processar_cadeia("bcbcbcbcbbbbbccccbcbcbbccbaaaa"))



class AutomatoQ1c:

    def __init__(self):

        self.estados = {0,1,2,3}
        self.alfabeto = {'a','b'}
        self.transiçoes = {
            (0, 'a'): 1,
            (0, 'b'): 3,

            (1, 'a'): 1,
            (1, 'b'): 2,

            (3, 'b'): 3,
            (3, 'a'): 2,
            
        }

        
        self.estado_inicial = 0
        self.estados_finais = {2}

    def processar_cadeia(self, cadeia):
        estado_atual = self.estado_inicial
        

        cont =0
        while(cont<= (len(cadeia) -1) ):
            if((estado_atual, cadeia[cont]) in self.transiçoes):
                estado_atual = self.transiçoes[(estado_atual, cadeia[cont])]
                cont+=1
                

            else:
                return False

        return estado_atual in self.estados_finais


automato3 = AutomatoQ1c()
print(automato3.processar_cadeia("ab"))



class AutomatoQ1d:

    def __init__(self):

        self.estados = {0,1,2,3}
        self.alfabeto = {'a','b','c'}
        self.transiçoes = {
            (0, 'a'): 1,
    
            (1, 'a'): 1,
            (1, 'b'): 2,
            (1, 'c'): 3,

            (2, 'b'): 2,
            (2, 'a'): 3,

            (3, 'c'): 3,
            
            
        }

        
        self.estado_inicial = 0
        self.estados_finais = {1,3}

    def processar_cadeia(self, cadeia):
        estado_atual = self.estado_inicial
        

        cont =0
        while(cont<= (len(cadeia) -1) ):
            if((estado_atual, cadeia[cont]) in self.transiçoes):
                estado_atual = self.transiçoes[(estado_atual, cadeia[cont])]
                cont+=1
                

            else:
                return False

        return estado_atual in self.estados_finais


automato4 = AutomatoQ1d()
print(automato4.processar_cadeia("aaaaabbbbaa"))
