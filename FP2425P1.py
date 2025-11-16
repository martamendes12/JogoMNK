def eh_tabuleiro(tab):
    """ eh_tabuleiro: universal → booleano """
    #Confirmar que é um tuplo dentro do dominio
    if (type(tab) is not tuple) or (len(tab) not in range(2,101)):
        return False
     #Confirmar os elementos dentro do tuplo
    for sub_tuplo in tab:
        #Confirmar que são tuplos
        if type(sub_tuplo) is not tuple: 
              return False
        #Confirmar que estão todos dentro do dominio
        if len(tab[0]) not in range (2,101):
                return False
        #Confirmar que tem todos o mesmo comprimento
        if len(sub_tuplo) != len(tab[0]):
                return False
        #confirmar que os elementos dentro dos sub-tuplos são inteiros entre -1,0 e 1
        for e in sub_tuplo:
            if e not in (-1,0,1) or type(e) is not int:
                return False
    return True

def eh_posicao(pos):
    """ eh_posicao: universal → booleano"""
    #Confirmar que a posiçao é um numero inteiro dentro do dominio
    if not(type(pos) is int and pos in range (1,100**2+1)):
        return False
    return True

def obtem_dimensao(tab):
    """obtem_dimensao: tabuleiro → tuplo"""
    #Confirmar que o tabuleiro é valido
    if not eh_tabuleiro(tab):
        return False
    #Devolver um tuplo com o numero de linhas e de colunas
    return (len(tab), len(tab[0]))

def obtem_valor(tab,pos):
    """obtem_valor: tabuleiro × posicao → inteiro"""
    #Validar o tabuleiro e a posição
    if not eh_tabuleiro(tab) or not eh_posicao(pos):
        return False
    #encontar o indice da coluna da posição
    col=(pos-1)%len(tab[0])
    #encontrar o indice da linha da posiçao
    lin=(pos-1)//len(tab[0])
    #mostrar o valor
    valor=tab[lin][col]
    return valor

def obtem_coluna(tab,pos):
    """obtem_coluna: tabuleiro × posicao → tuplo"""
    #verificar se os valores são válidos usando as outras funções
    if not eh_tabuleiro(tab) or not eh_posicao(pos):
        return False
    elif pos not in range(1,len(tab)*len(tab[0])+1):
        return False
    #criar um tuplo vazio que vai ser a coluna
    coluna=()
    #fazer com que a posição esteja na mesma linha para quando for feita a coluna, esteja por ordem 
    while pos > len(tab[0]):
        pos -= len(tab[0])
    #iterar por um numero ate chegar a ultima linha para adicionar os numeros à coluna
    for i in range(0,len(tab)):
            coluna += (pos + i*(len(tab[0])),)
    return coluna

def obtem_linha(tab,pos):
    """obtem_linha: tabuleiro × posicao → tuplo"""
    #Validar o tabuleiro e a posição
    if not eh_tabuleiro(tab) or not eh_posicao(pos):
        return False
    elif pos not in range(1,len(tab)*len(tab[0])+1):
        return False
    #ver em que elemento da linha está a posição e posicionalo no primeiro
    while pos%len(tab[0]) != 1 or pos%len(tab[0]) == 0:
         pos -= 1
    #criar um tuplo para a linha e adicionar todos os seguintes até ao final da linha
    linha=()
    for i in range (0, len(tab[0])):
         linha += (pos + i,)
    return linha

