# ArI-mazer
###Trabalho de IA para geração e resolução de labirintos</h3>
<p>Trabalho realizado como parte dos critérios para aprovação na disciplina de Inteligência Artifical</p>
<p>Regras:</p>
<ol>
<li>O aluno escolhe o Labirinto e classifica como fácil, médio ou difícil</li>
<li>Mostra da tela os passos e a quantidade de passos dados para encontrar a saída;</li>
<li>MOstrar qual seria o melhor caminho para a saída</li>
</ol>
<h2>Criadores</h2>
<ul>
  <li>André Luiz de Souza Gil</i>
  <li>Lucas Cardoso</li>
  <li>Lucas Oliveira Coelho</li>
</ul>
<h2>Sobre o trabalho</h2>
<p>Para a realização deste trabalho foi criado um labirinto inicial composto por 0 (onde há passagem) e 1 (onde há parede), foi programado um agente não informado para resolver este labirinto</p>
<h3>Como funciona?</h3>
<p>São 5 as funções que fazem o agente funcionar sendo uma função auxiliar para localizar as portas de entrada e saída do labirinto, três funções básicas do agente e uma função que integra as demais</p>
<h4>Localizando as portas do labirinto</h4>
<p>Para que o agente possa iniciar seu percuso pelo labirinto é preciso econtroar as portas de entrada e saída. Este agente foi programado para localizá-las sempre na primeira coluna (entrada) e na última coluna(saída), ele basicamente percorre essas duas colunas a procura de um valor 0. Caso exista mais de uma entrada ou saída o agente entenderá como entrada somente a porta mais acima e como saída a porta mais abaixo.</p>

```python
def locPortas(labirinto):
    alt, larg = labirinto.shape
    i = 0
    while(i<alt):
        if(labirinto[i,0]==0):
            ini = [i,0]
        if(labirinto[i,alt-1]==0):
            fim = [i,alt]
        i += 1
    return ini, fim
```
            
####Contexto
<p>A regra para o agente não informado encontrar a saída do labirinto é a regra da mão esquerda que consiste em colocar a mão esquerda na parede do labirinto e seguir até o final sem tirar a mão dessa forma conseguquentemente o agente vai seguir as seguintes opções:</p>
<ol>
  <li>Se puder virar à esquerda, então vire à esquerda</li>
  <li>Se não puder, mas se puder seguir em frente, então siga</li>
  <li>Se também não puder seguir em frente e se puder virar à direita, então vire à direita</li>
  <li>Finalmente, se estiver em um ponto morto (beco sem saída), então gire 180º e volte</li>
</ol>
Porém a dificuldade encontrada aqui é que 'virar a esquerda', por exemplo são operações diferentes dependendo da direção do agente, para resolver esse problema foi criado o conceito de contexto através da função abaixo:
```python
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
```
#### Olhando o caminho
<p>Além de saber a direção que está indo também é (extremamente) importante saber se há caminho naquela direção, para isso foi criada a função abaixo que retorna todos os caminhos possíveis a partir da posição do agente:</p>
```python
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
```
#### Andando
<p>Para facilitar a escrita do código para o deslocamento do agente foi criada a função abaixo:</p>
```python
def anda(pos,passo):
    nova_pos = [pos[0]+passo[0],pos[1]+passo[1]]
    return nova_pos
```

##ArI
<p>O nome ArI foi escolhido em, homenagem à Ariadne, personagem da mitologia grega (filha de Minus) que deu o fio dourado para que teseu pudesse escapar do labirinto de seu irmão (Minotauro). Eis abaixo o coração do algoritmo que integra todas as funções demonstradas até aqui para resolver o labirinto.</p>
```python
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
```

<a href="labirinto.html">Iniciar Iterface de Usuário do Labirinto</a>
