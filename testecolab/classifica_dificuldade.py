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
