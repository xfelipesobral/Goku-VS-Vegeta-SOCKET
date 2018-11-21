var Client = {};
Client.socket = io.connect();

Client.sendTest = function(){
    console.log("test sent");
    Client.socket.emit('test');
};

Client.askNewPlayer = function(){
    Client.socket.emit('newplayer');
};

Client.sendClick = function(x,y){
  Client.socket.emit('click',{x:x,y:y});
};

Client.moverJ = function(x, y){ // MOVER JOGADOR
    Client.socket.emit('moverJogador', {dx:x, dy:y});
};

Client.atualizarJ = function(player){
    console.log("chegou aqui");
    Client.socket.emit('atualizarJogador', {player:player});
}

Client.socket.on('newplayer',function(data){
    Game.addNewPlayer(data.id,data.x,data.y);
});

Client.socket.on('allplayers',function(data){
    for(var i = 0; i < data.length; i++){
        Game.addNewPlayer(data[i].id,data[i].x,data[i].y);
    }

    Client.socket.on('move',function(data){
        Game.movePlayer(data.jogador,data.dx,data.dy);
    });

    Client.socket.on('remove',function(id){
        Game.removePlayer(id);
    });
});