def obtem_diagonais(tab,pos):
    """obtem_diagonais: tabuleiro × posicao → tuplo """
    #Validar o tabuleiro e a posição
    if not eh_tabuleiro(tab) or not eh_posicao(pos):
        return False
    elif pos not in range(1,len(tab)*len(tab[0])+1):
        return False

    #criar um tuplo para a diagonal e econtrar a linha e a coluna da posicao
    diagonal=()
    i_coluna=(pos-1)%len(tab[0])
    i_linha=(pos-1)//len(tab[0])

    #mudar a linha e a coluna para o maximo a cima e a direita
    while i_coluna>0 and i_linha>0:
        i_coluna-=1
        i_linha-=1

    #mudar a posicao, para a nova posicao com a coluna e a linha e adiciona-la ao tuplo
    p_diagonal=i_linha*len(tab[0])+i_coluna+1
    diagonal+=(p_diagonal,)

    #iterar pelos valores da diagonal e adiciona-los a diagonal ate ao ultimo elemento
    while i_coluna+1<len(tab[0]) and i_linha+1<len(tab):
        i_linha+=1
        i_coluna+=1
        p_diagonal = i_linha*len(tab[0])+i_coluna+1
        diagonal+=(p_diagonal,)
    
    #fazer a mesma coisa para a antidiagonal
    antidiagonal=()
    i_coluna=(pos-1)%len(tab[0])
    i_linha=(pos-1)//len(tab[0])

    #mudar para o elemento mais a baixo a direita
    while i_coluna>0 and i_linha<len(tab)-1:
        i_coluna-=1
        i_linha+=1

    p_antidiagonal=i_linha*len(tab[0])+i_coluna+1
    antidiagonal+=(p_antidiagonal,)
    
    #iterar ate ao limite superior direito
    while i_coluna+1<len(tab[0]) and i_linha>0:
        i_linha-=1
        i_coluna+=1
        p_antidiagonal=i_linha*len(tab[0])+i_coluna+1
        antidiagonal+=(p_antidiagonal,)
    
    return ((diagonal), (antidiagonal))

def tabuleiro_para_str(tab):
    """tabuleiro_para_str: tabuleiro → cad. carateres"""
    #Validar o tabuleiro e a posição
    if not eh_tabuleiro(tab):
        return
    #criar uma string vazia para adicionar os valores
    str=""
    #iterar pelas linhas na tabela
    for i in range(0,len(tab)):
        line=""
        #iterar pelos elementos nas linhas e adicionar os valores a linha
        for l in range (0,len(tab[0])):
            if tab[i][l]==1:
                line += "X"
            elif tab[i][l]==-1:
                line += "O"
            elif tab[i][l]==0:
                line += "+"  
            #adicionar os hifens sempre que se adiciona um elemento a linha ate ao ultimo
            if l <len(tab[0])-1:
                line+="---" 
        #adicionar as linhas a string
        str = str +line
        #se nao for a ultima linha, adicionar paragrafos e barras entre linhas
        if i < len(tab)-1:
            str = str + "\n" + (len(tab[0])-1)*"|   " + "|\n" 
    return str

def eh_posicao_valida(tab,pos):
    """eh_posicao_valida: tabuleiro × posicao → booleano"""
    #Verificar os valores
    if not eh_tabuleiro(tab) or not eh_posicao(pos):
        raise ValueError('eh_posicao_valida: argumentos invalidos')
    #Verificar se a posição não estiver dentro das posições disponíveis
    if pos < 1 or pos > len(tab) * len(tab[0]):
        return False
    return True

def eh_posicao_livre(tab,pos):
    """eh_posicao_livre: tabuleiro × posicao → booleano"""
    #Verificar se a posição é válida
    if not eh_tabuleiro(tab) or not eh_posicao(pos):
        raise ValueError('eh_posicao_livre: argumentos invalidos')
    if not eh_posicao_valida(tab,pos):
        raise IndexError("tuple index out of range")
    #Se o valor for 0, está livre
    if obtem_valor(tab,pos)==0:
        return True
    else:
        return False

def obtem_posicoes_livres(tab):
    """obtem_posicoes_livres: tabuleiro → tuplo"""
    #Verificar se o tabuleiro é válido
    if not eh_tabuleiro(tab):
        raise ValueError('obtem_posicoes_livres: argumento invalido')
    #criar a posição atual, para ser iterada e um tuplo vazio para guardar as posições livres
    pos_atual = 1
    livres =()
    #iterar pelas linhas no tabuleiro e os elementos nas linhas
    for i in tab:
        for l in i:
            #se for 0, adicionar ao tuplo de livres
            if l == 0:
                livres += (pos_atual,)
            pos_atual += 1
    return livres

