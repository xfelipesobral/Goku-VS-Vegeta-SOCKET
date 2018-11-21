var Game = {};
var kW;
var kA;
var kS;
var kD;
var teclas;

Game.init = function(){
    game.stage.disableVisibilityChange = true;
};

Game.preload = function() {
    game.load.tilemap('map', 'assets/map/example_map.json', null, Phaser.Tilemap.TILED_JSON);
    game.load.spritesheet('tileset', 'assets/map/tilesheet.png',32,32);
    game.load.image('sprite','assets/sprites/sprite.png');
};

Game.create = function(){
    Game.playerMap = {}; // LISTA DE JOGADORES

    var testKey = game.input.keyboard.addKey(Phaser.Keyboard.ENTER);
    testKey.onDown.add(Client.sendTest, this);

    var map = game.add.tilemap('map');
    map.addTilesetImage('tilesheet', 'tileset');

    var layer;
    for(var i = 0; i < map.layers.length; i++) {
        layer = map.createLayer(i);
    }

    layer.inputEnabled = true;

    /* TECLAS PARA MOVER */

    kW = game.input.keyboard.addKey(Phaser.Keyboard.W);
    /*kA = game.input.keyboard.addKey(Phaser.Keyboard.A);
    kS = game.input.keyboard.addKey(Phaser.Keyboard.S);
    kD = game.input.keyboard.addKey(Phaser.Keyboard.D);*/

    //teclas = game.input.keyboard.addKeys('W,S,A,D');
    teclas = game.input.keyboard.addKeys({
                                          'w': Phaser.Keyboard.W,
                                          's': Phaser.Keyboard.S,
                                          'a': Phaser.Keyboard.A,
                                          'd': Phaser.Keyboard.D
                                        });

    /*kW.onDown.add(Client.moveY, this);
    kS.onDown.add(Client.moveNY, this);
    */
    /*kD.onDown.add(Client.moveX, this);
    kA.onDown.add(Client.moveNX, this);*/
    
    layer.events.onInputUp.add(Game.getCoordinates, this);
    Client.askNewPlayer();
};

Game.update = function(){

    Client.moverJ(0, 0);

    if (teclas.w.isDown){
        Client.moverJ(0, -1);
    }  else
    
    if (teclas.s.isDown){
        Client.moverJ(0, 1);
    } else
    
    if (teclas.a.isDown){
        Client.moverJ(-1, 0);
    } else
    
    if (teclas.d.isDown){
        Client.moverJ(1, 0);
    } 

}

Game.getCoordinates = function(layer,pointer){
    //Client.sendClick(pointer.worldX,pointer.worldY);
};

Game.addNewPlayer = function(id,x,y){
    Game.playerMap[id] = game.add.sprite(x,y,'sprite');
    Game.physics.enable(Game.playerMap[id]);
};

Game.movePlayer = function(id,dx,dy){
    var player = Game.playerMap[id];
    player.body.velocity.y = dy;
    player.body.velocity.x = dx;
    //Client.socket.emit('atualizarJogador', {player:player});
};

Game.removePlayer = function(id){
    Game.playerMap[id].destroy();
    delete Game.playerMap[id];
};