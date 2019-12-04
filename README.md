# ArI-mazer
<h3>Trabalho de IA para geração e resolução de labirintos</h3>
<p>Trabalho realizado como parte dos critérios para aprovação na disciplina de Inteligência Artifical<p>
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
<p>Para que o agente possa iniciar seu percuso pelo labirinto é preciso econtroar as portas de entrada e saída. Este agente foi programado para localizá-las sempre na primeira coluna (entrada) e na última coluna(saída), ele basicamente percorre essas duas colunas a procura de um valor 0. Caso exista mais de uma entrada ou saída o agente entenderá como entrada somente a porta mais acima e como saída a porta mais abaixo.<p>
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
<a href="labirinto.html">Iniciar Iterface de Usuário do Labirinto</a>
