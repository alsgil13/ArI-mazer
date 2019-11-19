#Definindo o contexto, pra saber se estamos indo pro norte, pro sul, leste....
#Isso é necessário pra saber qual operação devemos fazer para virar à esquerda

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
    
    
