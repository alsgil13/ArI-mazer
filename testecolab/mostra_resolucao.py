labirinto = get_primeiro_labirinto()
caminho = maoEsquerda(labirinto)

#Trocando os valores do caminho para podemor observar
for c in caminho:
    labirinto[c[0],c[1]] = -1
    
fig, ax = plt.subplots()
fig.set_size_inches(18.5, 10.5)
im = ax.imshow(labirinto)
plt.show()    
print(len(caminho))