def obtem_posicoes_jogador(tab,jog):
    """obtem_posicoes_jogador: tabuleiro × inteiro → tuplo"""
    #validar o tabuleiro e o jogador
    if not eh_tabuleiro(tab) or jog not in (-1,1):
        raise ValueError('obtem_posicoes_jogador: argumentos invalidos')
    
    #Fazer a mesma coisa que fiz para ver se as posicoes livres mas para cada jogador
    pos_atual = 1
    posicoes =()
    if jog==1:
        for i in tab:
            for l in i:
                if l == 1:
                    posicoes += (pos_atual,)
                pos_atual += 1
    elif jog==-1:
        for i in tab:
            for l in i:
                if l == -1:
                    posicoes += (pos_atual,)
                pos_atual += 1
    return posicoes

def obtem_posicoes_adjacentes(tab,pos):
    """obtem_posicoes_adjacentes: tabuleiro × posicao → tuplo"""
    #validar se a posicao é valida
    if not eh_tabuleiro(tab) or not eh_posicao(pos) or not eh_posicao_valida(tab,pos):
         raise ValueError('obtem_posicoes_adjacentes: argumentos invalidos')
    
    #encontrar a linha e a coluna da posicao
    lin=(pos-1)//len(tab[0])
    col=(pos-1)%len(tab[0])
    
    #criar um tuplo para as posicoes adjacentes e confirmar para cada adjacente com os limites de linhas e colunas
    pos_adj=()
    if col>0 and lin>0:
        pos_adj+=(pos-len(tab[0])-1,)
    if lin>0:
        pos_adj += (pos-len(tab[0]),)
    if lin>0 and col<len(tab[0])-1:
        pos_adj += (pos-len(tab[0])+1,)
    if col>0:
        pos_adj += (pos-1,)
    if col<len(tab[0])-1:
        pos_adj += (pos+1,)
    if lin<len(tab)-1 and col>0:
        pos_adj += (pos+len(tab[0])-1,)
    if lin<len(tab)-1:
        pos_adj += (pos+len(tab[0]),)
    if lin<len(tab)-1 and col<len(tab[0]):
        pos_adj += (pos+len(tab[0])+1,)
    
    return pos_adj

