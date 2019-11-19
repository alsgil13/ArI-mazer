#Função para achar o caminho possível
def olha(labirinto,pos,contexto):
    '''
        Recebe Labirinto, a posição e o contexto
        percorre o contexto verificando se há caminho
        retorna uma tupla de direção assim que encontrar um caminho possível
    '''
    a,l = labirinto.shape
    for c in contexto:
        
        temp = [pos[0]+contexto[c][0],pos[1]+contexto[c][1]]
        if(temp[0] > (a-1)):
            temp[0] = (a-1)
        if(temp[1] > (l-1)):
            temp[1] = (l-1)
        if( (labirinto[temp[0],temp[1]]) == 0 ):
            return (contexto[c])
        
        
