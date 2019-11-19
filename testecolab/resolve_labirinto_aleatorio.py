#Medindo desempenho
from timeit import default_timer as timer

#labirinto = get_primeiro_labirinto()
labirinto = get_labirinto()
start = timer()
caminho = maoEsquerda(labirinto)
end = timer()
tempo_gasto = end - start

dificuldade = classifica(caminho)

print(f"Nível de Dificuldade: {dificuldade}")
print(f"resolvido com {len(caminho)} passos em {tempo_gasto} segundos")


#Altera valores do caminho percorrido para podermos visualizar
for c in caminho:
    labirinto[c[0],c[1]] = -1
    
#Plota o labirinto com o caminho realçado
fig, ax = plt.subplots()
fig.set_size_inches(18.5, 10.5)
im = ax.ims
