# ArI-mazer
<h3>Trabalho de IA para geração e resolução de labirintos</h3>
<p>Trabalho realizado como parte dos critérios para aprovação na disciplina de Inteligência Artifical</p>
<p>Regras:</p>
<ol>
<li>O aluno escolhe o Labirinto e classifica como fácil, médio ou difícil</li>
<li>Mostra da tela os passos e a quantidade de passos dados para encontrar a saída;</li>
<li>Mostrar qual seria o melhor caminho para a saída</li>
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
###Localizando as portas do labirinto
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
            
<h3>Contexto</h3>
<p>A regra para o agente não informado encontrar a saída do labirinto é a regra da mão esquerda que consiste em colocar a mão esquerda na parede do labirinto e seguir até o final sem tirar a mão dessa forma conseguquentemente o agente vai seguir as seguintes opções:</p>
<ol>
  <li>Se puder virar à esquerda, então vire à esquerda</li>
  <li>Se não puder, mas se puder seguir em frente, então siga</li>
  <li>Se também não puder seguir em frente e se puder virar à direita, então vire à direita</li>
  <li>Finalmente, se estiver em um ponto morto (beco sem saída), então gire 180º e volte</li>
</ol>
<p>
Porém a dificuldade encontrada aqui é que 'virar a esquerda', por exemplo são operações diferentes dependendo da direção do agente, para resolver esse problema foi criado o conceito de contexto através da função abaixo:
</p>
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
<h3>Olhando o caminho</h3>
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
<h3>Andando</h3>
<p>Para facilitar a escrita do código para o deslocamento do agente foi criada a função abaixo:</p>
```python
def anda(pos,passo):
    nova_pos = [pos[0]+passo[0],pos[1]+passo[1]]
    return nova_pos
```

<h2>ArI</h2>
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
<h2>Além do escopo</h2>
<p>Além do ArI, também foi criada uma rotina para geração dos labirintos de forma aleatória, para isto adaptamos o código diposnível <a href="http://code.activestate.com/recipes/578356-random-maze-generator/">AQUI</a> a baixo apresentamos a função reponsável por gerar os labirintos de forma aleatória:</p>
```python
def get_labirinto():
  mx = 41; my = 41 # tamanho do labirinto
  maze = [[0 for x in range(mx)] for y in range(my)]
  pixels = maze
  dx = [0, 1, 0, -1]; dy = [-1, 0, 1, 0] # 4 para mover-se no labirinto
  color = [0, 1] # valores adicionados ao labirinto
  #inicial de uma célula aleatória
  cx = random.randint(0, mx - 1); cy = random.randint(0, my - 1)
  maze[cy][cx] = 1; stack = [(cx, cy, 0)] # empilhar elementos: (x, y, direction)

  while len(stack) > 0:
      (cx, cy, cd) = stack[-1]
      # prevenir zigzag pro labirinto ficar mais bonito
      if len(stack) > 2:
          if cd != stack[-2][2]: dirRange = [cd]
          else: dirRange = range(4)
      else: dirRange = range(4)

      # achar nova clelula pra adicionar
      nlst = [] # lista de vizinhança disponível
      for i in dirRange:
          nx = cx + dx[i]; ny = cy + dy[i]
          if nx >= 0 and nx < mx and ny >= 0 and ny < my:
              if maze[ny][nx] == 0:
                  ctr = 0 # vizinhos ocupados deve ser 1
                  for j in range(4):
                      ex = nx + dx[j]; ey = ny + dy[j]
                      if ex >= 0 and ex < mx and ey >= 0 and ey < my:
                          if maze[ey][ex] == 1: ctr += 1
                  if ctr == 1: nlst.append(i)

      # sem tem mais de um vizinho disponível seleciona aleatoriamente
      if len(nlst) > 0:
          ir = nlst[random.randint(0, len(nlst) - 1)]
          cx += dx[ir]; cy += dy[ir]; maze[cy][cx] = 1
          stack.append((cx, cy, ir))
      else: stack.pop()


  #Insere as portas
  def criaportas(maze):
    posl = 1; posc = 0;

    #entrada
    fim = False
    while(not fim):
      if(maze[(posc+1),posl] == 0):
        maze[posl,posc] = 0
        fim = True
      else:
        posl +=1

    #saída
    posl = maze.shape[0] - 1
    posc = maze.shape[0] - 1
    fim = False
    while(not fim):
      if(maze[(posc-1),posl] == 0):
        maze[posl,posc] = 0
        fim = True
      else:
        posl -=1


    return maze  
```
<h2>Interface para o Usuário</h2>
<p>Todas essa funções foram integradas em uma API hospedada no PythonAnywhere (disponível <a href="http://alsgil13.pythonanywhere.com/">aqui</a>). A função que roda na api está exposta abaixo: </p>

```python
from flask import Flask
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)
@app.route('/')
def serve_ari():
    labirinto = get_labirinto()
    caminho = maoEsquerda(labirinto)
    dificuldade = classifica(caminho)
    labirintobj = {
        "labirinto": labirinto.tolist(),
        "caminho" : caminho,
        "dificuldade" : dificuldade,
        "inicio" : caminho[0],
        "fim" : caminho[-1]
   }
    print(type(labirintobj))
    app_json = json.dumps(labirintobj)
    return app_json
```
<p>Como pode-se observar no código a 'serve_ari' importa as funções descritas anteriormente gerando e calculando a saída do labirinto e monta um json contendo o labirinto, o caminho encontrado, a dificuldade, o início e o fim do labirinto, este json é consumido pelo arquivo que será apresentado a seguir.</p>
<h3>Interface</h3>
<p>Foram criados arquivos html/css/js para consumir os dados da api apresentada anteriormente e gerar um console de interação com o usuário, no final das contas um jogo de labirinto</p>
<h4>Calculando a dificuldade</h4>
<p>Para calcular o nível de dificuldade do labrinto foi utilizado a seguitne fórmula: se o caminho encontrado pelo agente tiver menos de 500 passo o labirinto é classificado como fácil, caso seja maior que 500 e meno que 1000, o labirinto é classificado como médio e caso seja maior que 1000 o labirinto é classificado como difícil, a função que faz essa classificação está exposta abaixo:</p>
```python
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
```
<a href="labirinto.html"><button class="btn btn-block btn-success">Iniciar Iterface de Usuário do Labirinto</button></a>
