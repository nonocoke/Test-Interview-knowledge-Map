const fs = require('fs');

// readFile(filename, callback){};
fs.readFile('./www/index.html', function(err, data){
    if (err){
        console.log(err);
    }else{
        console.log(data.toString());
    }
});

// writeFile(filename, data, callback){};
fs.writeFile('./www/temp.txt', 'hhh', function(err){
    console.log(err);
});
