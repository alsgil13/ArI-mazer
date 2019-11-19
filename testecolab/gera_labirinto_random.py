#Gerador de labirintos aleatório
#Baseado neste código: http://code.activestate.com/recipes/578356-random-maze-generator/

import random
import numpy as np
from matplotlib import pyplot


def salva_maze(maze,nm):
    nome = "out/"+nm
    fig0, ax0 = pyplot.subplots(nrows=1, ncols=1)
    ax0.imshow(maze).set_cmap("gray")
    ax0.get_xaxis().set_ticks([])
    ax0.get_yaxis().set_ticks([])
    pyplot.savefig(nome+".jpg", bbox="none")
    pyplot.close(fig0)

    
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




  cont = 0
  maze = np.array(maze)
  
  #Inverte os valores do labirinto 
  for x in range(maze.shape[0]):
    for y in range(maze.shape[1]):
      if (maze[x,y] == 1):
        maze[x,y] = 0
      else:
        maze[x,y] = 1

  maze = np.pad(maze,1,'constant', constant_values=(1))
  maze = criaportas(maze)
  return maze