def ordena_posicoes_tabuleiro(tab,tup):
    """ordena_posicoes_tabuleiro: tabuleiro × tuplo → tuplo """
    #validar as entradas
    if not type(tup) is tuple or not eh_tabuleiro(tab):
        raise ValueError('ordena_posicoes_tabuleiro: argumentos invalidos')
    for pos in tup:
        if type(pos) is not int:
            raise ValueError('ordena_posicoes_tabuleiro: argumentos invalidos')
    
    #definir o centro do tabuleiro e guarda-lo numa lista
    centro= (((len(tab)//2))*len(tab[0]))+(len(tab[0]))//2+1
    #encontrar a coluna e a linha do centro
    coluna_centro= (centro-1)%len(tab[0])
    linha_centro= (centro-1)//len(tab[0])
    posicoes=()
    #criar um dicionario vazio para as distancias
    distancias={}
    #encontrar as distancias de cada elemento, usando o maximo de distancia entre colunas e linhas
    for pos in tup:
        coluna_pos=(pos-1)%len(tab[0])
        linha_pos=(pos-1)//len(tab[0])
        dis_col=abs(coluna_centro-coluna_pos)
        dis_lin=abs(linha_centro-linha_pos)
        distancia=max(dis_col,dis_lin)
        #se a distancia ja estiver no dicionario, adicionar a posicao a lista
        if distancia in distancias:
            (distancias[distancia]).append(pos)
        #se nao, criar a nova chave
        else:
            distancias[distancia]=[pos]
        
    #iterar pelos elementos no dicionario
    for ele in range(1,max(obtem_dimensao(tab))):
        if ele in distancias:
            #ordenar as litas de cada distancia e adicionalas ao tuplo
            lista_distancia=sorted(distancias[ele])
            lista_distancia=tuple(lista_distancia)
            posicoes+=(lista_distancia)
        
    return posicoes

def marca_posicao(tab,pos,jog):
    """marca_posicao: tabuleiro × posicao × inteiro → tabuleiro"""
    if not eh_tabuleiro(tab) or jog not in (1,-1) or not eh_posicao(pos):
        raise ValueError('marca_posicao: argumentos invalidos')
    if not eh_posicao_livre(tab,pos):
        raise ValueError('marca_posicao: argumentos invalidos')
    #encontrar linha e coluna da posicao
    lin=(pos-1)//len(tab[0])
    col=(pos-1)%len(tab[0])

    #criar a nova linha
    nova_lin=()
    #adicionar os elementos, ate a posicao que mudou
    if col>0:
        nova_lin+=tab[lin][0:col]
    #adicionar a posicao que mudou
    nova_lin+=(jog,)
    #adicionar os elementos depois da posicao que mudou
    if col<len(tab[lin])-1:
        nova_lin+=tab[lin][col+1:]
    #criar a tabela e fazer a mesma coisa mas em vez de mudar o elemento, muda a linha
    novo_tab=()
    if lin>0:
        novo_tab+=tab[0:lin]
    novo_tab+=(nova_lin,)
    if lin<len(tab)-1:
        novo_tab+=tab[lin+1:]
    
    return novo_tab

def verifica_k_linhas(tab,pos,jog,k):
    """verifica_k_linhas: tabuleiro × posicao × inteiro × inteiro → booleano"""
    #validar as entradas
    if not eh_tabuleiro(tab) or jog not in (-1,1) or not eh_posicao(pos) or not eh_posicao_valida(tab,pos) or not (type(k) is int) or not k>0:
        raise ValueError('verifica_k_linhas: argumentos invalidos')
    
    #se a posicao dada for o jogador iniciar, se nao, e falso
    if obtem_valor(tab,pos)==jog:
        #iterar pelas diferentes formas de ter consecutivas
        for tup in (obtem_coluna(tab,pos),obtem_linha(tab,pos),obtem_diagonais(tab,pos)[0],obtem_diagonais(tab,pos)[1]):
            #iterar pelas posicoes no tuplo, comecando do indice da posicao dada para ambos os lados
            if pos in tup:
                indice=tup.index(pos)
                consecutivas=1
                if indice<len(tup)-1:
                    for m in range(indice+1,len(tup)):
                        if obtem_valor(tab,tup[m]) == jog:
                            consecutivas+=1
                        else:
                            break
                if indice>0:
                    for n in range(indice-1,-1,-1):
                        if obtem_valor(tab,tup[n]) == jog:
                            consecutivas+=1
                        else:
                            break
                if consecutivas >= k:
                    return True
    return False

def eh_fim_jogo(tab,k):
    """eh_fim_jogo: tabuleiro × inteiro → booleano"""
    #validar entradas
    if not eh_tabuleiro(tab) or type(k) is not int or k<0:
        raise ValueError('eh_fim_jogo: argumentos invalidos')
    if len(obtem_posicoes_livres(tab)) == 0:
        return True
    #se verifica k linhas for verdadeiro, é o fim do jogo, para cada posicao no tabuleiro
    for jog in (-1,1):
        for pos in range(1,len(tab)*len(tab[0])+1):
            if verifica_k_linhas(tab,pos,jog,k) == True:
                return True
    return False

#auxiliar
def obtem_max_linhas(tab,pos,jog):
    """funcao auxiliar que obtem o max de consecutivas possivel obter"""
    #validar as entradas
    if not eh_tabuleiro(tab) or jog not in (-1,1) or not eh_posicao(pos) or not eh_posicao_valida(tab,pos):
        raise ValueError('verifica_k_linhas: argumentos invalidos')
    
    maxtup=()
    #iterar pelas diferentes formas de ter consecutivas
    for tup in (obtem_coluna(tab,pos),obtem_linha(tab,pos),obtem_diagonais(tab,pos)[0],obtem_diagonais(tab,pos)[1]):
        #iterar pelas posicoes no tuplo, comecando do indice da posicao dada para ambos os lados
        if pos in tup:
            indice=tup.index(pos)
            consecutivas=1
            if indice<len(tup)-1:
                for m in range(indice+1,len(tup)):
                    if obtem_valor(tab,tup[m]) == jog:
                        consecutivas+=1
                    else:
                        break
            if indice>0:
                for n in range(indice-1,-1,-1):
                    if obtem_valor(tab,tup[n]) == jog:
                        consecutivas+=1
                    else:
                        break
                    #adicionar a quantidade de consecutivas a um tuplo
            maxtup+=(consecutivas,)
    #obter o maximo do tuplo e devolver
    maxlinhas=max(maxtup)
    return maxlinhas

#auxiliar
def obtem_distancia_posicoes(tab,pos,centro):
    """funcao auxiliar que encontra a distancia de uma posicao ao centro"""
    #encontrar a distancia
    dis_col=abs((centro-1)%len(tab[0])-(pos-1)%len(tab[0]))
    dis_lin=abs((centro-1)//len(tab[0])-(pos-1)//len(tab[0]))
    distancia=max(dis_col,dis_lin)
    return distancia

def escolhe_posicao_manual(tab):
    """escolhe_posicao_manual: tabuleiro → posicao"""
    #validar entradas
    if not eh_tabuleiro(tab):
        raise ValueError('escolhe_posicao_manual: argumento invalido')

    #criar um while para pedir um input certo repetitidamente
    while True:
        pos=input("Turno do jogador. Escolha uma posicao livre: ")
        #se o input for valido, devolve-lo
        if pos.isdigit():
            pos=int(pos)
            if pos in obtem_posicoes_livres(tab):
                return pos
            
def escolhe_posicao_auto(tab,jog,k,lvl):
    """escolhe_posicao_auto: tabuleiro × inteiro × inteiro × cad. carateres→ posicao"""
    #validar as entradas
    if not eh_tabuleiro(tab) or jog not in (-1,1) or type(k) is not int or k<0:
        raise ValueError('escolhe_posicao_auto: argumentos invalidos')
    #usar as funcoes atribuidas para cada nivel de dificuldade e dar erro se nao existir o nivel
    if lvl=='facil':
        return estrategia_facil(tab,jog)
    elif lvl=='normal':
        return estrategia_normal(tab,jog,k)
    elif lvl=='dificil':
        return estrategia_dificil(tab,jog,k)
    else:
        raise ValueError('escolhe_posicao_auto: argumentos invalidos')

def estrategia_facil(tab,jog):
    """estrategia de jogo mais facil, Se existir no tabuleiro pelo menos uma posi¸c˜ao livre e adjacente a uma pedra pr´opria, jogar numa dessas posi¸c˜oes; Se n˜ao, jogar numa posi¸c˜ao livre."""
    #se houver posicoes adjacentes a do jogador, livres, adicionalas a um tuplo
    posicoes_adjacentes_livres=()
    for pos in obtem_posicoes_jogador(tab,jog):
        for adj in obtem_posicoes_adjacentes(tab,pos):
            if eh_posicao_livre(tab,adj):
                posicoes_adjacentes_livres.append(adj)
    #escolher a mais proxima do centro
    if posicoes_adjacentes_livres:
        return ordena_posicoes_tabuleiro(tab,tuple(posicoes_adjacentes_livres))[0]
    
    #se nao, escolhe a livre mais proxima do centro
    return ordena_posicoes_tabuleiro(tab,obtem_posicoes_livres(tab))[0]

def estrategia_normal(tab,jog,k):
    "estrategia de jogo de dificuldade normal, Determinar o maior valor de L ≤ k tal que o pr´oprio ou o advers´ario podem conseguir colocar L pe¸cas consecutivas na pr´oxima jogada numa linha vertical, horizontal ou diagonal que contenha essa jogada. Para esse valor: Se existir pelo menos uma posi¸c˜ao que permita obter uma linha que contenha essa posi¸c˜ao com L pedras consecutivas pr´oprias, jogar numa dessas posi¸c˜oes; Se n˜ao, jogar numa posi¸c˜ao que impossibilite o advers´ario de obter L pedras consecutivas numa linha que contenha essa posi¸c˜ao."
    #criar um tuplo com as posicoes livres 
    tab_liv=obtem_posicoes_livres(tab)
    resultados=[]
    #para cada jogador
    for temp_jog in (-1,1):
        #cada posicao no tuplo de livres
        for pos in tab_liv:
            #encontrar o centro, a distancia do centro, marcar a posicao e encontrar a melhor hipotese de consecutivas
            centro=(len(tab)//2)*len(tab[0])+(len(tab[0])//2)+1
            distancia=obtem_distancia_posicoes(tab,pos,centro)
            novo_tab= marca_posicao(tab,pos,temp_jog)
            maxlinhas=obtem_max_linhas(novo_tab,pos,temp_jog)
            if maxlinhas>k:
                maxlinhas=k
            #se for o proprio jogador, adicionar aos resultados com um 0
            if temp_jog==jog:
                resultados+=[(-maxlinhas,0,distancia,pos)]
            #se for o outro jogador, adicionar aos resultados com um 1
            else:
                resultados+=[(-maxlinhas,1,distancia,pos)]
    #ordenar os resultados e devolver a distancia do primeiro
    resultados=sorted(resultados)
    pos=resultados[0][3]
    return pos

def estrategia_dificil(tab,jog,k):
    """estrategia de jogo dificil, se existir uma posicao que possivelmente faca ganhar, usar, se nao, bloquear a do adversario"""
    #criar um tuplo de livres e ordenalo
    tab_liv=obtem_posicoes_livres(tab)
    tab_liv=ordena_posicoes_tabuleiro(tab,tab_liv)

    #iterar pelo tuplo a comecar na segunda posicao, porque a primeira e a central
    for i in range(1,len(tab_liv)):
        pos=tab_liv[i]
        novo_tab=marca_posicao(tab,pos,jog)
        maxlinha=obtem_max_linhas(novo_tab,pos,jog)
        if maxlinha>=k:
            return pos
    #mesma coisa para o outro jogador
    for i in range(1,len(tab_liv)):
        pos=tab_liv[i]
        novo_tab=marca_posicao(tab,pos,-jog)
        maxlinha=obtem_max_linhas(novo_tab,pos,-jog)
        if maxlinha>=k:
            return pos

def resultado_jogo(tab,k,jog,comp):
    """funcao auxiliar para obter o resultado do jogo"""
    if len(obtem_posicoes_livres(tab)) == 0:
        return "EMPATE\n0"
    #se verifica k linhas for verdadeiro, é o fim do jogo, para cada posicao no tabuleiro
    for temp_jog in (-1,1):
        for pos in range(1,len(tab)*len(tab[0])+1):
            if verifica_k_linhas(tab,pos,temp_jog,k) == True:
                if temp_jog==jog:
                    return "VITORIA\n"+str(jog)
                elif temp_jog==comp:
                    return "DERROTA\n"+str(comp)

def jogo_mnk(cfg,jog,lvl):
    """ jogo mnk: tuplo × inteiro × cad. carateres → inteiro"""
    #encontrar a linha, coluna e k do primeiro elemento
    lin=cfg[0]
    col=cfg[1]
    k=cfg[2]
    tab=lin*((col*(0,)),)
    #validar os argumentos
    if not eh_tabuleiro(tab) or jog not in (-1,1) or lvl not in ('facil', 'normal' ,'dificil') or type(k) is not int or not k>0:
        raise ValueError('jogo_mnk: argumentos invalidos')
    #fazer para ambos os jogadores, porque depende de quem comeca
    if jog==1:
        print("Bem-vindo ao JOGO MNK.\nO jogador joga com 'X'.\n" + tabuleiro_para_str(tab))
        comp=-1
        #obter valores e devolvelos
        while not eh_fim_jogo(tab,k):
            pos=escolhe_posicao_manual(tab)
            tab= marca_posicao(tab,pos,jog)
            print(tabuleiro_para_str(tab))
            print("Turno do computador ("+ lvl + "):")
            pos=escolhe_posicao_auto(tab,comp,k,lvl)
            tab= marca_posicao(tab,pos,comp)
            print(tabuleiro_para_str(tab))
        print(resultado_jogo(tab,k,jog,comp))
    if jog==-1:
        print("Bem-vindo ao JOGO MNK.\nO jogador joga com 'O'.\n" + tabuleiro_para_str(tab))
        comp=1
        while not eh_fim_jogo(tab,k):
                print("Turno do computador ("+ lvl + "):")
                pos=escolhe_posicao_auto(tab,comp,k,lvl)
                tab= marca_posicao(tab,pos,comp)
                print(tabuleiro_para_str(tab))
                pos=escolhe_posicao_manual(tab)
                tab= marca_posicao(tab,pos,jog)
                print(tabuleiro_para_str(tab))
        print(resultado_jogo(tab,k,jog,comp))

