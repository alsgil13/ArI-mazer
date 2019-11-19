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
