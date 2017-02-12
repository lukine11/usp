import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo
    e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma
    lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e
    devolve uma lista das
    palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto
    e deve devolver o grau de similaridade nas assinaturas.'''

    soma = abs (as_a[0] - as_b[0])
    soma+= abs (as_a[1] - as_b[1])
    soma+= abs (as_a[2] - as_b[2])
    soma+= abs (as_a[3] - as_b[3])
    soma+= abs (as_a[4] - as_b[4])
    soma+= abs (as_a[5] - as_b[5])

    return soma/6


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver
    a assinatura do texto.'''

    # TAMANHO MEDIO PALAVRAS
    totalPalavras = 0
    tamanhoPalavras = 0
    listaSenteca = separa_sentencas(texto)
    listaPalavrasTexto = []
    for sentenca in listaSenteca:
      listaFrases = separa_frases(sentenca)
      for frases in listaFrases:
        listaPalavras = separa_palavras(frases)
        totalPalavras += len(listaPalavras) #quantidade palavras
        for palavra in listaPalavras:
          listaPalavrasTexto.append(palavra)
          tamanhoPalavras += len(palavra)
    tamanhoMedioP = tamanhoPalavras / totalPalavras

    #RELAÇÃO TYPE-TOKEN
    quant_palavra_diferente = n_palavras_diferentes(listaPalavrasTexto)
    RTT = quant_palavra_diferente / totalPalavras

    #RAZAO HAPAX LEGOMANA
    quant_palavras_unicas = n_palavras_unicas(listaPalavrasTexto)
    RHL = quant_palavras_unicas/totalPalavras

    #TAMANHO MEDIO SENTENÇA
    tamanhoSentença = 0
    listaSenteca = separa_sentencas(texto)
    totalSenteca = len(listaSenteca)
    for sentenca in listaSenteca:
      tamanhoSentença += len(sentenca)
    tamanhoMedioS = tamanhoSentença / totalSenteca

    #COMPLEXIDADE
    quant_Frases  = 0
    for sentenca in listaSenteca:
      listaFrases = separa_frases(sentenca)
      quant_Frases += len(listaFrases)
    complexidade = quant_Frases/totalSenteca

    #TAMANHO MEDIO FRASE
    tamanhoFrase = 0
    quant_caracteres = 0
    for sentenca in listaSenteca:
      listaFrases = separa_frases(sentenca)
      for Frase in listaFrases:
        quant_caracteres += len(Frase)
    tamanhoMedioF = quant_caracteres / quant_Frases

    return [tamanhoMedioP, RTT, RHL, tamanhoMedioS, complexidade, tamanhoMedioF]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e
    deve devolver o numero (0 a n-1) do texto com maior
    probabilidade de ter sido infectado por COH-PIAH.'''

    textoCopia = 0
    similaridadeCopia = None
    for posicao, texto in enumerate(textos):
        ass = calcula_assinatura(texto)
        similaridade = compara_assinatura(ass, ass_cp)
        if (similaridadeCopia == None or similaridade < similaridadeCopia):
            similaridadeCopia = similaridade
            textoCopia = posicao


    return textoCopia


assinaturas = le_assinatura()
textos = le_textos()

texto_infectado = avalia_textos(textos, assinaturas)

print ("O autor do texto ", texto_infectado+1, " está  infectado")
