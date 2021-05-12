const http = require('http');
const fs = require('fs');

http.createServer(function (req, res) {
    var fileName = './www' + req.url;
    fs.readFile(fileName, function(err, data){
        if (err){
            res.write(err);
        }else{
            res.write(data);
        }
        res.end();
    });
}).listen(30001);
