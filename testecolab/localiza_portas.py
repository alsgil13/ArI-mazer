#definindo uma função pra localizar as portas
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
