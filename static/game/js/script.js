var origin;
const player1 = 'O';
const player2 = 'X';
const cells = document.querySelectorAll('.cell');
startGame();

function startGame(){
    document.querySelector(".alert").style.display = "none"
    origin = Array.from(Array(9).keys());
    for(var i = 0; i < cells.length; i++){
        cells[i].innerText = '';
        cells[i].style.removeProperty('background-color');
        cells[i].addEventListener('click',turnClick,false);

    }
}

function turnClick(square){
    if (typeof origin[square.target.id] == 'number') {
        move = square.target.id;
        turn(move, player1);
        httpGet(move);
    }
}

function turn(squareId, player){
    origin[squareId] = player;
    document.getElementById(squareId).innerText = player;
}

function httpGet(move)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.overrideMimeType("application/json");
    xmlHttp.open( "GET", '/game?move='+move, true ); // false for synchronous request
    xmlHttp.onload  = function() {
         var jsonResponse = JSON.parse(xmlHttp.responseText);
         computer_move =  jsonResponse.computer_move;
         message = jsonResponse.message;
         playing = jsonResponse.playing;
         console.log(computer_move)

         if(computer_move != -1){
            turn(computer_move, player2);
         }
         if(!playing){
            gameOver(message)
         }
    };
    xmlHttp.send();
}

function gameOver(message){
    for (var i = 0; i < cells.length; i++) {
        cells[i].removeEventListener('click', turnClick,false)
    };
    document.querySelector(".alert").style.display = "block";
    document.querySelector(".alert").innerText = message;
}
