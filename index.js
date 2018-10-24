var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');
});

io.on('connection', function(socket){
  console.log('USUARIO CONECTADO');
  socket.on('chat message', function(msg){
      console.log('MENSSAGEM: '+msg);
      io.emit('chat message', msg);
  });
  socket.broadcast.emit('Ola');
});

http.listen(3000, function(){
  console.log('Escutando em: localhost:3000');
});