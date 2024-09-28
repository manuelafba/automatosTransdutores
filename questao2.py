def automatoFinito(texto):
    """
    Função que simula um autômato finito determinístico (AFD) que reconhece a palavra "computador" 
    em um texto e retorna as posições onde ocorrem os casamentos exatos.

    O autômato percorre o texto caractere por caractere e, ao identificar a palavra 
    "computador", salva a posição inicial dessa ocorrência.

    Parâmetros:
    texto (str): O texto em que será procurada a palavra "computador".

    Retorno:
    list: Uma lista de inteiros contendo as posições no texto onde
    a palavra "computador" foi encontrada.
    """

    # Definição dos estados e das funções de transição
    funcoesTransicao = {
        ('q0', 'c'): 'q1', # Se no estado "q0" for lido a letra "c", a transição será para o estado "q1"
        ('q1', 'o'): 'q2',
        ('q2', 'm'): 'q3',
        ('q3', 'p'): 'q4',
        ('q4', 'u'): 'q5',
        ('q5', 't'): 'q6',
        ('q6', 'a'): 'q7',
        ('q7', 'd'): 'q8',
        ('q8', 'o'): 'q9',
        ('q9', 'r'): 'q10', # Se no estado "q9" for lido a letra "r", a transição será para o estado final "q10"
    }

    estadoInicial = 'q0'
    estadoFinal = 'q10'
    ocorrencias = []  # Lista vazia para armazenar as posições onde "computador" ocorre

    comprimentoTexto = len(texto)  # Determina o comprimento do texto 
    for i in range(comprimentoTexto):  # Laço para percorrer cada posição do texto, sendo "i" uma variável de controle que representa a posição
        estadoAtual = estadoInicial  # Define o estado atual como o estado inicial do autômato para reinicializá-lo a cada nova posição
        j = i  # Variável que percorre os caracteres do texto a partir da posição "i"
        
        while j < comprimentoTexto and (estadoAtual, texto[j]) in funcoesTransicao:  # Laço que continuará enquanto não chegar o fim do texto (j < comprimentoTexto) e houver uma transição válida
            estadoAtual = funcoesTransicao[(estadoAtual, texto[j])]  # Transição do estado atual para o próximo estado com base no caractere lido
            j += 1  # Incremento da ariável "j" para avançar para o próximo caractere

        if estadoAtual == estadoFinal: # Condicional para verificar se o autômato chegou ao estado final
            if (i == 0 or texto[i - 1] == ' ') and (j == comprimentoTexto or texto[j] == ' '): # Verifica se o caractere anterior é um espaço vazio e se o caractere após a palavra é um espaço ou o fim do texto
                ocorrencias.append(i)  # Adiciona a posição inicial da ocorrência para a lsita de posições

    return ocorrencias  # Retorna as posições encontradas

# Texto a ser analisado
texto = "O computador é uma máquina capaz de variados tipos de tratamento automático de informações ou processamento de dados. Entende-se por computador um sistema físico que realiza algum tipo de computação. Assumiu-se que os computadores pessoais e laptops são ícones da era da informação. O primeiro computador eletromecânico foi construído por Konrad Zuse (1910–1995). Atualmente, um microcomputador é também chamado computador pessoal ou ainda computador doméstico."

# Chamando a função e imprimindo o resultado
ocorrencias = automatoFinito(texto)
print("A palavra 'computador' foi encontrada nas posições:", ocorrencias)