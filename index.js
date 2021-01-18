var express = require('express');
var bodyParser = require('body-parser');
var http = require('http');
// var socketIO = require('socket.io');
var routes = require('./src/routes/loginRoutes');


const app = express();
var httpServer = http.Server(app);
// var io = socketIO(httpServer);
const PORT = 4000;
app.use(express.static('public'));

routes(app, __dirname);

var server = app.listen(PORT, () => {
    console.log(`server is listening on port ${server.address().port}`);
});
