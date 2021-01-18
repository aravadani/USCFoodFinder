var path = require("path");

const routes = (app, dirname) => {
    app.route('/login.html')
    .post((req, res, next) => {
        //middleware
        console.log(`Request from: ${req.originalUrl}`);
        console.log(`Request type: ${req.method}`);
        // Check Authentication
        next();
    }, (req, res) => {
        res.sendFile(path.join(dirname + '/public/login.html'));
    })
}

module.exports = routes;