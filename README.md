# ArI-mazer
<h1>Trabalho de IA para geração e resolução de labirintos</h1>

    <head>
            <link rel="stylesheet" type="text/css" href="estilo.css">
            <!-- <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous"> -->
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>

        
    </head>




    <body>
        <div class="tela">
            <canvas id="GameBoardCanvas" width="600px" height="600px"></canvas>
            <script src="labirinto.js"></script>
            <br>
            <input type="button" value="Reiniciar" onclick='javascript:location.reload(true);'>            
            <input type="button" id="revela" value="Revelar Caminho" >
        </div>
    </body>
