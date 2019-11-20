def locPortas(labirinto):
    alt, _ = labirinto.shape
    i = 0
    while(i<alt):
        if(labirinto[i,0]==0):
            ini = [i,0]
        if(labirinto[i,alt-1]==0):
            fim = [i,alt]
        i += 1
    return ini, fim


def get_contexto(pos,nova_pos):

    #recebe duas posições da matriz (x e y, x2 e y2)
    
    #O dicionário foi ordenado seguindo a regra da mão esquerda
    contexto = {
        "norte" : {
            "esquerda" : (0,-1),
            "frente"   : (-1,0),
            "direita"  : (0,1),
            "retorno"  : (1,0)
        },
        "sul" : {
            "esquerda" : (0,1),
            "frente"   : (1,0),
            "direita"  : (0,-1),
            "retorno"  : (-1,0)
        },
        "oeste" : {
            "esquerda" : (1,0),
            "frente"   : (0,-1),
            "direita"  : (-1,0),
            "retorno"  : (0,1)
        },
        "leste" : {
            "esquerda" : (-1,0),
            "frente"   : (0,1),
            "direita"  : (1,0),
            "retorno"  : (0,-1)
        }
    }

    
    #verifica pra onde foi o passo
    
    
    if (nova_pos[0]<pos[0]):
        return contexto['norte']
    elif (nova_pos[0]>pos[0]):
        return contexto['sul']
    elif (nova_pos[1]<pos[1]):
        return contexto['oeste']
    elif (nova_pos[1]>pos[1]):
        return contexto['leste']
    else:
        return "Mesma Posição"
    



#Função para achar o caminho possível
def olha(labirinto,pos,contexto):
    '''
        Recebe Labirinto, a posição e o contexto
        percorre o contexto verificando se há caminho
        retorna uma tupla de direção asism que encontrar um caminho possível
        
        
    '''
    
    a,l = labirinto.shape
    
    for c in contexto:
        #Arrumar pegando o tamanho do labirinto
        temp = [pos[0]+contexto[c][0],pos[1]+contexto[c][1]]
        if(temp[0] > (a-1)):
            temp[0] = (a-1)
        if(temp[1] > (l-1)):
            temp[1] = (l-1)

        if( (labirinto[temp[0],temp[1]]) == 0 ):
            return (contexto[c])
        
        

#Função para achar a nova posição a partir do passo
def anda(pos,passo):
    nova_pos = [pos[0]+passo[0],pos[1]+passo[1]]
    return nova_pos            

#Função que vai resolver o labirinto
def maoEsquerda(labirinto):
    
    #cria uma lista para armazenar o caminho
    caminho = []
    
    #Encontra as portas do labirinto
    ini, fim = locPortas(labirinto)
    
    #salva o iníciona lista do caminho
    caminho.append(ini)
    
    #Define o primeiro passo
    primeiro_passo = [ini[0],ini[1]+1]
    
    #pega o contexto do primeiro passo
    contexto = get_contexto(ini,primeiro_passo)
    
    #posiciona no primeir passo
    pos = primeiro_passo[:]
    
    #salva o iníciona lista do caminho
    caminho.append(pos)
    
    while(pos!=fim):
        #define o proximo passo
        passo = olha(labirinto,pos,contexto)

        #define a nova posição
        nova_pos = anda(pos,passo)

        #pega o novo contexto
        contexto = get_contexto(pos,nova_pos)

        #posiciona o cursos na nova posição
        pos = nova_pos[:]

        #Adiciona nova posição à lista de caminho
        caminho.append(pos)

    #retira a última entrada da lista de caminhos pois ela extrapola o labirinto    
    caminho.pop(-1)

    #retorna o caminho percorrido
    return caminho

        
def classifica(caminho):
  tam = len(caminho)
  dif = ''
  if tam < 500:
    dif = 'Fácil'
  elif (tam > 500 and tam < 1000):
    dif = 'Médio'
  else:
    dif = 'Difícil'
  return dif    
    

