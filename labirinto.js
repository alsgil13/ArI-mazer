


var canvas = $('#GameBoardCanvas');

var requestURL = 'http://alsgil13.pythonanywhere.com/';    
var request = new XMLHttpRequest();
request.open('GET', requestURL);
request.responseType = 'json';
request.send();


request.onload = function() {
    var labirinto = request.response;
    
    //l = labirinto['labirinto'];
    //console.log(labirinto['inicio'][0]);
    var dificuldade = labirinto['dificuldade'];
    var caminho = labirinto['caminho'];
    var tamanho = caminho.length;
    window.alert("bem vindo ao ArI-Mazer o desafio a seguir tem a dificuldade: " + dificuldade + ". \nResolva em menos de "+ tamanho + " passos para conseguir 3 estrelas");
    var inicio = {
        x: labirinto['inicio'][1],
        y: labirinto['inicio'][0]
    };

    var saida = {
        x: labirinto['fim'][1],
        y: labirinto['fim'][0]
    };
    var board = labirinto['labirinto'];
    var contador = 0;
    var player = inicio;


    //Desenha o tabuleiro
    function draw() {
        var width = canvas.width();
        var blockSize = width / board.length;
        var ctx = canvas[0].getContext('2d');
        ctx.setTransform(1, 0, 0, 1, 0, 0);
        ctx.clearRect(0, 0, width, width);
        ctx.fillStyle = "white";
        //Faz um loop através do tabuleiro para desenhar os muros
        for (var y = 0; y < board.length; y++) {
            for (var x = 0; x < board[y].length; x++) {
            //Desenha o Muro
                if (board[y][x] === 1) {
                    
                    ctx.fillRect(x * blockSize, y * blockSize, blockSize, blockSize);
                }

                if(board[y][x] === -1){
                    // var half = blockSize / 2;
                    // ctx.fillStyle = "white";
                    // ctx.arc(player.x * blockSize + half, player.y * blockSize + half, half, 0, 2 * Math.PI);
                    // ctx.fill();
                    ctx.beginPath();
                    var half = blockSize / 2;
                    ctx.fillStyle = "blue";
                    ctx.arc(player.x * blockSize + half, player.y * blockSize + half, half, 0, 2 * Math.PI);
                    ctx.fill();
                }
            
            }
        }





    //Desenha a bolinha do jogador
        ctx.beginPath();
        var half = blockSize / 2;
        ctx.fillStyle = "blue";
        ctx.arc(player.x * blockSize + half, player.y * blockSize + half, half, 0, 2 * Math.PI);
        ctx.fill();



    }


    //checa se o movimento solicitado está dentro do tabuleiro ou não é contra uma parede
    function canMove(x, y) {
    return (y >= 0) && (y < board.length) && (x >= 0) && (x < board[y].length) && (board[y][x] != 1);
    }



    $(document).keyup(function(e) {
    if ((e.which == 38) && canMove(player.x, player.y - 1)) { 
        player.y--;
        contador++;
        console.log(player.x);
        console.log(player.y);
        
    } else if ((e.which == 40) && canMove(player.x, player.y + 1)) { 
        player.y++;
        contador++;
        console.log(player.x);
        console.log(player.y);
    } else if ((e.which == 37) && canMove(player.x - 1, player.y)) {
        player.x--;
        contador++;
        console.log(player.x);
        console.log(player.y);
    } else if ((e.which == 39) && canMove(player.x + 1, player.y)) {
        player.x++;
        contador++;
        console.log(player.x);
        console.log(player.y);
    }
    if (player.x == saida.x && player.y == saida.y) {
        estrelas = 1;
        if(contador<tamanho){
            estrelas = 3;
        }
        window.alert("Parabéns, você concluiu o labirinto com: " + contador + " passos\nVocê conseguiu "+ estrelas + " estrelas neste desafio");
    }



    draw();
    e.preventDefault();
    });
    draw();

    // function revelaCaminho(){
    //     for(var x = 0; x < caminho.length; x++){
    //         console.log(caminho[x])
    //     }
    // }    
    
    $('#revela').click(function(){
        console.log(caminho.length)
        for(var x = 0; x < caminho.length; x++){
            board[caminho[x]] = -1;
            console.log(caminho[x]);
            console.log(board[caminho[x]]);
        }
        draw();        
    })

}

